# Tổng hợp bằng chứng pain — Track E2

## Cập nhật CP3 — 28/11/2026

Phụ trách: Ngô Văn Tuân; Codex hỗ trợ tìm nguồn và tổng hợp. Giữ nguyên tiêu chí của giả thuyết gốc và chuẩn đạt sau CP2. Đối tượng hiện tại đã được mở rộng theo Canvas, ghi riêng trong nhật ký thay đổi vì đây là quyết định sau khi đã có dữ liệu.

Link bảng do nhóm cung cấp: [Google Sheets khảo sát](https://docs.google.com/spreadsheets/d/1PBkJUoWysDsxhcFtNoagPUZxsqZ22c_B3GBI88UffRg/edit?gid=1174331201#gid=1174331201). Báo cáo này dùng bản CSV Tuân cung cấp; đã kiểm có 31 dòng dữ liệu và 31 timestamp khác nhau, không nhầm hàng tiêu đề thành phản hồi. Timestamp không lưu vào repo và không chứng minh 31 người độc lập.

### 1. Nguồn hiện có và mức xác minh

| Nguồn | Tiến độ | Giới hạn |
|---|---|---|
| Khảo sát E2 | Đã đọc CSV đầy đủ có **31 phản hồi**, giữ nguyên 24 dòng cũ. Bản đã ẩn danh và cách đếm ở [survey/README.md](survey/README.md). | Có 25 người từ 18 tuổi; **16 người khớp các thông tin đã hỏi của hồ sơ mở rộng**; trong đó 2 người mâu thuẫn ở Q3 nên báo thêm nhóm 14 người. Hồ sơ nhân viên văn phòng gốc vẫn có 3. Chưa xác nhận ngoài nhóm/30 ngày; không coi 31 phản hồi là mẫu đúng persona. |
| Review công khai E2 | Đã đối chiếu 5 trích đoạn từ 5 review App Store Timo/Techcombank, gồm ý kiến tích cực và phàn nàn. | Là ví dụ bổ trợ có chủ đích; chưa đủ mẫu 30 review theo kế hoạch. |
| Phỏng vấn bổ sung | Tuân xác nhận team phỏng vấn **3 người ngoài nhóm sáng 28/11/2026**, được đồng ý dùng nội dung ẩn danh. Có [P1–P3](interviews/README.md), 6 trích đoạn từ bản tóm tắt; 2/3 nêu rà ≥15 phút, giữ P3 không gặp phát hiện muộn. | Đủ số lượng của hướng bằng chứng phỏng vấn ≥3 người ngoài nhóm. Nguồn là **bản tóm tắt**, không nhận 6 đoạn là lời nói nguyên văn; chưa biết trùng người khảo sát, không cộng mẫu. |

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

### 2.1. Các chỉ số bổ sung của nhóm đã đối chiếu CSV

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

Bảng tổng hợp bổ sung: [survey/results-summary.csv](survey/results-summary.csv). Các số trên mô tả toàn bộ 31 phản hồi, gồm cả người dưới 18 tuổi; không thay mẫu số hồ sơ 16/14. Q4 tự báo tần suất dùng app, trong khi Q3 có ba lựa chọn mâu thuẫn đã ghi rõ ở trên. Cảm nhận/ý định sử dụng không phải hiệu quả đã đo.


### 2.2. Đối chiếu nhóm nghề nhân viên văn phòng

- Có 8/31 phản hồi thuộc nhóm nhân viên văn phòng, trong đó 7 người từ 18 tuổi. Đây là nhóm nghề để đối chiếu; đối tượng hiện tại không giới hạn nghề. Hồ sơ gốc có thêm điều kiện đang đặt ngân sách nên chỉ có 3 người.
- 7/8 chi vượt mức ít nhất thỉnh thoảng.
- 6/8 nhận ra trước hoặc khi gần chạm giới hạn; không ai trong nhóm này chọn trực tiếp “phát hiện vượt ngân sách quá muộn”.
- 3/8 quên theo dõi, 3/8 khó phân loại giao dịch và 2/8 không biết khoản nào có thể cắt giảm.
- 4/8 muốn cảnh báo hiển thị số đã chi và ngân sách còn lại.
- Chỉ 2/8 chấm cảnh báo minh họa ở mức 4/5; không có người chấm 5/5.

Kết quả nhóm nhỏ này không đủ để kết luận persona nhân viên văn phòng thường phát hiện quá muộn. Nó ủng hộ mạnh hơn nhu cầu theo dõi số tiền và phân loại giao dịch.

### 2.3. Ví dụ lựa chọn trắc nghiệm đã đối chiếu

Các dòng dưới đây giữ nguyên lựa chọn của người trả lời ở Q8, Q9 và Q11. Đây là **ví dụ nguyên văn từ lựa chọn trong form**, không phải câu tự luận do người tham gia tự viết.

1. **S006:** “Sau khi đã vượt ngân sách” · “Không biết khoản chi nào có thể cắt giảm, Phát hiện vượt ngân sách quá muộn, Cảnh báo chi tiêu chưa đủ thông tin” · “Rất khó xác định”.
2. **S011:** “Khi tài khoản gần hết tiền” · “Quên theo dõi chi tiêu, Không biết khoản chi nào có thể cắt giảm, Phát hiện vượt ngân sách quá muộn” · “Rất khó xác định”.
3. **S015:** “Khi tổng kết chi tiêu cuối tháng” · “Khó phân loại các khoản giao dịch, Nội dung giao dịch khó hiểu, Không biết khoản chi nào có thể cắt giảm, Chi tiêu qua nhiều ứng dụng, khó tổng hợp”.
4. **S024:** “Trước khi gần chạm giới hạn ngân sách” · “Phát hiện vượt ngân sách quá muộn, Chi tiêu qua nhiều ứng dụng, khó tổng hợp” · “Phải mất thời gian xem lại giao dịch”.
5. **S027:** “Khi tổng kết chi tiêu cuối tháng” · “Quên theo dõi chi tiêu, Nội dung giao dịch khó hiểu, Không biết khoản chi nào có thể cắt giảm, Cảnh báo chi tiêu chưa đủ thông tin, Chi tiêu qua nhiều ứng dụng, khó tổng hợp” · “Rất khó xác định”.

Câu 19 chỉ có các câu ngắn như “Không”, “Ko”, “ko”, “không” và “Có”, nên không đủ nội dung để dùng làm trích dẫn hành vi tự do.

Mã Sxxx khớp thứ tự dòng của `survey/responses-anonymized.csv`. Các lựa chọn có sẵn này giúp truy vết tình huống; không được tính thành năm lời kể tự do hoặc cuộc phỏng vấn để xác nhận giả thuyết.


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

### 3.1. Ghi chép phỏng vấn do Tuân bổ sung

Nguồn nhận ngày 28/11/2026: `khaosat.txt`, không có tên/liên hệ người tham gia. Tuân xác nhận team thực hiện phỏng vấn sáng cùng ngày, cả ba ngoài nhóm và đã đồng ý dùng nội dung ẩn danh. Bản trong repo chỉ giữ vai, tuổi từ 18 và nội dung cần phân tích; lược số tiền cụ thể, không đưa file gốc lên Git. Sáu đoạn ở [interviews/quotes.csv](interviews/quotes.csv) khớp **bản tóm tắt của team**, không phải lời nói nguyên văn. Nguyên văn trực tiếp từ nguồn công khai vẫn là 5 review ở mục 3.

| Mã | Vai theo nguồn | Trường hợp gần nhất | Phút rà tự báo | Lần/tháng tự báo | Ước lượng tải rà/tháng |
|---|---|---|---|---|---|
| [P1](interviews/P1.md) | Sinh viên, từ 18 tuổi; MoMo/MB Bank | Khoảng tuần trước, nhóm ăn uống gần hết ngân sách | Khoảng 15 | Khoảng 3 | 45 phút |
| [P2](interviews/P2.md) | Nhân viên văn phòng, từ 18 tuổi; Techcombank/ZaloPay | Khoảng 5 ngày trước, mua sắm đã vượt ngân sách | Khoảng 20–25 | Khoảng 2 | 40–50 phút |
| [P3](interviews/P3.md) | Nhân viên kinh doanh, từ 18 tuổi; Vietcombank/MoMo | Hôm kia, kiểm tra định kỳ, chưa vượt | Khoảng 5–10 | Khoảng 4 | 20–40 phút |

Theo mô tả, cả ba phù hợp hồ sơ mở rộng; chỉ P2 phù hợp điều kiện nghề nghiệp gốc. **2/3 người theo bản tóm tắt nêu một lần rà ≥15 phút trong 30 ngày qua**. Giữ P3 làm trường hợp không xác nhận pain phát hiện muộn hoặc mất ≥15 phút. Không dùng tỷ lệ % cho mẫu nhỏ, không gộp thành 34 người hay cộng vào nhóm 16/14 vì chưa biết có trùng người khảo sát hay không.

Thời điểm tương đối được tính theo sáng phỏng vấn 28/11/2026 đã được xác nhận; không tự bịa ngày sự kiện chính xác. Tải rà là tần suất × thời gian một lần tự báo, không phải tổng thời gian cả tháng đã đo, cũng không phải số phút prototype tiết kiệm.

### 4. Đối chiếu giả thuyết và impact

Ngưỡng giữ nguyên theo [hypothesis.md](hypothesis.md): ≥20 phản hồi hợp lệ, ít nhất 8 người kể trường hợp trong 30 ngày qua phát hiện gần/vượt ngân sách muộn **hoặc** mất ≥15 phút rà khoản có thể giảm, cùng ≥5 trích dẫn nguyên văn về hành vi thật.

**Kết luận hiện tại: chưa đủ dữ liệu để xác nhận đạt ngưỡng pain.** Hồ sơ gốc vẫn có 3 người; hồ sơ mở rộng có 16 người khớp các thông tin đã hỏi, hoặc 14 nếu kiểm thêm mâu thuẫn Q3; đều chưa đủ 20 và chưa xác minh ngoài nhóm. Form không hỏi trường hợp cụ thể trong 30 ngày hoặc thời gian rà ≥15 phút, nên không thể tính đúng hợp số người thỏa giả thuyết. Q7 dùng mốc ba tháng, Q8 hỏi thói quen và Q11 không hỏi số phút; 8/16 quên theo dõi không phải 8 trường hợp thỏa điều kiện gốc. Năm review bổ trợ không trực tiếp xác nhận ngưỡng kể trên. Việc mở rộng đối tượng được ghi sau khi đã thu dữ liệu, không thay kết quả kiểm chứng của giả thuyết ban đầu.

Nguồn phỏng vấn bổ sung đã được Tuân xác nhận và **đủ số lượng 3 người ngoài nhóm theo hướng phỏng vấn của bài**; cùng 5 review công khai nguyên văn được lưu riêng. Ba cặp tần suất/thời gian tự báo cho tải rà ước lượng 20–50 phút/người/tháng. Không lấy 2/3 trường hợp để thay điều kiện ≥20 người, ≥8 trường hợp của giả thuyết khảo sát gốc. Không nhận 6 đoạn từ bản tóm tắt là ≥5 lời nói nguyên văn của người tham gia.

Đã thay giả định 60 phút/người/tháng không có nguồn bằng bảng tải công việc có ghi rõ nguồn tự báo trong `spec.md` §2; **lợi ích tiết kiệm do prototype vẫn chưa được đo**. Không lấy mức thích cảnh báo minh họa, thời gian app tải chậm hoặc dữ liệu synthetic làm lợi ích thật. Không kết luận giả thuyết sai chỉ vì form chưa đo được các điều kiện cần kiểm chứng.

### 5. Phần cần bổ sung để chốt bàn giao

1. Đã làm: đọc file đầy đủ ngoài repo, xuất bản đã ẩn danh, đếm đủ 31 dòng, giữ đối chiếu mốc 22/24, đồng bộ đối tượng hiện tại và báo riêng hồ sơ gốc/mở rộng.
2. Tuân kiểm lại sáu dòng đã gắn cờ, ưu tiên S025/S028 về sử dụng app; xác nhận kênh tuyển người ngoài nhóm và điều kiện sử dụng lời kể công khai. Không tự coi các trường chưa hỏi là đã được đáp ứng.
3. Đã bổ sung nguồn phỏng vấn 3 người ngoài nhóm sáng 28/11/2026 theo xác nhận của Tuân, có đồng thuận dùng bản tóm tắt ẩn danh. Giữ trạng thái nguồn riêng và giới hạn khảo sát; nếu cần trích trực tiếp lời nói phải có lời nguyên văn từ người tham gia hoặc bản ghi được phép dùng.
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
