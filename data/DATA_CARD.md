# Data card — Track E2

## Dataset 1 · `transactions.csv`

| | |
|---|---|
| Dùng để làm gì | Tra giao dịch, cộng chi theo nhóm, kiểm ngưỡng và tìm khoản không thiết yếu. |
| Từ đâu | Sinh bằng `data/generate_transactions.py`, seed 42; hoàn toàn synthetic. |
| Xử lý | 3 persona × 3 tháng × 7 nhóm × 4 giao dịch = 252 dòng; mô tả nơi bán có nhiều cách viết; tiền VND nguyên. |
| Số dòng | 252 giao dịch; 84 giao dịch/persona; 7 nhóm chi. |
| Phiên bản | E2 CP2 · 27/11/2026. |
| Nhãn | `synthetic`; `is_essential` xác định trước cho nhà ở, hóa đơn, y tế. |
| Giới hạn | Không phản ánh người thật, không chứng minh pain/tác động, phân phối và ngân sách do nhóm tự dựng. |

## Dataset 2 · `users.json` và `budgets.json`

- U001: sinh viên; U002: nhân viên văn phòng; U003: người lo chi tiêu gia đình.
- Mỗi persona có ngân sách cho `an_uong`, `di_lai`, `mua_sam`, `giai_tri`, `nha_o`, `hoa_don`, `y_te`.
- Ba edge case cố định ở tháng 11: U001 ăn uống chạm 100%; U002 mua sắm vượt 100%; U003 y tế vượt 100% nhưng không được gợi ý cắt nhóm thiết yếu.

## Cấu hình demo · `demo_finance.json`

- Số tiền và ngày nhận thu nhập hàng tháng cùng số dư đầu kỳ của ba tháng là dữ liệu synthetic tự đặt để trình diễn giao diện.
- Chỉ dùng để tính số dư và dự báo trong bản demo local; không dùng làm bằng chứng pain hay số liệu người dùng thật.
- Giao dịch thêm trên giao diện chỉ tồn tại trong phiên trình duyệt và được tính lại ngay, không ghi vào dataset gốc.

## Tái lập và kiểm

```powershell
python data/generate_transactions.py
```

Script ghi lại cả ba file từ seed 42. Nguyễn Nho Trọng cần kiểm tay ba edge case và đếm đủ 252 dòng trước CP3; chưa ghi là đã kiểm độc lập khi việc đó chưa thực hiện.

Không commit sao kê, giao dịch, tên nơi bán, số tài khoản hay dữ liệu cá nhân thật.
