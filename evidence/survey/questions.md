# Khảo sát cách lựa chọn voucher cho dịch vụ gọi xe

Phụ trách: Ngô Văn Tuân · Nhóm EVPromoAI · Bản soạn ngày 27/11/2026.

## 1. Tạo form

Đã có nội dung và script, chưa tạo form trong tài khoản Google hoặc phát khảo sát. Phiên làm việc hiện chưa có công cụ kết nối tạo Google Form trực tiếp; các kết nối khác có thể được tìm trong [plugin directory](https://chatgpt.com/plugins).

1. Mở [Google Apps Script](https://script.google.com/home/start), tạo project mới.
2. Chép toàn bộ file [create-form.gs](create-form.gs) vào `Code.gs`, lưu.
3. Chọn hàm `createSurveyForm` rồi bấm **Run**. Script cần bạn cấp quyền Google Forms để tạo form trong tài khoản của bạn.
4. Mở link chỉnh sửa được in trong **Execution log**. Form được tạo ở trạng thái **chưa publish**, để Tuân và Linh đọc lại.
5. Sau khi duyệt, publish form; kiểm tra quyền trả lời và mở link người trả lời bằng Tab Ẩn Danh trước khi gửi. Không chia sẻ link chỉnh sửa.

Script dùng [FormApp.create(title, isPublished)](https://developers.google.com/apps-script/reference/forms/form-app#create(String,Boolean)) để tạo bản nháp và [page navigation](https://developers.google.com/apps-script/reference/forms/multiple-choice-item#createChoice(String,PageBreakItem)) để kết thúc sớm khi không đồng ý hoặc ngoài đối tượng. Chạy lại trong cùng Apps Script project sẽ trả lại form đã tạo, không thêm câu hỏi lần nữa.

## 2. Nội dung người trả lời nhìn thấy

**Tiêu đề:** Khảo sát cách lựa chọn voucher cho dịch vụ gọi xe

**Mô tả:**

> Nhóm EVPromoAI đang tìm hiểu cách người phụ trách khuyến mãi lựa chọn mức voucher và người nhận cho dịch vụ gọi xe. Khảo sát hỏi về công việc đã thực hiện trong 30 ngày gần nhất; không có câu trả lời đúng hoặc sai. Mỗi người vui lòng trả lời một lần theo trải nghiệm thật.
>
> Form không yêu cầu tên, email, số điện thoại hay tên công ty. Vui lòng không nhập thông tin nhận diện cá nhân, thông tin khách hàng hoặc số liệu nội bộ bí mật. Nhóm sử dụng câu trả lời để tổng hợp bài học và có thể trích dẫn đoạn đã ẩn danh trong repo bài tập công khai. Bạn có thể dừng bằng cách đóng form trước khi gửi.

## 3. Mười câu hỏi và điều hướng

### Q1. Bạn có đồng ý tham gia và cho phép nhóm sử dụng câu trả lời đã ẩn danh để tổng hợp, trích dẫn trong bài tập công khai không?

- Kiểu: chọn một, bắt buộc.
- **Đồng ý** → trang sàng lọc Q2.
- **Không đồng ý** → kết thúc, không hiện câu hỏi về công việc.

### Q2. Trong 30 ngày qua, vai trò nào mô tả đúng công việc của bạn nhất?

- Kiểu: chọn một, bắt buộc; không có lựa chọn tự điền ở câu điều hướng.
- **Quản lý tăng trưởng/marketing: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe** → Q3–Q10.
- **Phụ trách vận hành: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe** → Q3–Q10.
- **Phụ trách kinh doanh/chính sách: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe** → Q3–Q10.
- **Chỉ triển khai mã hoặc quảng cáo theo quyết định của người khác** → kết thúc.
- **Chọn/duyệt voucher cho ngành khác, không phải dịch vụ gọi xe** → kết thúc.
- **Chỉ sử dụng voucher với tư cách khách hàng** → kết thúc.
- **Là thành viên nhóm EVPromoAI** → kết thúc.
- **Không thuộc các vai trò trên hoặc chưa làm công việc này trong 30 ngày qua** → kết thúc.

Hướng dẫn: nếu là thành viên EVPromoAI, chọn đáp án đó dù đồng thời có vai trò nghề nghiệp khác. Chỉ tính đúng đối tượng khi trực tiếp quyết định hoặc duyệt voucher cho dịch vụ gọi xe.

### Q3. Trong 30 ngày qua, bạn đã lựa chọn hoặc duyệt mức voucher và người nhận bao nhiêu lần?

- Kiểu: câu trả lời ngắn, bắt buộc, số nguyên không âm.
- Hướng dẫn: tính mỗi lần ra quyết định hoặc duyệt là một lần, không tính theo số voucher phát ra; có thể ước lượng và dùng cùng cách đếm.

### Q4. Ở lần gần nhất, bạn đã dựa vào những cách nào để lựa chọn voucher?

- Kiểu: checkbox, bắt buộc, cho phép chọn nhiều và thêm lựa chọn khác.
- Excel/Google Sheets hoặc tính toán thủ công.
- Quy tắc cố định hoặc phân nhóm khách hàng có sẵn.
- Báo cáo lịch sử đặt chuyến và sử dụng ưu đãi.
- Kết quả A/B test hoặc thử nghiệm có nhóm đối chứng.
- Công cụ tự động đề xuất/tối ưu mức voucher.
- Kinh nghiệm cá nhân hoặc trao đổi với đồng nghiệp.
- Không rõ/không nhớ.
- Khác: tự điền.

### Q5. Ở lần gần nhất, từ khi bắt đầu xem dữ liệu đến khi chốt quyết định voucher, bạn mất khoảng bao lâu?

- Kiểu: chọn một, bắt buộc.
- Dưới 5 phút.
- Từ 5 đến dưới 15 phút.
- Từ 15 đến dưới 30 phút.
- Từ 30 đến 60 phút.
- Trên 60 phút.
- Không nhớ/không đo được.

### Q6. Kết quả công việc ở lần gần nhất là gì?

- Kiểu: chọn một, bắt buộc.
- Đã chốt được mức voucher và người nhận.
- Chỉ chốt được một phần, còn phải bổ sung hoặc kiểm tra.
- Chưa chốt được.
- Đã dừng vì không cần tiếp tục.
- Không nhớ.

### Q7. Điều gì gây khó khăn nhất trong lần đó, nếu có?

- Kiểu: đoạn văn, bắt buộc.
- Hướng dẫn: mô tả theo trải nghiệm thực tế. Nếu không gặp khó khăn, có thể ghi “Không gặp khó khăn” và điều giúp công việc thuận lợi. Không nêu tên người, công ty hoặc khách hàng.

### Q8. Trong 30 ngày qua, mỗi tình huống sau đã xảy ra bao nhiêu lần khi bạn làm công việc này?

- Kiểu: lưới chọn một đáp án mỗi hàng, bắt buộc.
- Các hàng:
  - Khó xác định ưu đãi có tạo thêm chuyến so với không ưu đãi hay không.
  - Phải điều chỉnh voucher vì giới hạn ngân sách hoặc biên lợi nhuận.
  - Khó giải thích lý do chọn mức voucher hoặc nhóm người nhận.
- Các cột: **0 lần · 1 lần · 2–3 lần · 4–5 lần · Từ 6 lần · Không rõ/không theo dõi**.
- Hướng dẫn: một lần ra quyết định có thể gặp nhiều tình huống. Chọn 0 nếu không xảy ra; không rõ thì chọn “Không rõ/không theo dõi”.

### Q9. Bạn có thể kể một trường hợp cụ thể trong 30 ngày qua, cách đã xử lý và kết quả không?

- Kiểu: đoạn văn, bắt buộc.
- Hướng dẫn: có thể kể trường hợp gặp hoặc không gặp trở ngại. Chỉ nêu điều đã quan sát; nếu nói về thời gian/chi phí thì phân biệt số ghi nhận và số tự ước lượng. Có thể ghi “Không có trường hợp để chia sẻ”; không cung cấp dữ liệu bí mật hoặc nhận diện cá nhân.

### Q10. Ở lần gần nhất, bạn đã kiểm tra hiệu quả tăng thêm của voucher bằng cách nào?

- Kiểu: chọn một, bắt buộc, có lựa chọn khác.
- So sánh với nhóm không nhận ưu đãi trong thử nghiệm có kiểm soát.
- So sánh số chuyến/doanh thu trước và sau chiến dịch.
- Theo dõi số lượt sử dụng voucher.
- Dựa vào kinh nghiệm hoặc phản hồi của đội vận hành.
- Chưa đánh giá hiệu quả tăng thêm.
- Không rõ/không nhớ.
- Khác: tự điền.

Thông báo sau khi gửi: **Cảm ơn bạn đã chia sẻ trải nghiệm. Nhóm EVPromoAI sẽ tổng hợp các câu trả lời đã ẩn danh cho bài tập.**

## 4. Quy tắc tổng hợp trước khi mở form

- Mẫu số N: phản hồi Q1 đồng ý, Q2 thuộc một trong ba vai trực tiếp quyết định/duyệt voucher gọi xe và Q3 từ 1 trở lên. Ghi riêng phản hồi sàng lọc không đạt, thiếu dữ liệu hoặc mâu thuẫn; không tự sửa câu trả lời để đủ điều kiện.
- Ngưỡng khảo sát của bài: **≥20 người ngoài nhóm, đúng đối tượng**. Ghi kênh mời và nhắc mỗi người trả lời một lần; form ẩn danh không tự xác minh được từng người độc lập.
- Báo số hoàn thành từng trạng thái ở Q6 dạng x/N. Với từng hàng Q8, báo số chọn từ 1 lần trở lên / số trả lời biết tần suất của hàng đó; ghi thêm số “Không rõ”. Các hàng có thể trùng sự kiện nên không cộng thành tổng số lần pain.
- Q3 là tần suất công việc; Q8 là tần suất tình huống khó. Không coi hai số là một. Q5 là khoảng thời gian, không tự thay khoảng bằng số phút chính xác.
- Q8 chỉ là trải nghiệm tự báo cáo. Chưa đủ căn cứ khẳng định đã thất thoát tiền hoặc ưu đãi đã tạo thêm chuyến; Q10 giúp mô tả cách người trả lời đang đo hiệu quả.
- Chọn ≥5 đoạn nguyên văn có nội dung từ Q7/Q9, gắn mã S001, S002…; giữ cả câu trái giả thuyết, ẩn chi tiết nhận diện. Không đổi câu trả lời thành lời phỏng vấn.
- Bản khảo sát này là nguồn bổ sung; giữ nguyên giả thuyết và tiêu chí gốc ở `evidence/hypothesis.md`, không dùng ngưỡng khảo sát mới để sửa kết luận cho thuận lợi.
- Chỉ đưa bản xuất đã ẩn danh và tổng hợp vào repo. Chưa có phản hồi thì ghi chưa thu thập, không tạo số liệu kết quả.

## 5. Log triển khai

| Mục | Trạng thái |
|---|---|
| Link chỉnh sửa | Chưa tạo; giữ nội bộ nhóm sau khi chạy script. |
| Link người trả lời | Chưa tạo/publish. |
| Kênh dự kiến | Người phụ trách growth/marketing/vận hành khuyến mãi gọi xe; chưa gửi lời mời. |
| Kênh thực tế đã gửi | Chưa gửi. |
| Giờ mở / giờ chốt (UTC+7) | Chưa mở / chưa chốt. |
| Số phản hồi hợp lệ | Chưa thu thập. |
