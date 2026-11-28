# EVPromoAI — Cảnh báo sắp vượt ngân sách

**Thành viên, lớp, track:** xem [TEAMS.md](TEAMS.md). **Điền TEAMS.md đúng format**: khi chấm và đánh giá, BTC quét file này để ghép điểm cho từng người.

*Lát cắt = phần nhỏ nhất làm xong được trong hackathon: một người dùng · một việc · một quyết định AI · một kết quả.*

---

## Bài toán CP1

**Track E — E2.** Người dùng ví điện tử hoặc app ngân hàng đang cố giữ chi tiêu theo nhóm trong ngân sách nhưng thường nhận ra quá muộn và khó tìm khoản có thể giảm mà không ảnh hưởng nhu cầu thiết yếu.

**Lát cắt.** Khi một giao dịch synthetic làm nhóm chi chạm 80% ngân sách, code bật cảnh báo và lọc khoản không thiết yếu; AI gợi ý 2–3 khoản có thể giảm, còn người dùng làm theo, bỏ qua hoặc tắt cảnh báo.

Chi tiết Canvas CP1: [canvas.md](canvas.md). Giả thuyết bằng chứng: [evidence/hypothesis.md](evidence/hypothesis.md).

---

---

## Nhóm làm gì, khung làm gì

| Nhóm quyết định và viết | Khung làm sẵn (không cần sửa) |
|---|---|
| Người dùng, pain, bằng chứng, impact (`evidence/`, `spec.md` §1–§2) | — |
| Hình dạng giải pháp, công cụ, prompt, luồng (`spec.md` §4, `codebase/agent.py`, `tools.py`, `ai.py`) | Ghi mọi lần gọi model / công cụ vào trace, cộng token (`codebase/tracing.py`) |
| Bộ câu thử, metric, chuẩn "đạt" (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `spec.md` §7) | Kiểm đủ cột, đủ câu `kho` / `tu_choi`, đủ ≥1/3 câu từ người dùng / data thật (`run.py check`) |
| Chấm cột `pass` theo metric spec | Chạy cả bộ một lệnh, có run ID, model, token từng câu (`run.py eval`) · tính % đạt (`run.py score`) |
| Persona, số người dùng thật, giá model (`cost/personas.yaml`) | Sinh ~50 phiên, chạy thật qua bản chạy thử, tính chi phí / phiên, / task thành công, / tháng 3 kịch bản (`run.py simulate`) |

*Ví dụ track A (ví dụ cỡ, không phải lời giải):* nhóm viết công cụ `search_lesson` tra bài pre-class đã đánh mã đoạn, luồng "tra đoạn → model trả lời kèm mã đoạn, không có thì nói không có", metric "mọi khẳng định có mã đoạn đúng", persona "ôn dồn trước kiểm tra". Khung chạy 25 câu thử ra `run-1.csv`, nhóm chấm `pass`, `score` in % đạt; `simulate` chạy 50 phiên ra chi phí / task thành công cho hai model.

## Chạy trong 3 phút

### Giao diện demo dạng điện thoại

Chạy `python codebase/demo_server.py` (Windows có thể dùng `py codebase/demo_server.py`), rồi mở **http://127.0.0.1:8765** trên máy đó. Dừng server bằng `Ctrl+C`. Giao diện chỉ lắng nghe trên máy local; không đưa API key ra trình duyệt. Cấu hình model trong `.env` theo [hướng dẫn kết nối](docs/connect-model.md).

Chọn một trong ba tình huống từ dữ liệu tổng hợp, xem các giao dịch liên quan và nhấn **Phân tích chi tiêu**. Cảnh báo được tính theo ngân sách của nhóm chi đến ngày giao dịch đang xét; chỉ tình huống đạt ngưỡng mới gọi model để gợi ý. Mục **Hỏi thêm** dùng model để trả lời theo đúng giao dịch và trạng thái ngân sách đang chọn. Nhãn kết quả cho biết model được gọi hay không; nếu cấu hình `fake`, mục hỏi đáp sẽ yêu cầu cấu hình model thật. Nút bỏ qua chỉ ẩn kết quả trên giao diện, không thay đổi dữ liệu hay cài đặt cảnh báo.

Thanh công cụ dưới màn hình chia demo thành ba mục: **Trang chủ** để xem dự báo ngân sách và hỏi chatbot, **Thu chi** để nhập giao dịch mới, và **Thông báo** để phân loại các khoản chưa có nhãn. Chuông hiển thị số giao dịch đang chờ. Giao dịch mới và ngân sách chỉnh trên giao diện chỉ tồn tại đến khi dừng server; ngày nhận thu nhập, thu nhập tháng và số dư đầu kỳ là giả định synthetic trong `data/demo_finance.json`.

