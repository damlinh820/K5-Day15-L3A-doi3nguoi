"""Giao diện demo local cho luồng E2; chạy bằng python codebase/demo_server.py."""
import json
import re
from datetime import date as calendar_date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import tracing
from agent import answer_group_question, answer_question, answer_with_budget
from tools import (add_demo_transaction, classify_demo_transaction, _budgets,
                   _transactions, get_budget_status)
from transaction_categories import detect_category

PAGE = Path(__file__).with_name("demo.html")
FINANCE = Path(__file__).parent.parent / "data" / "demo_finance.json"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CATEGORIES = {"an_uong", "di_lai", "mua_sam", "giai_tri", "nha_o", "hoa_don", "y_te", "tra_no", "cho_vay", "tiet_kiem", "khac", "thu_nhap_khac"}


def scenarios():
    """Ba mốc thời gian cố định của cùng một persona và tháng synthetic."""
    cases = {
        "salary": ("TX-U001-202609-ANUONG-01", "2026-09-05"),
        "mid": ("TX-U001-202609-DILAI-03", "2026-09-14"),
        "end": ("TX-U001-202609-GIAITRI-04", "2026-09-30"),
    }
    rows = {tx["tx_id"]: tx for tx in _transactions()}
    return {key: {"transaction": rows[tx_id], "as_of": as_of,
                  "status": get_budget_status("U001", "2026-09", rows[tx_id]["category"], as_of)}
            for key, (tx_id, as_of) in cases.items()}


class Handler(BaseHTTPRequestHandler):
    def send_data(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, data):
        self.send_data(status, json.dumps(data, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self):
        if self.path == "/":
            self.send_data(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/scenarios":
            self.send_json(200, scenarios())
        elif self.path == "/api/transactions":
            self.send_json(200, _transactions())
        elif self.path == "/api/budgets":
            self.send_json(200, _budgets())
        elif self.path == "/api/finance":
            self.send_json(200, json.loads(FINANCE.read_text(encoding="utf-8")))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path not in ("/api/analyze", "/api/transaction", "/api/classify"):
            self.send_error(404)
            return
        # Chỉ nhận yêu cầu từ chính giao diện local.
        if self.headers.get("Origin") != f"http://{self.headers.get('Host')}":
            self.send_error(403)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > 4096:
                raise ValueError("invalid length")
            data = json.loads(self.rfile.read(length))
            if not isinstance(data, dict):
                raise ValueError("invalid data")
        except (ValueError, TypeError, json.JSONDecodeError):
            self.send_json(400, {"error": "Đầu vào không hợp lệ."})
            return

        if self.path == "/api/transaction":
            try:
                user_id = data["user_id"]
                date = data["date"]
                description_raw = data["description"]
                description = description_raw.strip() if isinstance(description_raw, str) else ""
                amount = data["amount"]
                tx_type = data["type"]
                category = data.get("category") or "chua_phan_loai"
                calendar_date.fromisoformat(date)
                if (user_id not in _budgets() or not isinstance(date, str) or not DATE.match(date)
                        or not isinstance(description, str) or not description or len(description) > 120
                        or not isinstance(amount, int) or amount < 1 or tx_type not in ("in", "out")
                        or category not in CATEGORIES | {"chua_phan_loai"}):
                    raise ValueError("invalid transaction")
                classification = "manual"
                if category == "chua_phan_loai":
                    category = detect_category(description, tx_type) or "chua_phan_loai"
                    classification = "auto" if category != "chua_phan_loai" else "pending"
                number = 1 + sum(1 for row in _transactions() if row["tx_id"].startswith(f"TX-{user_id}-{date[:4]+date[5:7]}-DEMO"))
                transaction = add_demo_transaction({
                    "tx_id": f"TX-{user_id}-{date[:4]+date[5:7]}-DEMO-{number:02d}",
                    "user_id": user_id, "date": date, "description": description,
                    "amount": -amount if tx_type == "in" else amount,
                    "category": category, "is_essential": category in {"nha_o", "hoa_don", "y_te", "tra_no", "cho_vay", "tiet_kiem"},
                })
                self.send_json(201, {**transaction, "classification": classification})
            except (KeyError, TypeError, ValueError):
                self.send_json(400, {"error": "Giao dịch không hợp lệ."})
            return

        if self.path == "/api/classify":
            tx_id, category = data.get("tx_id"), data.get("category")
            transaction = (classify_demo_transaction(tx_id, category)
                           if isinstance(tx_id, str) and category in CATEGORIES else None)
            self.send_json(200, transaction) if transaction else self.send_json(404, {"error": "Không tìm thấy giao dịch demo."})
            return

        try:
            text = data["text"]
            if not isinstance(text, str) or not text.strip() or len(text) > 1000:
                raise ValueError("invalid text")
            mode = data.get("mode", "analyze")
            tx_id = data.get("tx_id", "")
            budget = data.get("budget")
            if (mode not in ("analyze", "question", "group_question") or not isinstance(tx_id, str)
                    or isinstance(budget, bool) or not isinstance(budget, int) or budget < (0 if mode == "group_question" else 1)):
                raise ValueError("invalid mode")
            if mode == "group_question":
                user_id, category, through = data["user_id"], data["category"], data["through"]
                if user_id not in _budgets() or category not in _budgets()[user_id]:
                    raise ValueError("invalid group")
                calendar_date.fromisoformat(through)
        except (ValueError, KeyError, TypeError):
            self.send_json(400, {"error": "Đầu vào không hợp lệ."})
            return
        tracing.begin("demo")
        try:
            if mode == "group_question":
                result = answer_group_question(text, user_id, category, through, budget)
            elif mode == "question":
                result = answer_question(text, tx_id, budget)
            else:
                result = answer_with_budget(text, budget)
            summary, _ = tracing.end()
            self.send_json(200, {"output": result["output"], "models": summary["models"], "model_calls": summary["model_calls"]})
        except Exception:
            tracing.end()
            self.send_json(502, {"error": "Không thể phân tích lúc này. Kiểm tra cấu hình model, kết nối rồi thử lại."})


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8765), Handler)
    print("Mở http://127.0.0.1:8765 — dừng bằng Ctrl+C", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
