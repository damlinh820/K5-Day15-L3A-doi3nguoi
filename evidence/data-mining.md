# Rà tài liệu công khai — cách chọn nguồn và kết quả

Ngày truy cập: **27/11/2026**. Phụ trách: Ngô Văn Tuân; Codex hỗ trợ tìm và tổng hợp, Tuân kiểm lại trước khi nộp.

Đây là tổng quan tài liệu, chưa phải bộ review hay dữ liệu hành vi người dùng. Không dùng số tài liệu để thay ngưỡng trong `hypothesis.md`.

## 1. Cách tìm và chọn nguồn

- Tìm theo các cụm: `promotion uplift budget allocation incentive`, `ride hailing coupon allocation budget constraints`, `Supporting large campaigns at scale`, `Using Causal Inference to Improve the Uber User Experience`.
- Chọn nguồn do doanh nghiệp trực tiếp vận hành hoặc tác giả nghiên cứu công bố; có nội dung đọc được, xuất bản không muộn hơn ngày truy cập và liên quan đến coupon, ngân sách hoặc vận hành chiến dịch.
- Loại bản đăng lại, trang tổng hợp, tuyển dụng và kết quả chỉ có snippet chưa kiểm tra nội dung gốc.
- Chọn mẫu có chủ đích, không phải mẫu ngẫu nhiên hay tìm kiếm hệ thống toàn bộ tài liệu. Đây là ghi chép phương pháp sau khi đọc nguồn, không phải kế hoạch mã hóa đăng ký trước.
- Danh mục: [public-sources.csv](public-sources.csv). Một dòng là một tài liệu; bản trùng URL/khu vực của cùng bài chỉ tính một lần.

## 2. Quy tắc mã hóa

| Cột | Quy tắc |
|---|---|
| `budget_constraint` | 1 nếu phần được dẫn nêu giới hạn ngân sách khi phân bổ ưu đãi; ngược lại 0. |
| `manual_operations` | 1 nếu phần được dẫn mô tả thao tác chiến dịch thủ công từng xảy ra; ngược lại 0. |
| `scope` | Phạm vi của nguồn, dùng để tránh suy rộng từ tài xế/giao đồ ăn/du lịch sang voucher hành khách. |

Cột mã hóa được Codex gán từ nội dung nguồn, chưa có người thứ hai chấm độc lập. Giá trị 0 là không có trong phần được dẫn, không khẳng định vấn đề không tồn tại.

## 3. Kết quả và cách đếm lại

| Đếm gì | x/N | % | Diễn giải |
|---|---|---|---|
| Tài liệu đề cập giới hạn ngân sách | 3/5 | 60% | S01, S02, S03. |
| Tài liệu mô tả vận hành thủ công trước đây | 2/5 | 40% | S01, S04; không phải tình trạng hiện tại đã xác nhận. |

**N = 5 tài liệu**, thuộc 4 tổ chức Uber, DiDi, Booking.com, Grab; không phải 5 người dùng độc lập. Các tỷ lệ chỉ mô tả tập tài liệu đã chọn, không đo tỷ lệ người dùng gặp pain.

Chạy từ thư mục gốc, chỉ dùng Python standard library:

```powershell
@'
import csv
from pathlib import Path
rows = list(csv.DictReader(Path("evidence/public-sources.csv").open(encoding="utf-8-sig", newline="")))
print("sources:", len(rows))
print("organizations:", len({row["organization"] for row in rows}))
for column in ("budget_constraint", "manual_operations"):
    count = sum(int(row[column]) for row in rows)
    print(f"{column}: {count}/{len(rows)} ({count / len(rows):.0%})")
'@ | python -X utf8 -
```

Lệnh chỉ kiểm lại phép đếm trên bảng đã mã hóa; người kiểm cần mở link và vị trí dẫn để xác nhận nội dung/mã hóa. Năm ví dụ nguyên văn và giới hạn từng nguồn nằm ở [summary.md](summary.md).

## 4. Giới hạn và bước kiểm chứng tiếp

- Không thu được review hay phỏng vấn người vận hành trong lần rà này. Nguồn doanh nghiệp có thể thiên về giới thiệu giải pháp đã xây.
- Chưa biết số lần pain/tháng, thời gian mất, chi phí trợ giá thừa hay nhu cầu dùng sản phẩm của người dùng mục tiêu.
- Không có dữ liệu giao dịch hoặc nhóm đối chứng để chứng minh voucher tạo thêm chuyến; dữ liệu demo dựng chỉ dùng kiểm tra luồng và quy tắc.
- Bước tiếp theo: phỏng vấn ≥3 người ngoài nhóm có kinh nghiệm vận hành khuyến mãi; hoặc thu bộ review thật theo kế hoạch gốc, đồng thời làm rõ giới hạn vì reviewer có thể là hành khách.
