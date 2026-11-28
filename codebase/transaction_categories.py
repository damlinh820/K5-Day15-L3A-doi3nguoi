"""Nhận diện nhóm giao dịch demo bằng các cụm từ rõ nghĩa, không gọi model."""
import re
import unicodedata


RULES = {
    "out": {
        "an_uong": ("tra sua", "ca phe", "cafe", "an trua", "an sang", "an toi", "com van phong", "nha hang", "quan an"),
        "di_lai": ("do xang", "tien xang", "gui xe", "taxi", "xe om", "ve xe buyt"),
        "mua_sam": ("mua quan ao", "mua giay dep", "mua sam", "sieu thi"),
        "giai_tri": ("xem phim", "ve xem phim", "karaoke", "choi game", "ve hoa nhac"),
        "nha_o": ("tien nha", "tien thue nha", "thue phong tro", "thue nha"),
        "hoa_don": ("tien dien", "tien nuoc", "hoa don dien", "hoa don nuoc", "tien internet"),
        "y_te": ("tien thuoc", "mua thuoc", "kham benh", "vien phi"),
        "tra_no": ("tra no", "tra gop", "thanh toan khoan vay"),
        "cho_vay": ("cho vay",),
        "tiet_kiem": ("gui tiet kiem", "nap tiet kiem", "chuyen vao tiet kiem"),
    },
    "in": {
        "khac": ("nhan luong", "luong thang", "tien luong", "thuong cong ty"),
        "tiet_kiem": ("rut tiet kiem", "tat toan tiet kiem", "rut tien tiet kiem"),
        "cho_vay": ("thu hoi cho vay", "thu hoi tien cho vay"),
    },
}


def normalize(text: str) -> str:
    """Bỏ dấu, chữ hoa và dấu câu, giữ ranh giới từ."""
    text = unicodedata.normalize("NFD", text.casefold().replace("đ", "d"))
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text).split())


def detect_category(description: str, transaction_type: str) -> str | None:
    """Trả nhóm duy nhất khớp rõ ràng; không chắc chắn thì trả None."""
    normalized = " " + normalize(description) + " "
    matched = {category for category, phrases in RULES.get(transaction_type, {}).items()
               if any(" " + phrase + " " in normalized for phrase in phrases)}
    return next(iter(matched)) if len(matched) == 1 else None
