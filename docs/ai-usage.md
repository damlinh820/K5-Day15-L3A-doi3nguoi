# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Soạn workflow đọc request, gọi model giả và kiểm tra quy tắc tài chính | Đàm Tuấn Linh duyệt luồng; Nguyễn Nho Trọng chạy và kiểm code trước CP3 | Đàm Tuấn Linh, Nguyễn Nho Trọng |
| Prompt / thiết kế lời gọi mô hình | Codex | Soạn system prompt giới hạn mức voucher và thẩm quyền | Đàm Tuấn Linh đối chiếu `spec.md` §4 | Đàm Tuấn Linh |
| Đào data (viết script đếm, gợi ý nhãn) | Codex | Hỗ trợ tổng hợp nguồn công khai và cách đếm | Ngô Văn Tuân phải mở lại 5 nguồn và kiểm từng nhãn; chưa ghi là đã kiểm độc lập | Ngô Văn Tuân |
| Rà câu hỏi phỏng vấn / khảo sát | Codex | Soạn câu hỏi hành vi, tránh hỏi dẫn dắt | Ngô Văn Tuân duyệt và chỉ ghi câu trả lời thật | Ngô Văn Tuân |
| Viết câu thử (benchmark) | Codex | Soạn 20 tình huống và pass criterion | Mỗi câu ghi nguồn; Nguyễn Nho Trọng cần kiểm chéo trước CP3 | Nguyễn Nho Trọng |
| Sinh data `synthetic` (nếu có) | Codex + Nguyễn Nho Trọng | Soạn 12 bối cảnh có chủ đích cho các edge case | Nguyễn Nho Trọng cần kiểm tay 12 bản ghi, chưa ghi kết quả khi chưa làm | Nguyễn Nho Trọng |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
