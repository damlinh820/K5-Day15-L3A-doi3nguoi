# Tóm tắt mô phỏng simulate-1@20261128-104044

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 24 | 1 | 193 | 142 | 0.6 | 3.5 |
| dung_vua | 18 | 3 | 559 | 401 | 1.7 | 10.1 |
| dung_nhieu | 8 | 5 | 1002 | 712 | 3.0 | 16.9 |

Tỉ lệ đạt dùng để tính: 20/20 (100%) — lượt run-2@20261128-103501

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (100 người) | Chi phí / tháng — cơ sở (500 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00050 | $0.00050 | $0.00021 | $0.4592 | $2.30 | $4.59 | $0.0046 |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0018 | $0.0018 | $0.00077 | $1.67 | $8.33 | $16.66 | $0.0167 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (2.4) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-nano. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
