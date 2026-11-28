# Kế hoạch thực hiện Checkpoint 3

## 1. Mục tiêu CP3

Nhóm cần hoàn thành các đầu ra sau:

1. Bằng chứng pain đạt ngưỡng ở ít nhất một nguồn và có tối thiểu 5 trích dẫn hoặc ví dụ nguyên văn.
2. Bộ câu thử có 20–30 câu, trong đó có ít nhất 5 câu `kho` và 2 câu `tu_choi`.
3. Bản chạy thử gọi model thật và video minh họa khoảng 30 giây.
4. Kết quả đánh giá lượt 1 dạng `x/N` kèm run ID.
5. `spec.md` hoàn thiện từ §0 đến §7.
6. Khai thật những phần chưa hoàn thành, nếu có.

## 2. Phân công chi tiết

### 2.1. Đàm Tuấn Linh — Model thật, tích hợp và nộp CP3

#### Công việc

- Kết nối model thật theo `docs/connect-model.md`.
- Đặt API key trong `.env`; không commit `.env` hoặc API key.
- Kiểm tra `codebase/ai.py` trả đúng các trường:
  - `text`;
  - `model`;
  - `tokens_in`;
  - `tokens_out`.
- Chạy thử:

```bash
python run.py
python run.py eval --try
```

- Xác nhận:
  - model không còn là `fake`;
  - token vào và token ra lớn hơn 0;
  - số tiền, ngân sách và tỷ lệ vẫn do code/công cụ tính;
  - model không tự tính lại ngân sách hoặc tự thực hiện giao dịch.
- Rà soát `spec.md` §3–§6:
  - kiến trúc;
  - công cụ;
  - ranh giới giữa code và model;
  - điểm người dùng duyệt;
  - biện pháp an toàn.
- Tổng hợp các đường dẫn cần nộp CP3.
- Kiểm tra repo công khai bằng cửa sổ ẩn danh.
- Chạy kiểm tra cuối trước khi nộp:

```bash
python run.py check
git status
```

#### Đầu ra bàn giao

- Model thật hoạt động trong workflow.
- `eval --try` chạy thành công và có token thật.
- `spec.md` §3–§6 hoàn thiện.
- Câu trả lời form CP3 và danh sách link nộp.

#### Điều kiện hoàn thành

- Luồng không lỗi từ đầu vào đến cảnh báo cuối.
- Không có API key hoặc dữ liệu cá nhân trong Git.
- Repo và các link nộp mở được khi không đăng nhập.

---

### 2.2. Ngô Văn Tuân — Bằng chứng pain và impact

#### Công việc

- Làm sạch bản đầy đủ 31 phản hồi khảo sát, giữ nguyên 24 dòng của bản trước:
  - loại dữ liệu nhận dạng;
  - không đưa email và timestamp lên Git;
  - giữ cả phản hồi không gặp pain;
  - báo toàn mẫu dạng `x/31`; báo riêng nhóm hồ sơ mở rộng `x/16` và nhóm không mâu thuẫn sử dụng app `x/14`, không tráo mẫu số.
- Tổng hợp các số liệu đã đếm lại từ bản đầy đủ:
  - 13/31 người quên theo dõi chi tiêu;
  - 13/31 người khó phân loại giao dịch;
  - 11/31 người không biết khoản nào có thể cắt giảm;
  - 5/31 người cho rằng cảnh báo hiện tại chưa đủ thông tin;
  - 6/31 người chọn khó khăn phát hiện vượt ngân sách quá muộn ở Q9;
  - 19/31 người đánh giá cảnh báo minh họa ở mức 4–5; không dùng điểm thích minh họa làm bằng chứng pain hoặc hiệu quả thật.
- Đồng bộ đối tượng theo Canvas: người từ 18 tuổi dùng ví/app, có đặt ngân sách theo nhóm và cần theo dõi; không giới hạn nghề. Hồ sơ gốc nhân viên văn phòng vẫn có 3 người, giữ để đối chiếu. Số liệu 22 dòng đầu của bản plan cũ được lưu trong `evidence/survey/README.md`; không sửa giả thuyết gốc hoặc chuẩn đạt.
- Kiểm lại các phản hồi có cờ chất lượng, ưu tiên S025/S028 về sử dụng app; chưa tự coi 16 hoặc 14 người là đã được xác minh ngoài nhóm.
- Đã có 5 trích đoạn review công khai có nguồn tại `evidence/review-quotes.csv`. Kiểm lại và bổ sung lời kể hành vi thật bằng một trong hai cách:
  - phỏng vấn nhanh ít nhất 3 người; hoặc
  - đào review công khai theo `evidence/data-mining.md`.
