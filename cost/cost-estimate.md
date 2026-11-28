# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): `dung_it` 50% · 2 phiên/tháng · 1 lượt/phiên; `dung_vua` 30% · 6 phiên/tháng · 3 lượt/phiên; `dung_nhieu` 20% · 15 phiên/tháng · 5 lượt/phiên. Tất cả là *(tự ước tính)* vì chưa có dữ liệu tần suất thực.
- **Số người dùng** 3 kịch bản: thấp 100 · cơ sở 500 · cao 1.000. Nguồn: *(tự ước tính)* cho phân tích độ nhạy; không phải quy mô thị trường đo được.
- **Giá**: `gpt-5.4-nano` $0,20 input / $1,25 output trên 1M token; `gpt-5.4-mini` $0,75 / $4,50. Nguồn: OpenAI, xem 28/11/2026, ghi rõ trong `cost/personas.yaml`.
- **Tỉ lệ đạt** dùng để tính: 20/20 (100%) — `run-2@20261128-103501`.
- Đo token trên `gpt-5.4-nano`; tính giá cho `gpt-5.4-nano` và kịch bản thay thế `gpt-5.4-mini`.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · Run ID `simulate-1@20261128-104044` · 50 phiên · seed 42 · 0/50 phiên lỗi.

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| `gpt-5.4-nano` | $0,00050 | $0,00050 | $0,4592 | $2,30 | $4,59 | $0,0046 |
| `gpt-5.4-mini` *(giá thay thế; token đo trên nano)* | $0,0018 | $0,0018 | $1,67 | $8,33 | $16,66 | $0,0167 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact tiết kiệm do sản phẩm (`spec.md` §2): **chưa đo**. Bản tóm tắt phỏng vấn P1–P3 được Tuân xác nhận cho phép ước lượng tải rà 20–50 phút/người/tháng từ tần suất × thời gian tự báo. Không coi toàn bộ tải này là thời gian AI tiết kiệm.
- Chi phí / người / tháng (cơ sở, `gpt-5.4-nano`): $0,0046 theo giả định persona và quy mô nêu trên.
- **Kết luận một dòng — đáng làm không:** chi phí model mô phỏng thấp, nhưng chưa thể kết luận giá trị sản phẩm vì lợi ích tiết kiệm và tần suất phiên cảnh báo chưa được đo; số lần người dùng tự rà chi tiêu không thay trực tiếp các giả định mô phỏng.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
