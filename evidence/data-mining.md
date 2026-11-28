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

## Nhật ký thực hiện CP3 — 28/11/2026

- Đã truy cập Apple App Store Việt Nam qua RSS công khai, tối đa 10 trang × 50 review cho mỗi ứng dụng: MoMo (`918751511`), Timo (`1521230347`) và Techcombank Mobile (`1548623362`). Tổng cộng 1.500 review, mỗi ứng dụng 500 ID khác nhau. Đây là phạm vi tìm kiếm, **không phải 1.500 người thuộc mẫu khảo sát**.
- Code quét từ khóa không dấu về chi tiêu, ngân sách, phân loại, lịch sử, báo cáo, hũ chi tiêu và tổng quan; sau đó đọc nội dung ứng viên. Không lọc theo số sao. Review về đăng nhập, hỗ trợ hoặc chuyển tiền chung không tự động được coi là pain ngân sách.
- Ngày cập nhật trong tập RSS tải được: MoMo 12–26/11/2026; Timo 13/08/2025–26/11/2026; Techcombank 10/09/2026–26/11/2026. Chỉ dùng review không muộn hơn 27/11/2026 như kế hoạch gốc.
- MoMo có quá ít nội dung phù hợp trong cửa sổ truy cập, nên tìm thêm Techcombank. Đã chọn **5 ví dụ có nội dung từ Timo và Techcombank**, giữ cả ý kiến tích cực; ID, ngày, sao, trích đoạn nguyên văn và URL trang RSS ở [review-quotes.csv](review-quotes.csv).
- Mỗi trích đoạn tối đa 25 từ; đã đối chiếu nguyên văn với nguồn, bỏ tên tác giả. Không lưu toàn bộ review tải về hay metadata tác giả vào repo.

**Giới hạn:** đây là 5 ví dụ chọn có chủ đích để bổ trợ trích dẫn, chưa phải mẫu 15 review/ứng dụng theo kế hoạch. Chưa tạo `review-sample.csv`, chưa tính tỷ lệ nhãn và chưa có thành viên thứ hai kiểm độc lập 10 review. Không báo phần đào review đã đạt ngưỡng ≥30 hoặc lấy 5 ví dụ này để khẳng định giả thuyết đã đúng.

Các ví dụ hỗ trợ nhu cầu xem tổng quan/tra lịch sử chi tiêu và cho thấy trải nghiệm trái chiều; không trực tiếp xác nhận việc phát hiện vượt ngân sách muộn hoặc mất ≥15 phút rà khoản có thể giảm. Giữ nguyên nhãn và tiêu chí đã đăng ký ở trên.

Để truy lại nguồn: mở URL RSS của từng dòng, tìm `review_id` trong `entry[].id.label`, rồi so `excerpt` với `entry[].content.label` và số sao với `entry[].im:rating.label`. RSS có thể thay đổi theo review mới; lưu ID và ngày để phân biệt nguồn. `review_updated_at` là thời điểm cập nhật công khai của review, không phải timestamp khảo sát.