- Không biến lựa chọn trắc nghiệm thành lời trích dẫn do người dùng tự nói.
- Ẩn tên và thông tin nhận dạng trong mọi trích dẫn.
- Đối chiếu kết quả với ngưỡng đã đăng ký trong `evidence/hypothesis.md`.
- Nếu chưa đạt ngưỡng, ghi đúng kết quả và hạn chế; không đổi ngưỡng sau khi đã có dữ liệu.
- Cập nhật:
  - `evidence/summary.md`;
  - `canvas.md` dòng bằng chứng;
  - `spec.md` §0–§2;
  - kết quả khảo sát đã ẩn danh trong `evidence/survey/`.

#### Đầu ra bàn giao

- Một nguồn bằng chứng pain được tổng hợp theo đúng ngưỡng đã đăng ký.
- Tối thiểu 5 trích dẫn hoặc ví dụ nguyên văn đã ẩn danh.
- `evidence/summary.md` có phương pháp, cỡ mẫu, `x/N`, kết luận và hạn chế.
- `spec.md` §0–§2 sử dụng số liệu thật thay cho trạng thái “chưa có phản hồi”.

#### Điều kiện hoàn thành

- Mọi số liệu truy ngược được về nguồn.
- Không bịa người tham gia, câu trả lời, review hoặc trích dẫn.
- Không commit dữ liệu cá nhân hay toàn bộ bản phản hồi thô.

---

### 2.3. Nguyễn Nho Trọng — Bộ câu thử và kết quả lượt 1

#### Công việc

- Rà lại `eval/benchmark.csv`:
  - tổng số câu nằm trong khoảng 20–30;
  - hiện có 8 câu thường, 8 câu khó và 4 câu từ chối;
  - không có ô bắt buộc bị trống;
  - các mã nguồn có thể truy ngược.
- Không được:
  - xoá câu thử trượt;
  - sửa `expected` để khớp output;
  - sửa chuẩn đạt trong `spec.md` §7;
  - sửa `eval/metric_spec.yaml` sau CP2.
- Chỉ gắn nguồn `nguoi_dung:` cho tình huống thực sự rút ra từ khảo sát, phỏng vấn hoặc review.
- Sau khi Linh nối model thật, chạy:

```bash
python run.py check
python run.py eval --try
python run.py eval
```

- Mở `eval/run-1.csv` và chấm từng câu:
  - `pass = 1` nếu đạt toàn bộ tiêu chí;
  - `pass = 0` nếu thiếu bất kỳ tiêu chí bắt buộc nào;
  - ghi lý do cụ thể trong `ghi_chu`.
- Chạy lệnh tính điểm:

```bash
python run.py score eval/run-1.csv
```

- Ghi lại:
  - run ID;
  - tổng số câu đạt `x/20`;
  - tỷ lệ đạt theo `thuong`, `kho`, `tu_choi`;
  - lỗi nổi bật;
  - tên model;
  - số lần gọi model, công cụ và token.
- Chỉ sửa code khi phát hiện lỗi triển khai thật; giữ nguyên bộ câu thử và chuẩn đạt.

#### Đầu ra bàn giao

- `eval/run-1.csv` được chấm đủ.
- `traces/run-1.jsonl` của đúng lượt chạy.
- Kết quả `x/20` và run ID để điền form CP3.
- Kết quả `python run.py check` không còn cảnh báo quan trọng.

#### Điều kiện hoàn thành

- Không còn ô `pass` chưa điền trong lượt 1.
- Kết quả được tính bằng `python run.py score`, không tính tay thay cho khung.
- Giữ lại toàn bộ câu trượt và ghi đúng nguyên nhân.

---

### 2.4. Trường — Tài liệu, video và kiểm thử bàn giao

#### Thông tin thành viên

- Họ và tên: cần bổ sung họ tên đầy đủ trong `TEAMS.md`.
- Mã học viên: `2A202603378`.
- Vai trò dự kiến: tài liệu CP3, kiểm thử bàn giao và video demo.

#### Công việc

- Thêm dòng thành viên số 4 vào `TEAMS.md`:

```markdown
| 4 | [Họ tên đầy đủ của Trường] | 2A202603378 | Thành viên | Tài liệu CP3, kiểm thử bàn giao và video demo |
```

- Cập nhật tên và phần việc trong:
  - `canvas.md` dòng 7;
  - `spec.md` §10.
- Kiểm tra `spec.md` có đủ §0–§7 và nội dung thống nhất với code.
- Chuẩn bị kịch bản và quay video khoảng 30 giây, thể hiện:
  1. chạy `python run.py`;
  2. nhập một mã giao dịch synthetic;
  3. hệ thống tạo cảnh báo;
  4. output hiển thị tên model thật;
  5. có số lần gọi model, công cụ và token.
- Không quay `.env`, API key, email hoặc dữ liệu cá nhân.
- Đăng video bằng một trong hai cách:
  - YouTube ở chế độ “Không công khai”; hoặc
  - Google Drive ở chế độ “Bất kỳ ai có đường liên kết”.
- Mở thử link video bằng cửa sổ ẩn danh.
- Chạy mô phỏng thử để chuẩn bị CP4:

