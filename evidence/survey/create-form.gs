function createBudgetSurveyForm() {
  const form = FormApp.create('Khảo sát theo dõi ngân sách trên ví/app ngân hàng', false);
  form.setDescription('Khảo sát hành vi trong 30 ngày qua. Không nhập tên, số dư, số tài khoản, lịch sử giao dịch hoặc ảnh sao kê.');

  const consent = form.addMultipleChoiceItem()
    .setTitle('Bạn đồng ý tham gia và cho phép dùng câu trả lời đã ẩn danh trong bài tập công khai?')
    .setRequired(true);

  const screenPage = form.addPageBreakItem().setTitle('Sàng lọc đối tượng');
  const screen = form.addMultipleChoiceItem()
    .setTitle('Trong 30 ngày qua, bạn có dùng ví/app ngân hàng và từng kiểm tra hoặc đặt giới hạn chi tiêu theo nhóm không?')
    .setRequired(true);

  const surveyPage = form.addPageBreakItem().setTitle('Trải nghiệm gần nhất');
  form.addMultipleChoiceItem().setTitle('Lần gần nhất bạn kiểm tra một nhóm chi là khi nào?')
    .setChoiceValues(['Hôm nay', 'Trong 7 ngày qua', '8–30 ngày trước', 'Không nhớ']).setRequired(true);
  form.addCheckboxItem().setTitle('Bạn đã kiểm tra bằng cách nào?')
    .setChoiceValues(['Tính năng trong app', 'Excel/Google Sheets', 'Tự cộng', 'Ghi chép', 'Nhớ/ước lượng', 'Khác']).setRequired(true);
  form.addMultipleChoiceItem().setTitle('Ở lần gần nhất, bạn phát hiện nhóm chi gần/vượt ngân sách vào lúc nào?')
    .setChoiceValues(['Trước khi chạm 80%', 'Khi gần hết', 'Sau khi vượt', 'Không gần/vượt', 'Không biết']).setRequired(true);
  form.addMultipleChoiceItem().setTitle('Bạn mất khoảng bao lâu để rà giao dịch và quyết định điều chỉnh?')
    .setChoiceValues(['Dưới 5 phút', '5–<15 phút', '15–<30 phút', '30–60 phút', 'Trên 60 phút', 'Không đo được']).setRequired(true);
  form.addParagraphTextItem().setTitle('Điều gì khó nhất ở lần đó? Nếu không khó, ghi điều giúp bạn làm nhanh.').setRequired(true);
  form.addGridItem().setTitle('Trong 30 ngày qua, các tình huống sau xảy ra bao nhiêu lần?')
    .setRows(['Phát hiện vượt ngân sách muộn', 'Khó hiểu mô tả/nhóm giao dịch', 'Cảnh báo quá chung chung hoặc không hữu ích'])
    .setColumns(['0', '1', '2–3', '4–5', '≥6', 'Không rõ']).setRequired(true);
  form.addParagraphTextItem().setTitle('Kể một trường hợp cụ thể gần nhất, cách xử lý và kết quả. Không ghi thông tin cá nhân hoặc bí mật.').setRequired(true);
  form.addCheckboxItem().setTitle('Nếu app cảnh báo nhóm chi chạm 80%, bạn muốn có quyền nào?')
    .setChoiceValues(['Bỏ qua', 'Tắt tạm', 'Sửa nhóm chi', 'Xem giao dịch làm căn cứ', 'Khác']).setRequired(true);

  consent.setChoices([
    consent.createChoice('Có', screenPage),
    consent.createChoice('Không', FormApp.PageNavigationType.SUBMIT),
  ]);
  screen.setChoices([
    screen.createChoice('Có', surveyPage),
    screen.createChoice('Không', FormApp.PageNavigationType.SUBMIT),
  ]);
  form.setConfirmationMessage('Cảm ơn bạn. Nhóm chỉ tổng hợp câu trả lời đã ẩn danh.');
  console.log('Edit URL: ' + form.getEditUrl());
}
