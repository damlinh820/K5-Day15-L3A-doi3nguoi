# Hồ sơ đánh giá — Track E2

## 1. Dataset

252 giao dịch synthetic, 3 persona, 3 tháng, 7 nhóm chi và ngân sách theo nhóm. Dữ liệu sinh bằng seed 42; không phải bằng chứng pain.

## 2. Bộ câu thử

- 20 câu: `thuong` 8 · `kho` 8 · `tu_choi` 4.
- Nguồn: `sinh_seed` 14 · `tu_viet` 6 · `nguoi_dung/data_that` 0. CP2 đủ số câu; trước CP3 phải bổ sung ≥1/3 câu từ khảo sát/review thật mà không sửa các câu/kết quả đã chạy.
- Phủ: trên/dưới ngưỡng, đúng tháng/ngày, thiếu/sai mã, nhóm thiết yếu, giọng phán xét, chuyển tiền, đầu tư và bí mật tài chính.

## 3. Metric

| Metric | Cách chấm | Ngưỡng |
|---|---|---|
| `task_success_rate` | người | ≥80% toàn bộ câu |
| `alert_and_number_accuracy` | code | 100% số và cảnh báo đúng |
| `safety_and_refusal` | người | 100% từ chối; 0 lần cắt thiết yếu |

- Người thứ hai chấm thử 5 output: chưa thực hiện; ghi kết quả thật trước CP3, cần khớp ≥4/5.
- Chuẩn đạt chép nguyên từ `spec.md` §7 và không sửa sau CP2.

## 4. Lệnh

`python run.py check` · `python run.py eval --try` · `python run.py eval`.

## 5. Lượt chạy

Chưa chạy model thật tại CP2; không có kết quả để báo %. Lượt AI giả chỉ dùng kiểm luồng, không tính lượt đánh giá.
