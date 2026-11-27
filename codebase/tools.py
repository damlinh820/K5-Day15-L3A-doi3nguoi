"""Công cụ E2: đọc giao dịch, tính ngân sách và tìm khoản có thể cắt."""
import csv
import json
import os
from collections import defaultdict

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
THRESHOLD = 0.80


def _transactions():
    with open(os.path.join(DATA_DIR, "transactions.csv"), encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["amount"] = int(row["amount"])
        row["is_essential"] = row["is_essential"] == "1"
    return rows


def _budgets():
    with open(os.path.join(DATA_DIR, "budgets.json"), encoding="utf-8") as handle:
        return json.load(handle)


@tool
def get_transaction(tx_id: str) -> dict | None:
    """get_transaction · Input: tx_id · Output: giao dịch synthetic hoặc None · Không tác động ra ngoài."""
    wanted = tx_id.strip().upper()
    return next((row for row in _transactions() if row["tx_id"].upper() == wanted), None)


@tool
def get_budget_status(user_id: str, month: str, category: str, through_date: str) -> dict:
    """get_budget_status · Input: user, tháng, nhóm, ngày · Output: chi/budget/tỷ lệ · Không tác động ra ngoài."""
    budget = int(_budgets()[user_id][category])
    rows = [row for row in _transactions() if row["user_id"] == user_id
            and row["date"].startswith(month) and row["category"] == category
            and row["date"] <= through_date]
    spent = sum(row["amount"] for row in rows)
    return {"user_id": user_id, "month": month, "category": category,
            "through_date": through_date, "spent": spent, "budget": budget,
            "ratio": spent / budget if budget else None, "transaction_count": len(rows)}


@tool
def check_alert_rules(status: dict) -> dict:
    """check_alert_rules · Input: trạng thái ngân sách · Output: có cảnh báo và lý do · Không tác động ra ngoài."""
    ratio = status.get("ratio")
    alert = ratio is not None and ratio >= THRESHOLD
    return {"alert": alert, "threshold": THRESHOLD,
            "reason": "spend_ratio_at_least_80_percent" if alert else "below_threshold"}


@tool
def find_cut_candidates(user_id: str, month: str, through_date: str) -> list:
    """find_cut_candidates · Input: user, tháng, ngày · Output: khoản không thiết yếu tổng hợp · Không tác động ra ngoài."""
    grouped = defaultdict(lambda: {"amount": 0, "count": 0})
    for row in _transactions():
        if (row["user_id"] != user_id or not row["date"].startswith(month)
                or row["date"] > through_date or row["is_essential"]):
            continue
        key = (row["category"], row["description"])
        grouped[key]["amount"] += row["amount"]
        grouped[key]["count"] += 1
    candidates = [{"category": key[0], "description": key[1], **value}
                  for key, value in grouped.items()]
    return sorted(candidates, key=lambda item: item["amount"], reverse=True)[:5]
