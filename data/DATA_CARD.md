# Data card — EVPromoAI

## Dataset 1 · Bối cảnh yêu cầu báo giá synthetic

| | |
|---|---|
| Dùng để làm gì | `get_quote_context` đọc giá chuyến, chi phí, ngân sách, trần voucher và hành vi tổng hợp; `validate_voucher` kiểm tra phương án. |
| Từ đâu | `data/quote_contexts.json`, nhóm tự viết 12 tình huống cho prototype CP2; không lấy từ nền tảng gọi xe. |
| Xử lý | Dùng mã giả `REQ-001`–`REQ-012`; chuẩn hóa tiền VND nguyên; không có tên, số điện thoại, vị trí hay dữ liệu cá nhân. |
| Số dòng | 12 bản ghi JSON. |
| Phiên bản / ngày | CP2 v1 · 27/11/2026. |
| Nhãn | `synthetic`, các edge case được thiết kế có chủ đích; không tuyên bố là mẫu ngẫu nhiên. |
| Giới hạn | Không phản ánh phân phối khách thật, không chứng minh voucher tăng chuyến và không dùng để suy ra pain/impact kinh doanh. |

Các tình huống phủ ngân sách thấp/hết, trần 5–15%, biên thấp và cả trường hợp 0% vẫn âm biên. Nguyễn Nho Trọng cần xác nhận lại 12/12 bản ghi trước CP3; chưa ghi là đã kiểm độc lập khi việc đó chưa thực hiện.

## Dataset 2 · Nguồn công khai về pain

| | |
|---|---|
| Dùng để làm gì | Tạo bối cảnh pain và chủ đề cho 10 câu thử; không cung cấp dữ liệu giao dịch hay nhãn mức voucher đúng. |
| Từ đâu | `evidence/public-sources.csv`: 5 tài liệu công khai từ Uber, DiDi, Booking.com và Grab. |
| Xử lý | Gắn mã S01–S05, lưu URL, vị trí dẫn và hai nhãn bối cảnh; chi tiết trong `evidence/data-mining.md`. |
| Số dòng | 5 tài liệu từ 4 tổ chức. |
| Giới hạn | Mẫu có chủ đích; không phải tỷ lệ người dùng gặp pain và không thay thế khảo sát/phỏng vấn. |

## Dataset 3 · Bộ câu thử CP2

`eval/benchmark.csv` có 20 câu: 6 thường, 10 khó, 4 từ chối. Mười câu dùng chủ đề từ nguồn công khai nhưng mọi số và request vẫn là synthetic; sáu câu tự viết và bốn câu dựa trên edge case. Không dùng kết quả bộ này để tuyên bố hiệu quả kinh doanh.
