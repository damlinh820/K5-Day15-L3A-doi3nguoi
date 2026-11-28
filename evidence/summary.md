# Tổng hợp bằng chứng pain — Track E2

## Cập nhật CP3 — 28/11/2026

Phụ trách: Ngô Văn Tuân; Codex hỗ trợ tìm nguồn và tổng hợp. Giữ nguyên tiêu chí của giả thuyết gốc và chuẩn đạt sau CP2. Đối tượng hiện tại đã được mở rộng theo Canvas, ghi riêng trong nhật ký thay đổi vì đây là quyết định sau khi đã có dữ liệu.

### 1. Nguồn hiện có và mức xác minh

| Nguồn | Tiến độ | Giới hạn |
|---|---|---|
| Khảo sát E2 | Đã đọc CSV đầy đủ có **31 phản hồi**, giữ nguyên 24 dòng cũ. Bản đã ẩn danh và cách đếm ở [survey/README.md](survey/README.md). | Có 25 người từ 18 tuổi; **16 người khớp các thông tin đã hỏi của hồ sơ mở rộng**; trong đó 2 người mâu thuẫn ở Q3 nên báo thêm nhóm 14 người. Hồ sơ nhân viên văn phòng gốc vẫn có 3. Chưa xác nhận ngoài nhóm/30 ngày; không coi 31 phản hồi là mẫu đúng persona. |
| Review công khai E2 | Đã đối chiếu 5 trích đoạn từ 5 review App Store Timo/Techcombank, gồm ý kiến tích cực và phàn nàn. | Là ví dụ bổ trợ có chủ đích; chưa đủ mẫu 30 review theo kế hoạch. |
| Phỏng vấn | Chưa có biên bản để kiểm tra. | Không tạo người hoặc lời phỏng vấn giả. |

### 2. Số liệu đã đếm lại từ CSV

Nguồn: [survey/responses-anonymized.csv](survey/responses-anonymized.csv), cách đếm tái lập bằng [survey/analyze.py](survey/analyze.py), bảng máy đọc ở [survey/metrics.csv](survey/metrics.csv). Năm khó khăn đếm lựa chọn Q9; điểm minh họa đếm Q16 = 4 hoặc 5. Dùng N = 31 khi mô tả toàn bộ file mới; dùng 16 hoặc 14 cho từng nhóm mở rộng, không tráo mẫu số. Nhóm 16 khớp tuổi, có chọn ví/app và đang đặt ngân sách; nhóm 14 kiểm thêm không mâu thuẫn ở Q3, chưa có nghĩa đã xác minh mọi điều kiện.

| Nội dung | Toàn bộ file mới | Hồ sơ mở rộng | Hồ sơ mở rộng không mâu thuẫn Q3 |
|---|---|---|---|
| Quên theo dõi chi tiêu | 13/31 | 8/16 | 8/14 |
| Khó phân loại giao dịch | 13/31 | 5/16 | 4/14 |
| Không biết khoản nào có thể cắt giảm | 11/31 | 6/16 | 5/14 |
| Cảnh báo hiện tại chưa đủ thông tin | 5/31 | 2/16 | 2/14 |
| Phát hiện vượt ngân sách quá muộn | 6/31 | 3/16 | 3/14 |
| Đánh giá cảnh báo minh họa mức 4–5 | 19/31 | 9/16 | 9/14 |

Các lựa chọn có thể trùng người, không cộng các tử số. Giữ đủ 31 dòng, kể cả người không gặp pain, dưới 18 tuổi và câu trả lời có cờ chất lượng; các nhóm riêng chỉ phục vụ phân tích. Các số của bản plan cũ 11/22, 8/22, 7/22, 4/22, 3/22, 14/22 vẫn khớp 22 dòng đầu. Bản 24 phản hồi cũ có các tử số 12, 9, 7, 4, 4, 16; giữ phần đối chiếu trong `metrics.csv` và `survey/README.md`, không dùng làm kết quả hiện tại. Điểm đánh giá minh họa không chứng minh pain hay hiệu quả thực tế.

S025/S028/S029 vừa chọn có ứng dụng vừa chọn không sử dụng; S025/S028 thuộc nhóm 16, cần hỏi lại nên có nhóm đối chiếu 14. S012/S015/S025 có lựa chọn cách theo dõi mâu thuẫn; S022 vừa chọn không gặp khó khăn vừa chọn khó phân loại. Đã gắn cờ, không tự sửa/xóa. Q19 có 26 ô trống và 5 câu Có/Không/Ko, **không có lời kể tự do đủ nội dung** để trích dẫn hành vi. Bộ thực tế 19 câu khác bản thiết kế 10 câu trong repo; xem [survey/questions-actual.csv](survey/questions-actual.csv).

### 3. Năm trích đoạn nguyên văn công khai đã ẩn danh

Nguyên văn chỉ lưu một lần tại [review-quotes.csv](review-quotes.csv), cột `excerpt`; không có tên người viết. Các mô tả trong bảng dưới là diễn giải của nhóm, không phải lời phỏng vấn.

| Mã | Nguồn / ngày cập nhật / sao | Nội dung quan sát | Giới hạn diễn giải |
|---|---|---|---|
| R01 | Techcombank · 23/11/2026 · 1 sao | Người viết phản ánh mất biểu đồ thu chi tháng. | Không biết người đó có đặt ngân sách hay phát hiện vượt muộn không. |
| R02 | Techcombank · 04/11/2026 · 2 sao | Người viết không thấy tổng quan chi tiêu tháng. | Không suy ra tần suất hoặc số tiền bị ảnh hưởng. |
| R03 | Techcombank · 09/10/2026 · 5 sao | Người viết thấy giao diện thuận tiện để theo dõi và quản lý chi tiêu. | Giữ ý kiến tích cực; không phải bằng chứng gặp pain. |
| R04 | Timo · 19/11/2026 · 2 sao | Người viết tự báo chờ 5 phút để xem lịch sử giao dịch. | Chờ tải lịch sử không đồng nghĩa mất ≥15 phút rà khoản có thể giảm. |
| R05 | Timo · 09/09/2026 · 5 sao | Người viết đề nghị thêm tổng chi theo ngày trong lịch sử. | Là yêu cầu tính năng, chưa chứng minh đã vượt ngân sách muộn. |

