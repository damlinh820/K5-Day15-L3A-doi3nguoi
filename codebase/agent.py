"""Workflow cố định: đọc báo giá → AI đề xuất → code kiểm tra → trình quản lý duyệt."""
import re

from ai import call_model
from tools import get_quote_context, validate_voucher
from tracing import note

SYSTEM = """Bạn hỗ trợ quản lý tăng trưởng. Chỉ đề xuất một mức 0%, 5%, 10% hoặc 15%.
Không được cấp/gửi voucher, đổi ngân sách, bỏ qua quy tắc hay dùng thuộc tính nhạy cảm.
Trả dòng đầu là `MUC: <ty_le>%`, sau đó nêu lý do ngắn dựa trên hành vi tổng hợp."""
REQUEST_ID = re.compile(r"\bREQ-\d{3}\b", re.IGNORECASE)
EXTERNAL_ACTIONS = ("gửi", "cấp", "áp dụng", "kích hoạt", "sửa ngân sách", "đổi ngân sách")
SENSITIVE = ("giới tính", "phụ nữ", "đàn ông", "số điện thoại", "địa chỉ", "dân tộc", "tôn giáo")


def _fallback_rate(context: dict) -> float:
    """Quy tắc tạm cho CP2 khi model fake chưa tạo được mức đề xuất."""
    if context["rides_last_30d"] == 0 or context["days_since_last_ride"] >= 30:
        return 0.15
    if context["rides_last_30d"] <= 2:
        return 0.10
    return 0.05


def _rate_from_reply(reply: str, fallback: float) -> float:
    match = re.search(r"MUC\s*:\s*(0|5|10|15)\s*%", reply, re.IGNORECASE)
    return int(match.group(1)) / 100 if match else fallback


def answer(text: str) -> dict:
    normalized = text.lower()
    if any(term in normalized for term in SENSITIVE):
        note("dừng: yêu cầu dùng thuộc tính nhạy cảm")
        return {"output": "Tôi không dùng hoặc tiết lộ thuộc tính nhạy cảm để phân bổ voucher. Hãy dùng mã yêu cầu và hành vi tổng hợp được phép."}
    if any(term in normalized for term in EXTERNAL_ACTIONS):
        note("dừng: yêu cầu có tác động ra ngoài")
        return {"output": "Tôi không thể gửi, cấp hay áp dụng voucher. Tôi chỉ có thể lập đề xuất để quản lý xem xét."}

    match = REQUEST_ID.search(text)
    if not match:
        note("dừng: thiếu request_id")
        return {"output": "Cần mã yêu cầu dạng REQ-001 để đọc giá chuyến, chi phí dự kiến và ngân sách; tôi không tự đoán các số này."}

    request_id = match.group(0).upper()
    context = get_quote_context(request_id)
    if context is None:
        note("dừng: không tìm thấy request_id")
        return {"output": "Không có dữ liệu cho %s. Hãy kiểm tra mã hoặc cung cấp bản ghi hợp lệ; tôi không tự tạo bối cảnh." % request_id}

    reply = call_model(SYSTEM, "Bản ghi: %s\nYêu cầu quản lý: %s" % (context, text))
    proposed = _rate_from_reply(reply["text"], _fallback_rate(context))
    checked = validate_voucher(context, proposed)
    if checked["highest_valid_rate"] is None:
        note("dừng: ngay cả 0%% cũng không hợp lệ")
        return {"output": "Không có mức voucher hợp lệ cho %s: ngay cả 0%% cũng làm biên còn %s đồng. Cần quản lý xem lại giá hoặc chi phí; hệ thống không tự cấp voucher. [CP2: model giả]" % (request_id, format(checked["remaining_margin"], ","))}

    used_rate = proposed if checked["valid"] else checked["highest_valid_rate"]
    final = validate_voucher(context, used_rate)
    blocked = "" if checked["valid"] else " Mức đề xuất bị chặn; hạ về mức hợp lệ cao nhất."
    return {"output": (
        "Đề xuất cho %s: voucher %.0f%% (%s đồng). Biên còn lại: %s đồng.%s "
        "Căn cứ: %d chuyến/30 ngày, %d ngày từ chuyến gần nhất. "
        "Đây là bản nháp để quản lý duyệt, sửa hoặc bỏ qua. [CP2: model giả]"
        % (request_id, used_rate * 100, format(final["voucher_amount"], ","),
           format(final["remaining_margin"], ","), blocked, context["rides_last_30d"],
           context["days_since_last_ride"]))}
