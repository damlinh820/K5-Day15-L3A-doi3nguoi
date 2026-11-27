# Kế hoạch đào review công khai — Track E2

Trạng thái CP2: đã chốt phương pháp trước khi thu mẫu; chưa có kết quả.

## Cách chọn mẫu

- Chọn 2 ứng dụng ví điện tử/app ngân hàng phổ biến mà nhóm mở được trang review công khai.
- Với mỗi ứng dụng, lấy 15 review gần nhất tính từ 27/11/2026 có nội dung liên quan đến quản lý chi tiêu, phân loại giao dịch, ngân sách hoặc cảnh báo; mọi mức sao.
- Không chỉ lọc review 1–3 sao. Ghi cả review không gặp vấn đề để tránh mẫu chỉ gồm phàn nàn.
- Bỏ tên người viết; lưu URL/trang nguồn, ngày review, số sao, tối đa 2 câu nguyên văn và nhãn.

## Nhãn đăng ký trước

| Nhãn | Định nghĩa |
|---|---|
| `phat_hien_muon` | Người dùng nói chỉ nhận ra chi nhiều/vượt ngân sách sau khi đã xảy ra. |
| `phan_loai_kho_hieu` | Mô tả hoặc nhóm giao dịch làm họ khó biết tiền đi đâu. |
| `canh_bao_khong_huu_ich` | Cảnh báo quá muộn, chung chung, sai hoặc không điều khiển được. |
| `khong_gap_pain` | Review liên quan nhưng không mô tả ba vấn đề trên. |
| `khong_lien_quan` | Sau khi đọc đủ nội dung, review không dùng được cho câu hỏi nghiên cứu. |

## Cách đếm

- Mẫu số N là toàn bộ review đã chọn và mã hóa, kể cả `khong_gap_pain` và `khong_lien_quan`.
- Báo từng nhãn dạng `x/N` và `%`; một review có thể có nhiều nhãn nên không cộng tỷ lệ thành 100%.
- Ít nhất một thành viên thứ hai kiểm lại 10 review; ghi số nhãn khớp thật.

File kết quả dự kiến: `evidence/review-sample.csv`. Chưa có dữ liệu thì không tạo dòng giả.