```bash
python run.py simulate --try
```

- Rà checklist CP3 và báo rõ từng mục đạt/chưa đạt trước khi đội trưởng nộp.

#### Đầu ra bàn giao

- `TEAMS.md`, `canvas.md` và `spec.md` có đủ 4 thành viên.
- Link video khoảng 30 giây mở được khi không đăng nhập.
- Checklist CP3 dạng đạt/chưa đạt.
- Kết quả mô phỏng thử 10 phiên để chuẩn bị CP4.

#### Điều kiện hoàn thành

- Video cho thấy model thật, không phải chế độ `fake`.
- Video không làm lộ dữ liệu bí mật.
- Link chia sẻ được kiểm tra ở chế độ ẩn danh.

## 3. Thứ tự phối hợp

### Giai đoạn 1 — Làm song song

1. Tuân xử lý bằng chứng khảo sát và thu đủ 5 trích dẫn nguyên văn.
2. Linh nối model thật và chạy `eval --try`.
3. Trọng rà benchmark, metric và các điều kiện chấm.
4. Trường cập nhật thông tin thành viên, chuẩn bị kịch bản video và checklist.

### Giai đoạn 2 — Tích hợp

1. Linh xác nhận model thật hoạt động và token lớn hơn 0.
2. Tuân chốt `evidence/summary.md`, `canvas.md` và `spec.md` §0–§2.
3. Trọng chạy lượt đánh giá chính thức, chấm `run-1.csv` và tính điểm.
4. Linh cập nhật kết quả lượt 1 vào `spec.md` mà không sửa chuẩn đạt.
5. Trường quay video trên đúng phiên bản code đã dùng để chạy lượt 1.

### Giai đoạn 3 — Kiểm tra và nộp

1. Trường kiểm tra link video bằng cửa sổ ẩn danh.
2. Linh chạy `python run.py check`.
3. Cả bốn người kiểm tra phần có tên mình và xác nhận có thể giải thích được.
4. Linh kiểm tra `git status`, commit, push và mở repo công khai.
5. Linh nộp CP3 bằng mã học viên của đội trưởng.

## 4. Checklist trước khi nộp CP3

- [ ] `TEAMS.md` có đủ 4 thành viên và đúng format.
- [ ] Đã bổ sung họ tên đầy đủ của Trường, MSSV `2A202603378`.
- [ ] `evidence/summary.md` có nguồn pain đạt ngưỡng.
- [x] Có 5 trích đoạn review công khai nguyên văn đã ẩn danh; việc đạt ngưỡng pain vẫn cần đánh giá riêng.
- [x] Số liệu khảo sát được báo dạng `x/31`, kèm nhóm hồ sơ mở rộng `x/16` và nhóm không mâu thuẫn Q3 `x/14`.
- [ ] `eval/benchmark.csv` có 20–30 câu.
- [ ] Có ít nhất 5 câu `kho` và 2 câu `tu_choi`.
- [ ] Chuẩn đạt trong `spec.md` §7 không bị thay đổi sau CP2.
- [ ] `spec.md` hoàn thiện từ §0 đến §7.
- [ ] `python run.py check` chạy đạt.
- [ ] `python run.py eval --try` gọi model thật và có token lớn hơn 0.
- [ ] Đã chạy lượt đánh giá chính thức.
- [ ] `eval/run-1.csv` được chấm đủ cột `pass` và `ghi_chu`.
- [ ] Có kết quả lượt 1 dạng `x/N` và run ID.
- [ ] Video khoảng 30 giây thể hiện bản chạy thử gọi model thật.
- [ ] Link video mở được bằng cửa sổ ẩn danh.
- [ ] Repo công khai và mở được bằng cửa sổ ẩn danh.
- [ ] Không có `.env`, API key hoặc dữ liệu cá nhân trong Git.
- [ ] Đã ghi rõ những phần chưa hoàn thành, nếu có.

## 5. Điểm nghẽn cần ưu tiên

1. Khảo sát đầy đủ có 31 phản hồi nhưng chỉ 16 người khớp các trường hồ sơ mở rộng, hoặc 14 nếu kiểm thêm mâu thuẫn Q3; chưa xác minh ngoài nhóm và chưa đo trường hợp trong 30 ngày/thời gian rà ≥15 phút. Đã có 5 review bổ trợ, nhưng chưa đủ mẫu review 30 theo kế hoạch và Q19 khảo sát không có lời kể có nội dung. Tuân ưu tiên xác minh, bổ sung đúng người và trường hợp thực tế; không đổi ngưỡng để kết luận đạt.
2. Không chạy lượt đánh giá chính thức trước khi Linh xác nhận model thật và token lớn hơn 0.
3. Không quay video khi hệ thống vẫn hiển thị model `fake`.
4. Chưa được thêm Trường vào `TEAMS.md` cho đến khi có họ tên đầy đủ để tránh sai thông tin thành viên.
