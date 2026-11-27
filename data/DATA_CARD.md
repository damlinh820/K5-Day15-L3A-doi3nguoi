# Data card — dữ liệu bản chạy thử dùng

## Dataset 1 · Bối cảnh yêu cầu báo giá synthetic

| | |
|---|---|
| Dùng để làm gì | Công cụ `get_quote_context` đọc giá chuyến, chi phí dự kiến, ngân sách, trần voucher và hai trường hành vi tổng hợp; làm căn cứ cho một phần câu thử. |
| Từ đâu | Nhóm tự viết cho bản chạy thử CP2; không lấy từ nền tảng gọi xe, không có dữ liệu cá nhân thật. |
| Xử lý những bước gì | Thiết kế 12 bản ghi có chủ đích cho các tình huống thường, trần campaign, cạn ngân sách và âm biên; chuẩn hóa tiền theo VND nguyên; không cần ẩn danh vì không chứa cá nhân. |
| Số dòng / số đoạn | 12 bản ghi JSON. |
| Phiên bản / ngày lấy | `quote_contexts.json` v1 · 27/11/2026. |
| Nhãn | `synthetic`. |
| Giới hạn | Không phản ánh phân phối khách thật, không chứng minh voucher tạo thêm chuyến, không dùng để suy ra pain hay impact kinh doanh. |

**Cách sinh và kiểm:** dữ liệu được viết theo schema trong `spec.md` §4, với seed ghi nhãn là 42 để truy vết bộ tình huống. Codex đã kiểm cấu trúc 12/12 bản ghi, các trường bắt buộc và số không âm; Nguyễn Nho Trọng cần xác nhận nội dung/tình huống trước khi nộp. Không dùng prompt hoặc dữ liệu cá nhân để sinh.

## Dataset 2 · Bộ câu thử CP2

| | |
|---|---|
| Dùng để làm gì | Kiểm workflow `answer(text)`: tra bối cảnh, đề xuất voucher, kiểm tra quy tắc, thiếu dữ liệu và từ chối tác động ngoài phạm vi. |
| Từ đâu | Nhóm tự viết từ 8 kịch bản trong `spec.md` §5 và 12 bản ghi synthetic ở Dataset 1. |
| Xử lý những bước gì | Mỗi câu có `expected`, `pass_criterion`, `type` và `source`; chưa lấy từ người dùng hoặc dữ liệu thật. |
| Số dòng / số đoạn | 12 câu trong `eval/benchmark.csv`: thường 3, khó 6, từ chối 3. |
| Phiên bản / ngày lấy | CP2 v1 · 27/11/2026. |
| Nhãn | `synthetic` và `tu_viet`. |
| Giới hạn | Chưa đạt yêu cầu CP3 về 20–30 câu và ≥1/3 câu từ người dùng/dữ liệu thật; không dùng kết quả của bộ này để kết luận chất lượng thực tế. |

Các bản ghi và câu thử ở đây không phải bằng chứng pain; bằng chứng được lưu riêng trong `evidence/`.
