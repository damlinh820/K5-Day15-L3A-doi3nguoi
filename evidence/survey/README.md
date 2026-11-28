# Khảo sát E2 — kết quả từ bản CSV nhận ngày 28/11/2026

## Nguồn, cách làm sạch và tái lập

CSV đầy đủ mới do Tuân cung cấp có **31 phản hồi, 19 câu hỏi và một cột timestamp**, tăng 7 phản hồi so với bản 24 trước đó. Đã so nội dung Q1–Q19 và xác nhận 24 dòng cũ giữ nguyên trong phần đầu bản mới. Bản gốc giữ ngoài repo; SHA-256 của đúng bản xuất mới ghi trong [analysis.json](analysis.json). Chưa có bản CSV riêng tại mốc 22 phản hồi.

Đối tượng hiện tại theo Canvas: **người từ 18 tuổi dùng ví/app ngân hàng, có đặt ngân sách theo nhóm chi và cần theo dõi để tránh vượt ngân sách**. Nhóm nghề không còn là điều kiện của phân tích mở rộng. Đây là thay đổi sau khi đã có dữ liệu, ghi ở spec §10 và phần bổ sung trong `evidence/hypothesis.md`; vẫn giữ nhóm nhân viên văn phòng gốc để đối chiếu, không tuyên bố các kết quả mở rộng là kiểm định đã đăng ký trước.

Chạy từ gốc repo, Python standard library, không gọi model hoặc gửi dữ liệu ra ngoài:

```powershell
python evidence/survey/analyze.py --input 'C:\duong-dan-ngoai-repo\survey.csv'
```

Script tạo:

- [responses-anonymized.csv](responses-anonymized.csv): giữ đủ 31 dòng S001–S031; bỏ timestamp, gộp tuổi thành `18_plus`/`under_18`, chuẩn hóa nhóm nghề và trạng thái ngân sách. Bổ sung lựa chọn ứng dụng Q3 để kiểm tra điều kiện người dùng ví/app; giữ cờ hồ sơ mới, cờ hồ sơ cũ và cờ mâu thuẫn riêng. Không lưu nội dung tự do Q19 hoặc các trường không dùng trong phân tích này.
- [metrics.csv](metrics.csv): sáu chỉ số theo tám nhóm, có tử số và mẫu số riêng.
- [questions-actual.csv](questions-actual.csv): nguyên câu hỏi thực tế Q1–Q19, không chứa câu trả lời.
- [analysis.json](analysis.json): cỡ mẫu, kiểm tra trùng câu trả lời, cờ chất lượng và giới hạn đo lường; không chứa đường dẫn file cá nhân.

[results-summary.csv](results-summary.csv) là bảng 18 chỉ số toàn mẫu do nhóm bổ sung từ bản 31 phản hồi, đã được đối chiếu lại với CSV gốc khi tích hợp. Đây là bảng snapshot của nhóm, không do `analyze.py` sinh; nếu thay bản khảo sát cần kiểm lại bảng này. Kết quả theo hồ sơ mở rộng/gốc dùng `metrics.csv`, không suy ra từ phần trăm toàn mẫu.

S001 là dòng dữ liệu đầu tiên sau header, tương tự đến S031; mã S001–S024 giữ nguyên vì câu trả lời cũ không đổi thứ tự. Thành viên có CSV gốc có thể truy lại từng dòng. Không lưu tên, email, timestamp, số tài khoản hoặc nội dung giao dịch thật. Khoảng trắng và dấu phẩy thừa trong lựa chọn được chuẩn hóa; câu checkbox được tách theo **toàn bộ nhãn đã biết**, không cắt nhãn chứa dấu phẩy thành nhiều đáp án. Nhãn lạ khiến script dừng trước khi xuất để tránh vô tình công khai nội dung ngoài danh sách.

## Mẫu số và điều kiện đúng đối tượng

| Nhóm | N | Ý nghĩa |
|---|---|---|
| `all_received` | 31 | Toàn bộ bản xuất mới; dùng mô tả tập trả lời nhận được, không gọi là 31 phản hồi đúng persona. |
| `first_22_comparison` | 22 | 22 dòng đầu theo thứ tự CSV, chỉ để đối chiếu các số trong bản plan cũ. Không khẳng định đây là snapshot lịch sử độc lập. |
| `first_24_comparison` | 24 | Giữ kết quả toàn mẫu của bản xuất trước để so tiến độ, không dùng thay kết quả 31 dòng hiện tại. |
| `adults_only` | 25 | Từ 18 tuổi; 6 phản hồi dưới 18 tuổi vẫn được giữ trong dữ liệu/toàn mẫu. |
| `adult_office` | 7 | Từ 18 tuổi, tự khai nghề nhân viên văn phòng. |
| `original_target_profile` | 3 | Hồ sơ gốc: người lớn, dùng app, nhân viên văn phòng và đang đặt ngân sách. |
| `target_profile` | 16 | Hồ sơ mở rộng: người lớn, Q3 có chọn ví/app và Q5 đang đặt ngân sách thường xuyên hoặc không thường xuyên, không giới hạn nghề. |
| `target_profile_consistent_app` | 14 | Trong 16 trường hợp trên, bỏ riêng hai trường hợp Q3 vừa chọn ứng dụng vừa chọn không sử dụng; đây là phân tích đối chiếu, không xóa hai dòng khỏi dữ liệu. |

Q3 được tách theo nhãn đầy đủ, bao gồm cả lựa chọn ngân hàng có dấu phẩy trong tên. `target_profile_match` là cờ hồ sơ mở rộng; `original_target_profile_match` giữ định nghĩa gốc. `consistent_app_profile_match` chỉ kiểm thêm mâu thuẫn sử dụng app, không có nghĩa đã xác minh tất cả điều kiện.

