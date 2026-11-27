"""Sinh dữ liệu chi tiêu synthetic cho E2. Chỉ dùng thư viện chuẩn."""
import csv
import json
import random
from datetime import date
from pathlib import Path

SEED = 42
ROOT = Path(__file__).parent
CATEGORIES = {
    "an_uong": (False, ["TRASUA*HANOI", "com van phong", "CAFE 24H"]),
    "di_lai": (False, ["XEMAU*BIKE", "xe mau", "BUS CITY"]),
    "mua_sam": (False, ["SHOP ONLINE", "SIEUTHI*STORE", "CLOTHES HN"]),
    "giai_tri": (False, ["CINEMA", "GAME ONLINE", "MUSIC APP"]),
    "nha_o": (True, ["TIEN NHA", "HOME RENT", "PHI CHUNG CU"]),
    "hoa_don": (True, ["DIEN LUC", "INTERNET", "MOBILE BILL"]),
    "y_te": (True, ["NHA THUOC", "PHONG KHAM", "HOSPITAL"]),
}
USERS = [
    {"user_id": "U001", "persona": "sinh_vien", "description": "Sinh viên theo dõi sát ăn uống và đi lại."},
    {"user_id": "U002", "persona": "nhan_vien_van_phong", "description": "Nhân viên văn phòng có nhiều chi mua sắm và ăn ngoài."},
    {"user_id": "U003", "persona": "nguoi_lo_chi_tieu_gia_dinh", "description": "Người quản lý chi tiêu gia đình, ưu tiên khoản thiết yếu."},
]
BUDGETS = {
    "U001": {"an_uong": 600000, "di_lai": 500000, "mua_sam": 700000, "giai_tri": 400000, "nha_o": 2500000, "hoa_don": 600000, "y_te": 500000},
    "U002": {"an_uong": 1800000, "di_lai": 1000000, "mua_sam": 1200000, "giai_tri": 900000, "nha_o": 5000000, "hoa_don": 1200000, "y_te": 1000000},
    "U003": {"an_uong": 3000000, "di_lai": 1500000, "mua_sam": 2000000, "giai_tri": 800000, "nha_o": 7000000, "hoa_don": 2500000, "y_te": 1000000},
}
EDGE_AMOUNTS = {
    ("U001", "an_uong"): [120000, 140000, 160000, 180000],
    ("U002", "mua_sam"): [200000, 300000, 350000, 400000],
    ("U003", "y_te"): [100000, 100000, 200000, 700000],
}


def amount_for(rng, user_id, month, category, index):
    if month == "2026-11" and (user_id, category) in EDGE_AMOUNTS:
        return EDGE_AMOUNTS[(user_id, category)][index - 1]
    essential = CATEGORIES[category][0]
    low, high = (180000, 800000) if essential else (40000, 350000)
    return rng.randrange(low // 10000, high // 10000 + 1) * 10000


def build_transactions():
    rng = random.Random(SEED)
    rows = []
    for user in USERS:
        user_id = user["user_id"]
        for month in ("2026-09", "2026-10", "2026-11"):
            year, month_number = map(int, month.split("-"))
            for category, (essential, descriptions) in CATEGORIES.items():
                code = category.replace("_", "").upper()
                for index, day in enumerate((3, 8, 14, 20), start=1):
                    rows.append({
                        "tx_id": f"TX-{user_id}-{year}{month_number:02d}-{code}-{index:02d}",
                        "user_id": user_id,
                        "date": date(year, month_number, day).isoformat(),
                        "description": descriptions[(index - 1) % len(descriptions)],
                        "amount": amount_for(rng, user_id, month, category, index),
                        "category": category,
                        "is_essential": "1" if essential else "0",
                    })
    return rows


def main():
    rows = build_transactions()
    with (ROOT / "transactions.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (ROOT / "users.json").write_text(json.dumps(USERS, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "budgets.json").write_text(json.dumps(BUDGETS, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} transactions for {len(USERS)} personas with seed {SEED}")


if __name__ == "__main__":
    main()