URL RSS và review ID từng trường hợp nằm trong CSV. Cách tìm và giới hạn mẫu ghi ở [data-mining.md](data-mining.md). Chưa có thành viên thứ hai kiểm tra độc lập.

### 4. Đối chiếu giả thuyết và impact

Ngưỡng giữ nguyên theo [hypothesis.md](hypothesis.md): ≥20 phản hồi hợp lệ, ít nhất 8 người kể trường hợp trong 30 ngày qua phát hiện gần/vượt ngân sách muộn **hoặc** mất ≥15 phút rà khoản có thể giảm, cùng ≥5 trích dẫn nguyên văn về hành vi thật.

**Kết luận hiện tại: chưa đủ dữ liệu để xác nhận đạt ngưỡng pain.** Hồ sơ gốc vẫn có 3 người; hồ sơ mở rộng có 16 người khớp các thông tin đã hỏi, hoặc 14 nếu kiểm thêm mâu thuẫn Q3; đều chưa đủ 20 và chưa xác minh ngoài nhóm. Form không hỏi trường hợp cụ thể trong 30 ngày hoặc thời gian rà ≥15 phút, nên không thể tính đúng hợp số người thỏa giả thuyết. Q7 dùng mốc ba tháng, Q8 hỏi thói quen và Q11 không hỏi số phút; 8/16 quên theo dõi không phải 8 trường hợp thỏa điều kiện gốc. Năm review bổ trợ không trực tiếp xác nhận ngưỡng kể trên. Việc mở rộng đối tượng được ghi sau khi đã thu dữ liệu, không thay kết quả kiểm chứng của giả thuyết ban đầu.

Chưa có số thật về tần suất công việc và thời gian có thể tiết kiệm để thay giả định impact 60 phút/người/tháng trong `spec.md` §2. Không lấy mức thích cảnh báo minh họa, thời gian app tải chậm hay dữ liệu synthetic làm lợi ích đã đo của sản phẩm. Không kết luận giả thuyết sai chỉ vì form chưa đo được các điều kiện cần kiểm chứng.

### 5. Phần cần bổ sung để chốt bàn giao

1. Đã làm: đọc file đầy đủ ngoài repo, xuất bản đã ẩn danh, đếm đủ 31 dòng, giữ đối chiếu mốc 22/24, đồng bộ đối tượng hiện tại và báo riêng hồ sơ gốc/mở rộng.
2. Tuân kiểm lại sáu dòng đã gắn cờ, ưu tiên S025/S028 về sử dụng app; xác nhận kênh tuyển người ngoài nhóm và điều kiện sử dụng lời kể công khai. Không tự coi các trường chưa hỏi là đã được đáp ứng.
3. Bổ sung đúng người dùng và câu hỏi về trường hợp trong 30 ngày, thời gian rà chi tiêu; giữ nguyên ngưỡng gốc, không đổi persona sau khi thấy dữ liệu để đủ mẫu.
4. Tuân kiểm lại 5 nguồn review; nguồn bổ sung không thay được ngưỡng khảo sát. Nếu tiếp tục đào mẫu 30 review, giữ cách chọn mẫu/nhãn gốc và nhờ thành viên thứ hai kiểm độc lập.

## Hồ sơ tại CP2 — giữ để phân biệt tiến độ

| Nguồn | Tiến độ | Có được tính là bằng chứng đạt ngưỡng chưa? |
|---|---|---|
| Google Form người dùng ví/app ngân hàng | Đã soạn nội dung và script tạo form; chưa tạo/publish, chưa có phản hồi | Chưa |
| Review công khai ví/app ngân hàng | Đã đăng ký cách chọn mẫu và nhãn; chưa thu ≥30 review | Chưa |
| Phỏng vấn | Chưa thực hiện | Chưa |
| 5 tài liệu về voucher gọi xe trước khi đổi hướng | Đã loại vì không thuộc E2 | Không |

### Số chính và kết luận tại CP2

- Số phản hồi khảo sát hợp lệ ghi nhận trong hồ sơ CP2: **0**.
- Số review E2 đã mã hóa tại CP2: **0**.
- Số trích dẫn người dùng E2 tại CP2: **0**.
- **Kết luận:** chưa đủ dữ liệu để kết luận giả thuyết đúng hoặc sai. Dữ liệu synthetic trong `data/` chỉ dùng chạy prototype, không phải bằng chứng pain.

### Kế hoạch đã ghi tại CP2

1. Tạo và duyệt Google Form từ `survey/create-form.gs`, mở thử bằng cửa sổ ẩn danh.
2. Thu ≥20 phản hồi hợp lệ từ người ngoài nhóm dùng ví/app ngân hàng và từng theo dõi ngân sách trong 30 ngày qua.
3. Xuất bản đã ẩn danh, giữ cả câu không gặp pain; báo `x/N`, không tự sửa câu trả lời.
4. Chọn tổng ≥5 trích dẫn nguyên văn có nội dung, bỏ thông tin nhận diện.
5. Đào review theo `data-mining.md` để kiểm tra chéo; nếu hai nguồn lệch nhau, giải thích thay vì chọn số thuận lợi.
