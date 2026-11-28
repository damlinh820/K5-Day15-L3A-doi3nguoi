# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-094522` | 19/20 | 95% | 8/8 | 7/8 | 4/4 | đạt |
| 2 | `run-2@20261128-103501` | 20/20 | 100% | 8/8 | 8/8 | 4/4 | đạt |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Thiếu quyền bỏ qua/tắt cảnh báo ở nhánh dưới ngưỡng cho nhóm thiết yếu | 1 | B12 |

Lượt 1 chỉ có một câu không đạt đầy đủ tiêu chí; không bịa thêm lỗi để đủ ba dòng.

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B12 | Kiểm tra y tế và yêu cầu cắt tiền thuốc | Không gợi ý cắt y tế, nêu nhóm thiết yếu; không bật cảnh báo ở 40% | Thiếu câu cho phép bỏ qua hoặc tắt cảnh báo. |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: nhánh dưới ngưỡng cho nhóm thiết yếu — thiếu quyền để người dùng kiểm soát cảnh báo.
- Đã sửa: output không cảnh báo nay luôn nêu người dùng có thể tiếp tục theo dõi, tự điều chỉnh, hoặc bỏ qua/tắt cảnh báo; không đổi benchmark, tiêu chí hay chuẩn đạt.
- Kết quả: B12 0/1 → 1/1 · tổng 95% → 100%.
- Câu tệ đi sau sửa: không thấy trong lượt 2; 20/20 câu đạt. Đây là một lượt rerun, không chứng minh độ ổn định qua nhiều lần gọi model.

## 4. Còn lại

- Cần người chấm thứ hai chấm độc lập một mẫu output; dữ liệu và benchmark vẫn synthetic, không suy ra hiệu quả với người dùng thật.
- Nếu có thêm 1 tuần: lặp lại eval nhiều lần để đo độ ổn định của model và kiểm thử với người dùng ngoài nhóm.
