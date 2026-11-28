"""Workflow E2: giao dịch mới → code kiểm ngưỡng → AI gợi ý → người dùng quyết định."""
import json
import re

from ai import call_model
from tools import check_alert_rules, find_cut_candidates, get_budget_status, get_transaction
from tracing import note

SYSTEM = """Bạn hỗ trợ người dùng ví/app ngân hàng hiểu cảnh báo ngân sách.
Chỉ gợi ý 2–3 khoản không thiết yếu từ danh sách được cung cấp; không tự cộng tiền,
không phán xét, không gợi ý cắt tiền nhà, hóa đơn hay y tế, không tư vấn đầu tư
và không thực hiện giao dịch. Nói rõ người dùng có thể bỏ qua hoặc tắt cảnh báo."""
TX_ID = re.compile(r"\bTX-U\d{3}-\d{6}-[A-Z]+-\d{2}\b", re.IGNORECASE)
FORBIDDEN = ("chuyển tiền", "thanh toán hộ", "mua cổ phiếu", "đầu tư", "xin otp",
             "mật khẩu", "số thẻ", "transfer money", "buy stock")


def _money(value):
    return f"{int(value):,}".replace(",", ".") + "đ"


def _fake_suggestions(candidates):
    if not candidates:
        return "Chưa có khoản không thiết yếu đủ căn cứ để gợi ý cắt giảm"
    items = ["giảm %s (%s, %s lần)" % (item["description"], _money(item["amount"]), item["count"])
             for item in candidates[:2]]
    return "; ".join(items)


def answer(text: str) -> dict:
    normalized = " ".join(text.lower().split())
    if any(term in normalized for term in FORBIDDEN):
        note("dừng: yêu cầu ngoài phạm vi tài chính an toàn")
        return {"output": "Từ chối: hệ thống không chuyển tiền, thanh toán, xin thông tin bí mật hoặc tư vấn đầu tư. Hãy dùng kênh chính thức của ví/ngân hàng nếu cần hỗ trợ giao dịch."}
    match = TX_ID.search(text)
    if not match:
        note("dừng: thiếu tx_id")
        return {"output": "Chưa đủ thông tin: vui lòng cung cấp mã giao dịch synthetic dạng TX-U001-202611-ANUONG-04; hệ thống không tự đoán giao dịch."}
    tx_id = match.group(0).upper()
    transaction = get_transaction(tx_id)
    if transaction is None:
        note("dừng: không tìm thấy tx_id")
        return {"output": f"Không có dữ liệu cho {tx_id}. Vui lòng kiểm tra mã; hệ thống không tự tạo giao dịch."}

    month = transaction["date"][:7]
    status = get_budget_status(transaction["user_id"], month, transaction["category"], transaction["date"])
    alert = check_alert_rules(status)
    ratio_text = "%.0f%%" % (status["ratio"] * 100)
    if not alert["alert"]:
        essential_note = (
            " Đây là nhóm thiết yếu nên hệ thống không gợi ý cắt giảm."
            if transaction["is_essential"]
            else ""
        )
        return {"output": (f"Không bật cảnh báo cho {tx_id}: nhóm {transaction['category']} đã chi "
                           f"{_money(status['spent'])}/{_money(status['budget'])} ({ratio_text}), dưới ngưỡng 80%. "
                           f"Bạn có thể tiếp tục theo dõi hoặc tự điều chỉnh ngân sách.{essential_note}")}

    candidates = find_cut_candidates(transaction["user_id"], month, transaction["date"])
    prompt = "Trạng thái do code tính:\n%s\nKhoản không thiết yếu:\n%s" % (
        json.dumps(status, ensure_ascii=False), json.dumps(candidates, ensure_ascii=False))
    reply = call_model(SYSTEM, prompt)
    suggestions = _fake_suggestions(candidates) if reply["model"] == "fake" else reply["text"].strip()
    essential_note = " Không gợi ý cắt nhóm thiết yếu này." if transaction["is_essential"] else ""
    return {"output": (f"Cảnh báo {tx_id}: nhóm {transaction['category']} đã chi "
                       f"{_money(status['spent'])}/{_money(status['budget'])} ({ratio_text}), chạm ngưỡng 80%."
                       f"{essential_note} Gợi ý từ {'AI giả CP2' if reply['model'] == 'fake' else reply['model']}: "
                       f"{suggestions}. Đây chỉ là gợi ý; bạn có thể bỏ qua hoặc tắt cảnh báo.")}
