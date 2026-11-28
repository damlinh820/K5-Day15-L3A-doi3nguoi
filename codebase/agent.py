"""Workflow E2: giao dịch mới → code kiểm ngưỡng → AI gợi ý → người dùng quyết định."""
import json
import re

from ai import call_model
from tools import _transactions, check_alert_rules, find_cut_candidates, get_budget_status, get_transaction
from tracing import note

SYSTEM = """Bạn hỗ trợ người dùng ví/app ngân hàng hiểu cảnh báo ngân sách.
Chỉ gợi ý 2–3 khoản không thiết yếu từ danh sách được cung cấp; không tự cộng tiền,
không phán xét, không gợi ý cắt tiền nhà, hóa đơn hay y tế, không tư vấn đầu tư
và không thực hiện giao dịch. Nói rõ người dùng có thể bỏ qua hoặc tắt cảnh báo."""
CHAT_SYSTEM = """Bạn trả lời ngắn gọn bằng tiếng Việt về đúng trạng thái ngân sách và
giao dịch được cung cấp. Không tự tính lại số liệu, không bịa dữ liệu, không tư vấn đầu tư,
không yêu cầu thông tin bí mật và không thực hiện giao dịch. Nếu câu hỏi ngoài ngữ cảnh,
hãy nói phạm vi hỗ trợ. Nhắc rằng người dùng có thể bỏ qua hoặc tắt cảnh báo khi phù hợp."""
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


def answer_group_question(question: str, user_id: str, category: str, through: str, budget: int) -> dict:
    """Hỏi đáp theo đúng một nhóm và ngày đang xem trong giao diện demo."""
    normalized = " ".join(question.lower().split())
    if any(term in normalized for term in FORBIDDEN):
        return {"output": "Từ chối: hệ thống không thực hiện giao dịch, xin thông tin bí mật hoặc tư vấn đầu tư."}
    rows = [row for row in _transactions() if row["user_id"] == user_id
            and (row["category"] == category or (category == "khac" and row["category"] == "thu_nhap_khac")) and row["date"].startswith(through[:7])
            and row["date"] <= through]
    spent = sum(row["amount"] for row in rows if row["amount"] > 0)
    net_saved = sum(row["amount"] for row in rows) if category == "tiet_kiem" else None
    context = {"nhom": category, "den_ngay": through, "muc_tieu_hoac_tran": None if category == "khac" else budget,
               "da_chi": None if category == "tiet_kiem" else spent,
               "tong_thu": sum(-row["amount"] for row in rows if row["amount"] < 0),
               "tiet_kiem_rong": net_saved, "giao_dich": rows}
    if category == "nha_o":
        context["phan_bo_co_dinh"] = budget
        context["ghi_chu"] = "Phân bổ 100% mức cố định khác với số tiền đã trả theo giao dịch; không tự tạo khoản chi."
    system = CHAT_SYSTEM + " Chỉ trả lời về nhóm được chọn, từ chối câu hỏi về nhóm khác. Tiết kiệm là tiền gửi trừ tiền rút, không phải chi tiêu. Nhà ở đã phân bổ khác với tiền đã trả."
    reply = call_model(system, "Dữ liệu nhóm:\n%s\nCâu hỏi:\n%s" % (json.dumps(context, ensure_ascii=False), question))
    if reply["model"] == "fake":
        return {"output": "Chế độ model giả chưa trả lời hội thoại. Hãy cấu hình model thật trong .env."}
    return {"output": reply["text"].strip()}


def answer_question(question: str, tx_id: str, budget_override=None) -> dict:
    """Trả lời câu hỏi tiếp nối bằng ngữ cảnh đã được code tính từ một giao dịch."""
    normalized = " ".join(question.lower().split())
    if any(term in normalized for term in FORBIDDEN):
        note("dừng chat: yêu cầu ngoài phạm vi tài chính an toàn")
        return {"output": "Từ chối: hệ thống không chuyển tiền, thanh toán, xin thông tin bí mật hoặc tư vấn đầu tư. Bạn có thể hỏi về cảnh báo và ngân sách đang hiển thị."}
    transaction = get_transaction(tx_id.strip().upper())
    if transaction is None:
        note("dừng chat: không tìm thấy tx_id")
        return {"output": "Không tìm thấy giao dịch đang chọn. Vui lòng chọn lại tình huống."}
    month = transaction["date"][:7]
    status = get_budget_status(transaction["user_id"], month, transaction["category"], transaction["date"])
    if isinstance(budget_override, int) and budget_override > 0:
        status["budget"] = budget_override
        status["ratio"] = status["spent"] / budget_override
    alert = check_alert_rules(status)
    candidates = find_cut_candidates(transaction["user_id"], month, transaction["date"])
    context = {
        "transaction": transaction,
        "budget_status": status,
        "alert": alert,
        "nonessential_candidates": candidates,
    }
    prompt = "Dữ liệu do code cung cấp:\n%s\n\nCâu hỏi của người dùng:\n%s" % (
        json.dumps(context, ensure_ascii=False), question.strip())
    reply = call_model(CHAT_SYSTEM, prompt)
    if reply["model"] == "fake":
        return {"output": "Chế độ model giả chưa trả lời hội thoại. Hãy cấu hình model thật trong .env để dùng mục Hỏi thêm."}
    return {"output": reply["text"].strip()}


def _answer(text: str, budget_override=None) -> dict:
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
    if isinstance(budget_override, int) and budget_override > 0:
        status["budget"] = budget_override
        status["ratio"] = status["spent"] / budget_override
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
                           f"Bạn có thể tiếp tục theo dõi, tự điều chỉnh ngân sách, hoặc bỏ qua/tắt cảnh báo.{essential_note}")}

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


def answer(text: str) -> dict:
    """Hợp đồng chính của khung eval và simulate."""
    return _answer(text)


def answer_with_budget(text: str, budget: int) -> dict:
    """Luồng demo khi người dùng đã chỉnh ngân sách của nhóm trên giao diện."""
    return _answer(text, budget)
