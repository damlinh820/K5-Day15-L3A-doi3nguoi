# Tổng hợp bằng chứng pain — Track E2

## Trạng thái cập nhật CP3

Nguồn chính là [Google Form quản lý chi tiêu cá nhân](https://docs.google.com/spreadsheets/d/1PBkJUoWysDsxhcFtNoagPUZxsqZ22c_B3GBI88UffRg/edit?gid=1174331201#gid=1174331201). Bản xuất ngày 28/11/2026 có **31 phản hồi và 31 dấu thời gian khác nhau**. Con số 32 trên trang tính bao gồm một hàng tiêu đề, vì vậy mẫu số dùng trong báo cáo là 31.

| Nguồn | Tiến độ | Trạng thái bằng chứng |
|---|---|---|
| Khảo sát người dùng ví/app ngân hàng | 31 phản hồi, đã tổng hợp và ẩn danh | Đủ ngưỡng số lượng ≥20; kết quả ủng hộ một phần giả thuyết |
| Review công khai ví/app ngân hàng | Chưa thu và mã hóa đủ ≥30 review | Chưa dùng để kết luận |
| Phỏng vấn | Chưa thực hiện | Chưa dùng để kết luận |
| Dữ liệu giao dịch synthetic | 252 giao dịch, seed 42 | Chỉ dùng chạy prototype; không phải bằng chứng pain |

## Cách xử lý

- Mỗi dòng phản hồi được tính một lần; bản xuất có 31 dấu thời gian duy nhất.
- Không lưu timestamp, tên, email hoặc dữ liệu nhận dạng vào repo.
- Câu chọn nhiều được đếm độc lập, vì vậy tổng tỷ lệ trong một câu có thể lớn hơn 100%.
- Giữ cả phản hồi không gặp pain và phản hồi đánh giá thấp cảnh báo minh họa.
- Không coi dữ liệu synthetic trong `data/` là bằng chứng người dùng.

## Đặc điểm mẫu

- 31/31 sử dụng ví điện tử hoặc app ngân hàng ít nhất vài lần mỗi tháng.
- 23/31 sử dụng ít nhất khoảng một lần mỗi ngày.
- 19/31 hiện có đặt ngân sách theo nhóm, thường xuyên hoặc không thường xuyên.
- Nghề nghiệp: 13 học sinh/sinh viên, 8 nhân viên văn phòng, 8 kinh doanh/làm việc tự do và 2 nhóm khác.
- Vì chỉ 8/31 là nhân viên văn phòng, kết quả toàn mẫu không được trình bày như kết quả riêng của persona chính.

## Kết quả chính của toàn mẫu

| Quan sát | Kết quả | Diễn giải |
|---|---:|---|
| Chi vượt mức ít nhất thỉnh thoảng trong 3 tháng gần đây | 27/31 (87,1%) | Vượt mức dự kiến là tình huống phổ biến trong mẫu |
| Nhận ra trước hoặc khi gần chạm giới hạn | 19/31 (61,3%) | Phần lớn không nói rằng họ chỉ phát hiện sau khi đã vượt |
| Nhận ra sau khi vượt, khi gần hết tiền hoặc lúc tổng kết cuối tháng | 9/31 (29,0%) | Tín hiệu gần nhất cho pain phát hiện muộn, nhưng không thay thế câu hỏi hành vi 30 ngày |
| Chọn “quên theo dõi chi tiêu” | 13/31 (41,9%) | Pain theo dõi có tín hiệu rõ |
| Chọn “khó phân loại các khoản giao dịch” | 13/31 (41,9%) | Pain hiểu giao dịch có tín hiệu rõ |
| Chọn “không biết khoản chi nào có thể cắt giảm” | 11/31 (35,5%) | Có nhu cầu hỗ trợ chọn khoản có thể giảm |
| Chọn “phát hiện vượt ngân sách quá muộn” | 6/31 (19,4%) | Có pain nhưng không chiếm đa số toàn mẫu |
| Chọn “cảnh báo chi tiêu chưa đủ thông tin” | 5/31 (16,1%) | Pain về chất lượng cảnh báo còn yếu |
| Phải xem lại giao dịch hoặc rất khó xác định khoản nên cắt | 13/31 (41,9%) | Hỗ trợ gợi ý khoản giảm có căn cứ |
| Muốn thấy số đã chi và ngân sách còn lại trong cảnh báo | 16/31 (51,6%) | Ủng hộ việc để code hiển thị số và tỷ lệ |
| Muốn thấy các giao dịch dẫn đến nguy cơ | 10/31 (32,3%) | Ủng hộ cảnh báo có căn cứ truy ngược |
| Muốn nhận đề xuất khoản có thể cắt giảm | 9/31 (29,0%) | Có nhu cầu, nhưng không phải lựa chọn của đa số |
| Chấm cảnh báo minh họa ở mức 4–5/5 | 19/31 (61,3%) | Mẫu toàn bộ đánh giá ý tưởng tích cực ở mức vừa |
| Rất sẵn sàng hoặc có thể dùng nếu bảo mật | 26/31 (83,9%) | Bảo mật là điều kiện quan trọng, không phải sự chấp nhận vô điều kiện |

## Kiểm tra riêng persona nhân viên văn phòng

- Có 8/31 phản hồi thuộc nhóm nhân viên văn phòng.
- 7/8 chi vượt mức ít nhất thỉnh thoảng.
- 6/8 nhận ra trước hoặc khi gần chạm giới hạn; không ai trong nhóm này chọn trực tiếp “phát hiện vượt ngân sách quá muộn”.
- 3/8 quên theo dõi, 3/8 khó phân loại giao dịch và 2/8 không biết khoản nào có thể cắt giảm.
- 4/8 muốn cảnh báo hiển thị số đã chi và ngân sách còn lại.
- Chỉ 2/8 chấm cảnh báo minh họa ở mức 4/5; không có người chấm 5/5.

Kết quả nhóm nhỏ này không đủ để kết luận persona nhân viên văn phòng thường phát hiện quá muộn. Nó ủng hộ mạnh hơn nhu cầu theo dõi số tiền và phân loại giao dịch.

## Năm ví dụ phản hồi đã ẩn danh

Các dòng dưới đây giữ nguyên lựa chọn của người trả lời ở Q8, Q9 và Q11. Đây là **ví dụ nguyên văn từ lựa chọn trong form**, không phải câu tự luận do người tham gia tự viết.

1. **R06:** “Sau khi đã vượt ngân sách” · “Không biết khoản chi nào có thể cắt giảm, Phát hiện vượt ngân sách quá muộn, Cảnh báo chi tiêu chưa đủ thông tin” · “Rất khó xác định”.
2. **R11:** “Khi tài khoản gần hết tiền” · “Quên theo dõi chi tiêu, Không biết khoản chi nào có thể cắt giảm, Phát hiện vượt ngân sách quá muộn” · “Rất khó xác định”.
3. **R15:** “Khi tổng kết chi tiêu cuối tháng” · “Khó phân loại các khoản giao dịch, Nội dung giao dịch khó hiểu, Không biết khoản chi nào có thể cắt giảm, Chi tiêu qua nhiều ứng dụng, khó tổng hợp”.
4. **R24:** “Trước khi gần chạm giới hạn ngân sách” · “Phát hiện vượt ngân sách quá muộn, Chi tiêu qua nhiều ứng dụng, khó tổng hợp” · “Phải mất thời gian xem lại giao dịch”.
5. **R27:** “Khi tổng kết chi tiêu cuối tháng” · “Quên theo dõi chi tiêu, Nội dung giao dịch khó hiểu, Không biết khoản chi nào có thể cắt giảm, Cảnh báo chi tiêu chưa đủ thông tin, Chi tiêu qua nhiều ứng dụng, khó tổng hợp” · “Rất khó xác định”.

Câu 19 chỉ có các câu ngắn như “Không”, “Ko”, “ko”, “không” và “Có”, nên không đủ nội dung để dùng làm trích dẫn hành vi tự do.

## Đối chiếu giả thuyết đã đăng ký

Giả thuyết yêu cầu trong ≥20 phản hồi phải có ít nhất 8 người kể một trường hợp trong 30 ngày qua phát hiện gần/vượt ngân sách muộn hoặc mất ≥15 phút rà khoản có thể giảm, đồng thời có ≥5 trích dẫn nguyên văn mô tả hành vi thật.

Khảo sát hiện tại dùng mốc **3 tháng**, không hỏi số phút và chủ yếu là câu chọn sẵn. Vì vậy:

- Đã đạt ngưỡng số lượng phản hồi.
- Có tín hiệu pain theo dõi, phân loại và tìm khoản có thể giảm.
- Chưa đo đúng điều kiện “trong 30 ngày” hoặc “mất ≥15 phút”.
- Chưa có 5 câu tự luận mô tả hành vi thật.
- **Chưa được tuyên bố giả thuyết đã đạt toàn bộ ngưỡng đăng ký trước.**

## Kết luận và việc còn thiếu

Kết quả 31 phản hồi ủng hộ việc hiển thị số đã chi/ngân sách, giúp theo dõi và chỉ ra khoản có thể giảm. Tuy nhiên, dữ liệu không chứng minh rằng phát hiện quá muộn là pain chiếm đa số ở persona nhân viên văn phòng. Nhóm giữ lát cắt prototype đã chốt, nhưng phải trình bày kết luận này trung thực.

Để hoàn thiện bằng chứng CP3, cần thực hiện ít nhất một trong hai hướng:

1. Phỏng vấn nhanh ≥3 người đúng persona, hỏi một trường hợp cụ thể trong 30 ngày qua và lấy ≥5 câu nguyên văn có nội dung; hoặc
2. Thu và mã hóa ≥30 review công khai theo `evidence/data-mining.md`, giữ cả review không gặp pain.