Khi nhập thu chi, để **Tự nhận diện** để hệ thống đối chiếu các cụm từ rõ nghĩa với nhóm (không gọi model). Nội dung không khớp hoặc khớp nhiều nhóm sẽ chờ xác nhận ở chuông; nếu người dùng chọn nhóm thủ công, lựa chọn đó được ưu tiên. Danh sách cụm từ chỉ là quy tắc demo và không nhận diện được mọi nội dung giao dịch.

Các nhóm trả nợ, cho vay và tiết kiệm mặc định chưa có ngân sách; chọn **Chỉnh sửa** để đặt mức phù hợp. Thu nhập và chi tiêu chưa có nhãn đều xuất hiện ở chuông, kể cả sau khi tải lại trang trong cùng phiên server. Dữ liệu demo không đồng bộ ngân hàng và không lưu lâu dài.

Ba kịch bản dùng cùng persona U001 và tháng 09/2026: ngày 05 nhận lương, ngày 14 nhóm đi lại chạm 80%, ngày 30 nhóm giải trí vượt ngân sách. Chọn một nhóm ở Trang chủ để xem biểu đồ tròn, sửa trần, hỏi chatbot theo nhóm và xem lịch sử đến ngày đang xem. Ngân sách nhập chỉ nằm trong trang hiện tại và sẽ trở lại mặc định nếu tải lại trang. Giao dịch mới cập nhật số dư, số đã chi và số còn lại; mức ngân sách do người dùng đặt không tự thay đổi.

Nhóm **Tiết kiệm** được trình bày theo mục tiêu, không coi khoản gửi là chi tiêu: tiền ra gắn nhãn này là gửi tiết kiệm, tiền vào là rút tiết kiệm; số đã tiết kiệm ròng trong tháng bằng tiền gửi trừ tiền rút. Số dư là tiền còn sử dụng, vì vậy vẫn giảm khi gửi và tăng khi rút. Đây là mô phỏng theo tháng, không phải số dư tài khoản tiết kiệm tích lũy thực tế.

Trang chủ có biểu đồ cơ cấu tiền ra theo nhóm đến ngày đang xem, kể cả khoản chưa phân loại; biểu đồ không gồm tiền gửi tiết kiệm và không cộng tiền vào. Nhóm **Khác** dùng cho thu hoặc chi phát sinh, không đặt mức trần; xem chi tiết để phân biệt tổng tiền vào và tiền ra.

Nhóm **Nhà ở** được dành cố định toàn bộ hạn mức mỗi tháng, nên thanh phân bổ luôn hiện 100% khi đã đặt mức. Đây là số đã phân bổ, không mặc định coi là đã thanh toán: chi tiết vẫn hiển thị tổng tiền đã trả theo giao dịch; số dư và biểu đồ tiền ra chỉ tính những giao dịch đã có. Có thể đổi mức cố định trong chi tiết nhóm.

Khi nhóm đang phân tích đã vượt hạn mức, giao diện có thể đề xuất chuyển phần ngân sách chưa dùng từ các nhóm không thiết yếu để bù. Các số tiền trong phương án do quy tắc xác định tính, không được trích từ văn bản model; nếu nguồn bù không đủ, ứng dụng ghi rõ phần còn thiếu. Người dùng chọn đồng ý, từ chối hoặc điều chỉnh số tiền chuyển trước khi áp dụng. Tổng hạn mức không thay đổi; giao dịch và số dư thực tế không bị sửa.

Bộ khung cần **Python 3.10 trở lên** (Python 3.9 có sẵn trên macOS vẫn chạy được, chỉ in một dòng nhắc). **Không cần `pip install`.**

**Bước 1 — Mở cửa sổ lệnh ngay trong thư mục repo**

| Windows (PowerShell) | macOS |
|---|---|
| Mở thư mục repo bằng File Explorer → bấm vào thanh địa chỉ → gõ `powershell` → Enter | Mở **Terminal** (Cmd + Space, gõ "Terminal") → gõ `cd ` (có dấu cách) → kéo thả thư mục repo vào → Enter |

Gõ `dir` (Windows) hoặc `ls` (macOS / Linux): thấy `run.py` và `README.md` là đang đứng đúng chỗ.

**Bước 2 — Kiểm Python và chạy thử**

