# Tổng hợp bằng chứng pain — EVPromoAI

Ngày truy cập nguồn: **27/11/2026**. Phụ trách: Ngô Văn Tuân; Codex hỗ trợ tìm và tổng hợp. Chưa có phỏng vấn, khảo sát hay review do nhóm thu thập trong lần này.

## 1. Nguồn và trạng thái yêu cầu

| Nguồn | Trạng thái | Hồ sơ |
|---|---|---|
| Tài liệu công khai | Đã đọc 5 tài liệu từ 4 tổ chức, có 5 trích dẫn; là bằng chứng bối cảnh, chưa tự xác nhận đạt ngưỡng pain CP3. | [data-mining.md](data-mining.md), [public-sources.csv](public-sources.csv) |
| Review theo kế hoạch ban đầu | Chưa thu thập bộ ≥30 phản hồi. | Tiêu chí gốc: [hypothesis.md](hypothesis.md). |
| Phỏng vấn ≥3 người ngoài nhóm, đúng vai | Chưa thực hiện; chưa có lịch hẹn xác nhận. | Chỉ ghi người đã thực sự trao đổi, đã ẩn danh. |
| Khảo sát ≥20 người ngoài nhóm, đúng vai | Chưa thực hiện. | Không có số liệu để báo cáo. |

## 2. Số chính

- Tập tài liệu đã chọn: **5 tài liệu**, thuộc **4 tổ chức**; 5 trích dẫn ngắn ở mục 3.
- Có **3/5 tài liệu (60%)** đề cập giới hạn ngân sách; **2/5 (40%)** mô tả vận hành thủ công trước đây. Cách mã hóa và đếm lại ở `data-mining.md`.
- Đây là tỷ lệ tài liệu trong mẫu chọn có chủ đích, không phải tỷ lệ người dùng gặp pain; hai bài của Uber không phải hai người dùng độc lập.
- Chưa có số thật về tần suất pain, thời gian xử lý hay mức thất thoát ngân sách ở người dùng mục tiêu.

## 3. Năm trích dẫn nguyên văn có nguồn

Giữ tiếng Anh để kiểm tra nguyên văn; lược tên tác giả cá nhân, giữ tổ chức và link. Các câu diễn giải bên dưới là nhận định của nhóm, không phải lời người được phỏng vấn.

### S01 — Uber: phân bổ incentive và ngân sách

> Operations teams manually adjusted rewards to meet quarterly limits

[Beyond Prediction: Solving the Multiple Knapsack Problem at Scale: How Uber Optimizes Incentives](https://www.uber.com/us/en/blog/solving-multiple-knapsack/) — 14/05/2026, mục **The Pre-Tarot Landscape: First-In Wins**.

Diễn giải: từng có thao tác điều chỉnh thưởng thủ công. Giới hạn: ví dụ ban đầu chủ yếu về tài xế/courier, ngân sách quý; chưa chứng minh pain voucher hành khách theo ngày.

### S02 — DiDi: coupon trong môi trường gọi xe cạnh tranh

> Evaluating coupon strategies in real time is risky due to potential declines in GMV and order volume.

[Order Acquisition Under Competitive Pressure: A Rapidly Adaptive Reinforcement Learning Approach for Ride-Hailing Subsidy Strategies](https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2025/ads/preprint_ecml_pkdd_2025_ads_1131.pdf) — ECML PKDD 2025 preprint, **trang PDF 3, §1 Introduction**.

Diễn giải: coupon cần được thử thận trọng và có kiểm soát ngân sách. Giới hạn: nhà cung cấp dịch vụ trên nền tảng tổng hợp ở Trung Quốc, không phải dữ liệu nhóm tự đo tại Việt Nam.

### S03 — Booking.com: chi phí của ưu đãi

> a dedicated budget usually limits monetary losses.

[Optimization Levers for Promotions Personalization Under Limited Budget](https://ceur-ws.org/Vol-2959/paper2.pdf) — MORS/RecSys 2021, **trang PDF 1, Abstract**.

Diễn giải: ngân sách là ràng buộc khi cá nhân hóa ưu đãi. Giới hạn: ngành du lịch trực tuyến; chỉ bổ trợ, không thay bằng chứng từ người vận hành gọi xe.

### S04 — Grab: công việc thủ công của đội marketing

> Grab’s marketing team used to stay awake at midnight to manually trigger such campaigns.

[Supporting large campaigns at scale](https://engineering.grab.com/supporting-large-campaigns-at-scale) — 01/04/2022, mục **Introduction**.

Diễn giải: có tiền lệ pain khi vận hành chiến dịch. Giới hạn: lịch sử trước khi có batch job, không chứng minh hiện nay vẫn làm thủ công hoặc chọn sai mức voucher.

### S05 — Uber: tác động khác nhau giữa các nhóm

> treatment that works well for one group of customers may not work well for another group.

[Using Causal Inference to Improve the Uber User Experience](https://www.uber.com/us/en/blog/causal-inference-at-uber/) — 19/06/2019, mục **When treatment effect varies across segments**.

Diễn giải: cần phân biệt hiệu quả tăng thêm giữa các nhóm. Giới hạn: nguyên lý đo tác động, không phải bằng chứng sản phẩm của nhóm đã tăng chuyến hoặc tiết kiệm tiền.

## 4. Kết luận và tác động tới Canvas

Các nguồn hỗ trợ tính hợp lý của bài toán phân bổ ưu đãi có ràng buộc. Chúng chưa xác nhận rằng phát voucher đồng loạt gây trợ giá thừa ở người dùng mục tiêu, cũng chưa chứng minh giải pháp đề xuất tốt hơn luật tĩnh.

**Giả thuyết ban đầu: chưa đủ dữ liệu để kết luận đúng hay sai.** Giữ nguyên tiêu chí trong `hypothesis.md`; không coi 5 tài liệu là 30 review hoặc 3 cuộc phỏng vấn.

Canvas được cập nhật theo hướng một đề xuất cho một yêu cầu báo giá, có kiểm tra ngân sách và biên bằng code. Không lấy nhận xét của hành khách để suy ra khó khăn của quản lý tăng trưởng; không dùng demo trên dữ liệu dựng để tuyên bố hiệu quả kinh doanh.

## 5. Phần Tuân cần xác minh tiếp

Ưu tiên phỏng vấn ≥3 người ngoài nhóm từng trực tiếp vận hành voucher/khuyến mãi. Ghi vai, thời điểm, câu trả lời thật đã ẩn danh và xin phép sử dụng trích dẫn. Người bán hàng chỉ phù hợp nếu thực sự có trách nhiệm phân bổ ngân sách ưu đãi; ghi rõ khác biệt với người dùng mục tiêu gọi xe.

Các câu hỏi gợi ý:

1. Trong chiến dịch gần nhất, anh/chị chọn người nhận và mức ưu đãi như thế nào? Hiện dùng công cụ gì?
2. Bước nào khó nhất, nếu có? Có thể kể một trường hợp cụ thể và cách xử lý không?
3. Trong tháng vừa qua việc đó xảy ra bao nhiêu lần, lần gần nhất mất bao lâu? Có ghi chép đã ẩn danh để đối chiếu không?
4. Anh/chị xác định ưu đãi tạo thêm đơn/chuyến bằng cách nào? Có trường hợp ưu đãi không cần thiết hoặc không gặp khó khăn như giả thuyết không?

Tổng hợp ít nhất 5 trích dẫn thật từ các cuộc trao đổi; báo số người gặp pain dạng x/3 khi n nhỏ, ghi rõ trường hợp không gặp pain. Sau đó cập nhật kết luận và xin Linh chốt Canvas.