Form không hỏi người trả lời có thuộc nhóm dự án hay không, không hỏi rõ ngân sách/theo dõi trong **30 ngày qua**, cũng không xác nhận trực tiếp nhu cầu theo dõi của từng người. Vì vậy 16/14 trường hợp chỉ khớp các thông tin có thể đọc từ CSV. Cả hai nhóm đều chưa đủ 20; không gọi 25 người lớn hoặc toàn bộ 31 phản hồi là ≥20 người đúng persona.

## Sáu chỉ số kiểm lại

Năm chỉ số đầu đếm đúng lựa chọn tương ứng ở **Q9**; chỉ số cuối đếm Q16 bằng 4 hoặc 5. Một người có thể chọn nhiều khó khăn, không cộng các tử số.

| Chỉ số | 22 dòng đầu, đối chiếu plan cũ | Toàn bộ bản mới | Hồ sơ mở rộng | Hồ sơ mở rộng, không mâu thuẫn Q3 |
|---|---|---|---|---|
| Quên theo dõi chi tiêu | 11/22 | 13/31 | 8/16 | 8/14 |
| Khó phân loại các khoản giao dịch | 8/22 | 13/31 | 5/16 | 4/14 |
| Không biết khoản chi nào có thể cắt giảm | 7/22 | 11/31 | 6/16 | 5/14 |
| Cảnh báo chi tiêu chưa đủ thông tin | 4/22 | 5/31 | 2/16 | 2/14 |
| Phát hiện vượt ngân sách quá muộn | 3/22 | 6/31 | 3/16 | 3/14 |
| Cảnh báo minh họa được đánh giá 4–5 | 14/22 | 19/31 | 9/16 | 9/14 |

Cả sáu số của plan cũ khớp 22 dòng đầu. Toàn mẫu của bản 24 phản hồi trước có các tử số lần lượt 12, 9, 7, 4, 4, 16; vẫn tái lập ở `first_24_comparison`. Nhóm hồ sơ gốc trên bản mới vẫn là 3 người với các tử số 2, 1, 1, 0, 0, 0. Không gộp các nhóm hoặc bỏ dòng để ép kết quả về mốc cũ.

Q8 hỏi thời điểm thường nhận ra vượt ngân sách, có 5/31 chọn sau khi đã vượt; Q9 có 6/31 chọn khó khăn phát hiện muộn. Hai câu hỏi khác nhau, giữ riêng. Điểm thích minh họa Q16 không phải pain đã quan sát, ý định sử dụng thực tế hoặc hiệu quả tiết kiệm tiền/thời gian. Tương tự, 8/16 quên theo dõi không phải 8 lời kể đáp ứng giả thuyết.

## Chất lượng và giới hạn

- Q3: S025, S028, S029 vừa chọn ứng dụng vừa chọn không sử dụng. Trong đó S025/S028 thuộc hồ sơ mở rộng; S029 dưới 18 tuổi. Giữ đủ cả ba dòng và báo riêng nhóm 14 người không mâu thuẫn ở Q3.
- Q6: S012, S015, S025 đồng thời chọn không theo dõi và một cách theo dõi. Q9: S022 đồng thời chọn không gặp khó khăn đáng kể và khó phân loại. Chỉ gắn cờ, không tự sửa/xóa; nhóm không mâu thuẫn Q3 vẫn có thể còn các cờ này.
- Không có hai dòng trùng toàn bộ Q1–Q19 sau khi bỏ timestamp. Điều này không chứng minh 31 người độc lập vì khảo sát không có cách xác minh danh tính/thành viên nhóm.
- Q19 có 26 ô trống và 5 câu chỉ là Có/Không/Ko; **không có câu tự do đủ nội dung để làm trích dẫn hành vi**. Không viết lại các lựa chọn trắc nghiệm thành lời phỏng vấn.
- Form thực tế **khác bản soạn 10 câu trong repo**: không hỏi đồng thuận trích dẫn công khai, không lấy trường hợp cụ thể trong 30 ngày và không hỏi thời gian rà giao dịch có ≥15 phút hay không. Không suy ra các điều này từ Q7 về ba tháng, Q8 về thói quen hoặc Q11 chỉ nói mất thời gian.
- Ngưỡng và hồ sơ gốc trong `evidence/hypothesis.md` giữ nguyên; chỉ bổ sung nhật ký về hồ sơ mở rộng. Bản khảo sát này chưa đủ dữ liệu để kiểm tra trọn ngưỡng, kể cả sau khi mở rộng; không kết luận giả thuyết sai hoặc đã được xác nhận.
- Chưa đo tần suất công việc/tháng và số phút có thể tiết kiệm. Impact 60 phút/người/tháng trong spec vẫn là tự ước tính.

## Bàn giao cho Tuân/Linh

Tuân kiểm lại các dòng đã gắn cờ và xác nhận kênh tuyển người ngoài nhóm. Muốn kiểm chứng ngưỡng đã đăng ký cần bổ sung đúng người dùng, trường hợp cụ thể trong 30 ngày và thời gian rà chi tiêu; xin đồng thuận trước khi dùng lời kể nguyên văn. Năm review công khai ở `evidence/review-quotes.csv` là nguồn bổ trợ, không thay việc xác minh mẫu hoặc điều kiện của giả thuyết.

Cập nhật bổ sung: đã có nguồn [phỏng vấn 3 người ngoài nhóm](../interviews/README.md) sáng 28/11/2026 được Tuân xác nhận. Đây là bản tóm tắt do team thực hiện, không sửa các câu trả lời CSV hoặc nhận sáu trích đoạn tóm tắt là lời nói nguyên văn. Giữ kết luận giới hạn khảo sát và các cỡ mẫu nguyên trạng.