| Việc | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Kiểm Python | `python --version` (không được thì `py --version`) | `python3 --version` |
| Chạy bản chạy thử (chế độ giả, chưa gọi model) | `python run.py` | `python3 run.py` |
| Kiểm bộ câu thử | `python run.py check` | `python3 run.py check` |
| Tạo file `.env` để nối model | `copy .env.example .env` | `cp .env.example .env` |

- Windows: gõ `python` mà mở Microsoft Store hoặc báo không có lệnh → dùng `py`. Chưa có Python: cài từ python.org, **tick "Add python.exe to PATH"**, mở lại PowerShell.
- macOS: báo `command not found: python` là bình thường → dùng `python3`.
- `python run.py` in ra "[câu trả lời giả — chưa nối model] …" là khung chạy đúng. Nối model thật: [docs/connect-model.md](docs/connect-model.md).

Trong README này lệnh viết là `python …`; máy nhóm cần `python3` hay `py` thì gõ thay.

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `python run.py` | Chạy bản chạy thử (gõ đầu vào, nhận kết quả, kèm số lần gọi model / token) |
| `python run.py check` | Kiểm `eval/benchmark.csv` (6 cột, số câu, `kho` / `tu_choi`, mã `source`, ô trống, dòng mẫu) `eval/metric_spec.yaml` (≥3 metric điền đủ) và `TEAMS.md` (đúng format để BTC quét). Chỉ cảnh báo, không sửa file |
| `python run.py eval --try` | **Thử nối model:** chạy 3 câu đầu (`--try 5` = 5 câu) → `eval/run-try.csv`. Thấy "Nối model được" là xong. Không tính là một lượt |
| `python run.py eval` | Chạy cả bộ qua `codebase/agent.py` → `eval/run-1.csv` (lần sau `run-2.csv`…) + `traces/run-1.jsonl`. Mỗi dòng có run ID, model, số lần gọi model / công cụ, token. Model còn giả → chỉ ghi `run-mock.csv`; mọi câu lỗi → `run-error.csv`; Ctrl+C → `run-stopped.csv` — đều **không** được đánh số |
| `python run.py eval --fake` | Thử riêng bộ chạy, không gọi agent → `eval/run-fake.csv` |
| `python run.py score eval/run-1.csv` | Sau khi điền cột `pass` (1 / 0): in % đạt tổng và theo `type`. Còn ô trống → "CHƯA CHẤM XONG", không in % |
| `python run.py simulate --try` | Thử mô phỏng chi phí 10 phiên (làm trước CP3) → `cost/simulate-try.csv` |
| `python run.py simulate` | Mô phỏng chi phí khi dùng thật theo `cost/personas.yaml` (≥50 phiên) → `cost/simulate-N.csv` + `cost/simulate-N-summary.md` |
| `python run.py simulate --rate-from eval/run-2.csv` | Như trên, lấy tỉ lệ đạt từ đúng lượt chỉ định. Không ghi thì khung lấy lượt `run-N` mới nhất đã chấm, cùng model, và ghi rõ đã lấy lượt nào trong bản tóm tắt |

Gói miễn phí báo hết lượt: thêm `--wait 4` sau `eval` hoặc `simulate` (nghỉ 4 giây giữa hai lượt gọi). Sửa CSV bằng Excel: *File → Save As → CSV UTF-8*; Google Sheets: *Tệp → Tải xuống → CSV*.

**Lượt có lỗi kỹ thuật** (cột `error` có chữ): không sửa tay file đó, chạy lại thành lượt mới và ghi vào bảng các lượt ở `eval/README.md`. Không xoá file lượt nào.

Nhóm dùng stack khác (Node, Streamlit, notebook…): sửa hàm `run_app()` trong `run.py` để `python run.py` vẫn chạy được bản chạy thử, và giữ `answer()` trong `codebase/agent.py` để `eval`, `simulate` chạy được.

## Bản chạy thử — viết ở đâu

| File | Viết gì | Bước guide |
|---|---|---|
| `codebase/agent.py` | `answer(text)` — luồng chính, đúng hình dạng ở `spec.md` §4. Khung có sẵn một workflow 2 bước *ví dụ* | 3.2 |
| `codebase/tools.py` | Công cụ của bài toán, mỗi công cụ một hàm có `@tool` | 2.2, 3.2 |
| `codebase/ai.py` | `call_model(system, user)` — chỗ duy nhất gọi model. Chưa điền `.env` thì chạy **chế độ giả** | 3.3 |

- **Trước CP2:** để chế độ giả, công cụ trả dữ liệu giả — `python run.py` đi hết luồng là đủ.
- **Trước CP3:** nối model thật theo [docs/connect-model.md](docs/connect-model.md), `eval --try` thấy token > 0 rồi mới `eval`.
- Bộ chạy gửi **nguyên ô `input`** của câu thử vào `answer(text)`. Dữ liệu nền (bài học, thông báo, lịch…) để trong `data/`, đọc qua công cụ.

