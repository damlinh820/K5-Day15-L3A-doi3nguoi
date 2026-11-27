"""Công cụ đọc bối cảnh voucher và kiểm tra quy tắc tài chính."""
import json
import os

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "data", "quote_contexts.json")
ALLOWED_RATES = (0.00, 0.05, 0.10, 0.15)
REQUIRED_FIELDS = ("fare_amount", "estimated_cost", "remaining_budget", "max_voucher_rate")


@tool
def get_quote_context(request_id: str) -> dict | None:
    """get_quote_context · Input: request_id · Output: bản ghi synthetic hoặc None · Không tác động ra ngoài."""
    with open(DATA_PATH, encoding="utf-8") as file:
        records = json.load(file)
    wanted = request_id.strip().upper()
    return next((record for record in records if record["request_id"] == wanted), None)


def missing_required_fields(context: dict) -> list:
    """Trả danh sách trường bắt buộc bị thiếu; hàm thuần, không ghi trace riêng."""
    return [field for field in REQUIRED_FIELDS if context.get(field) is None]


@tool
def validate_voucher(context: dict, proposed_rate: float) -> dict:
    """validate_voucher · Input: bối cảnh + tỷ lệ đề xuất · Output: phép tính và mức hợp lệ · Không tác động ra ngoài."""
    missing = missing_required_fields(context)
    if missing:
        return {"valid": False, "missing_fields": missing, "highest_valid_rate": None}
    fare, cost = context["fare_amount"], context["estimated_cost"]
    budget, cap = context["remaining_budget"], context["max_voucher_rate"]

    def check(rate: float) -> dict:
        amount = round(fare * rate)
        margin = fare - cost - amount
        conditions = {
            "muc_duoc_phep": rate in ALLOWED_RATES,
            "khong_vuot_tran_voucher": rate <= cap,
            "khong_vuot_ngan_sach": amount <= budget,
            "khong_am_bien": margin >= 0,
        }
        return {"rate": rate, "voucher_amount": amount, "remaining_margin": margin,
                "conditions": conditions, "valid": all(conditions.values())}

    candidate = round(float(proposed_rate), 2)
    result = check(candidate)
    valid_rates = [rate for rate in ALLOWED_RATES if check(rate)["valid"]]
    result["highest_valid_rate"] = max(valid_rates) if valid_rates else None
    return result
