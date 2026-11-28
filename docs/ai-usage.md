# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Soạn workflow E2: đọc giao dịch, tính ngưỡng, lọc khoản thiết yếu, gọi model giả | Đàm Tuấn Linh duyệt luồng; Nguyễn Nho Trọng chạy và kiểm code trước CP3 | Đàm Tuấn Linh, Nguyễn Nho Trọng |
| Prompt / thiết kế lời gọi mô hình | Codex | Soạn prompt giới hạn gợi ý và giọng không phán xét | Đàm Tuấn Linh đối chiếu `spec.md` §4 | Đàm Tuấn Linh |
| Đào data | Codex | Soạn kế hoạch, đọc RSS App Store công khai và đối chiếu 5 trích đoạn review E2; chưa hoàn thành mẫu 30 review theo kế hoạch | Ngô Văn Tuân kiểm lại nguồn và giới hạn; chưa có lượt kiểm độc lập 10 review | Ngô Văn Tuân |
| Rà câu hỏi khảo sát | Codex | Soạn 10 câu hỏi hành vi E2 và Apps Script tạo form | Ngô Văn Tuân duyệt, tạo form và chỉ ghi câu trả lời thật | Ngô Văn Tuân |
| Xử lý khảo sát | Codex | Đọc CSV thật 31 phản hồi do Tuân cung cấp, viết script ẩn danh/đếm lại; giữ các mốc 22/24 và tách hồ sơ gốc, hồ sơ mở rộng 16/14 | Ngô Văn Tuân kiểm dữ liệu, xác minh các cờ mâu thuẫn và điều kiện ngoài nhóm; không coi lựa chọn trắc nghiệm là lời phỏng vấn | Ngô Văn Tuân |
| Viết câu thử | Codex | Soạn 20 tình huống và pass criterion | Nguyễn Nho Trọng kiểm chéo; bổ sung câu từ dữ liệu thật trước CP3 | Nguyễn Nho Trọng |
| Sinh data `synthetic` | Codex | Soạn script sinh 252 giao dịch, 3 persona, seed 42 | Nguyễn Nho Trọng kiểm tay edge case và số dòng | Nguyễn Nho Trọng |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