## Phần nào thật, phần nào giả

| Thành phần | Thật / Giả | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | **Thật tại CP3** | `gpt-5.4-nano`; lượt 1 có Run ID `run-1@20261128-094522`, token đo từ API và kết quả 19/20. |
| Dữ liệu giao dịch | **Synthetic** | 252 dòng, 3 persona, 3 tháng, 7 nhóm chi, seed 42; không dùng chứng minh pain. |
| Bằng chứng pain E2 | **Có nguồn phỏng vấn bổ sung; giả thuyết khảo sát chưa kiểm chứng đầy đủ** | Có 31 phản hồi ẩn danh, 5 review nguyên văn và bản tóm tắt phỏng vấn 3 người ngoài nhóm sáng 28/11 được Tuân xác nhận, có đồng thuận dùng nội dung ẩn danh. Không nhận 6 đoạn tóm tắt là lời nói nguyên văn, không gộp mẫu hoặc coi ngưỡng khảo sát cũ đã được xác nhận. |

## Dùng AI vào việc gì

2–3 dòng (bắt buộc): nhóm dùng công cụ AI nào để làm gì, người kiểm lại phần nào. Chi tiết: [docs/ai-usage.md](docs/ai-usage.md). Coding agent đọc [AGENTS.md](AGENTS.md).

Nhóm dùng Codex để rà đề, chuyển bài sang E2, soạn workflow, dữ liệu synthetic, khảo sát và bộ câu thử. Thành viên phụ trách phải kiểm lại thiết kế, code, nguồn và từng câu thử; không dùng AI để tạo người phỏng vấn, câu trả lời khảo sát, review hay số liệu bằng chứng.

## File mẫu — điền ở bước nào

| File | Điền ở bước guide | Mốc |
|---|---|---|
| `TEAMS.md` | 1.0 | CP1 · **đúng format**, BTC quét khi chấm |
| `canvas.md` | 1.4 | CP1, cập nhật CP2 |
| `evidence/hypothesis.md` | 1.1 | trước khi tìm bằng chứng |
| `evidence/data-mining.md` · `evidence/interviews/TEMPLATE.md` → `P1.md`… · `evidence/survey/TEMPLATE.md` | 1.2 | bắt đầu sau Zoom, xong CP3 |
| `evidence/summary.md` | 1.2 | CP3 |
| `spec.md` | §0–§2: 1.1–1.3 · §3–§5: 2.1–2.3 · §7: 2.4 · §8: 4.2 · §10: suốt | §7 chốt CP2 · §0–§7 CP3 · đủ CP4 |
| `data/DATA_CARD.md` | 2.4 | bản đầu CP2 |
| `eval/benchmark.csv` · `eval/metric_spec.yaml` | 2.4 | ≥10 câu + metric chốt CP2 · 20–30 câu CP3 |
| `codebase/` | 3.2, 3.3 | khung CP2 · AI thật CP3 |
| `eval/report.md` · `eval/README.md` | 4.1 (README mục 1–4 từ 2.4) | CP4 |
| `cost/personas.yaml` · `cost/cost-estimate.md` | 4.2 | thử 10 phiên CP3 · đủ CP4 |
| `validation/log.md` *(bonus)* | 4.3 | CP4 |
| `slides/outline.md` → `demo-slides.pdf` | 5.1 | CP4 |
| `reflection/TEMPLATE.md` → `reflection/<ten>.md` | 5.3 | 23:59 Thứ Bảy 28/11 |
| `AGENTS.md` · `docs/ai-usage.md` | khi dùng coding agent / AI | suốt |

## Bảy hạng mục bắt buộc — nằm ở file nào

| # | Hạng mục | File |
|---|---|---|
| 1 | Bằng chứng pain | `evidence/` (tổng hợp ở `evidence/summary.md`) |
| 2 | Impact có số | `spec.md` §2 |
| 3 | Thiết kế giải pháp | `spec.md` §4 |
| 4 | Bản chạy thử làm trọn lát cắt | `codebase/` · lệnh ở mục "Lệnh" |
| 5 | Định nghĩa "tốt" + bộ câu thử | `data/DATA_CARD.md` · `eval/` |
| 6 | Mô phỏng chi phí khi dùng thật | `cost/` |
| 7 | Slide + demo + video dự phòng | `demo-slides.pdf` ở thư mục gốc · link video: ____ |
| + | *Bonus:* người dùng thử | `validation/log.md` |
