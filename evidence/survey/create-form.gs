/**
 * Chạy createSurveyForm trong Google Apps Script để tạo bản nháp Google Form.
 * Cần cấp quyền Google Forms; chưa publish, chưa gửi lời mời hay tạo phản hồi.
 * Nguồn API: https://developers.google.com/apps-script/reference/forms
 */
function createSurveyForm() {
  const properties = PropertiesService.getScriptProperties();
  const existingId = properties.getProperty('EVPROMOAI_SURVEY_FORM_ID');
  if (existingId) {
    const existing = FormApp.openById(existingId);
    return logSurveyLinks(existing);
  }

  const form = FormApp.create(
    'Khảo sát cách lựa chọn voucher cho dịch vụ gọi xe',
    false
  );
  Logger.log('Bản nháp đang tạo: ' + form.getEditUrl());
  form.setDescription(
    'Nhóm EVPromoAI đang tìm hiểu cách người phụ trách khuyến mãi lựa chọn ' +
    'mức voucher và người nhận cho dịch vụ gọi xe. Khảo sát hỏi về công việc ' +
    'đã thực hiện trong 30 ngày gần nhất; không có câu trả lời đúng hoặc sai. ' +
    'Mỗi người vui lòng trả lời một lần theo trải nghiệm thật.\n\n' +
    'Form không yêu cầu tên, email, số điện thoại hay tên công ty. ' +
    'Vui lòng không nhập thông tin nhận diện cá nhân, thông tin khách hàng ' +
    'hoặc số liệu nội bộ bí mật. Nhóm sử dụng câu trả lời để tổng hợp bài học ' +
    'và có thể trích dẫn đoạn đã ẩn danh trong repo bài tập công khai. ' +
    'Bạn có thể dừng bằng cách đóng form trước khi gửi.'
  );
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setPublishingSummary(false);
  form.setShowLinkToRespondAgain(false);
  form.setShuffleQuestions(false);
  form.setProgressBar(true);
  form.setConfirmationMessage(
    'Cảm ơn bạn đã chia sẻ trải nghiệm. Nhóm EVPromoAI sẽ tổng hợp ' +
    'các câu trả lời đã ẩn danh cho bài tập.'
  );

  const consent = form.addMultipleChoiceItem()
    .setTitle('Q1. Bạn có đồng ý tham gia và cho phép nhóm sử dụng câu trả lời đã ẩn danh để tổng hợp, trích dẫn trong bài tập công khai không?')
    .setRequired(true);
  const screeningPage = form.addPageBreakItem().setTitle('Vai trò và trải nghiệm');
  const role = form.addMultipleChoiceItem()
    .setTitle('Q2. Trong 30 ngày qua, vai trò nào mô tả đúng công việc của bạn nhất?')
    .setHelpText('Nếu là thành viên EVPromoAI, chọn đáp án đó dù đồng thời có vai trò nghề nghiệp khác. Chỉ tính đúng đối tượng khi trực tiếp quyết định hoặc duyệt voucher cho dịch vụ gọi xe.')
    .setRequired(true);
  const experiencePage = form.addPageBreakItem().setTitle('Công việc trong 30 ngày qua');

  const countValidation = FormApp.createTextValidation()
    .requireTextMatchesPattern('^(0|[1-9][0-9]*)$')
    .setHelpText('Nhập số nguyên không âm, ví dụ 0, 1 hoặc 12.')
    .build();
  form.addTextItem()
    .setTitle('Q3. Trong 30 ngày qua, bạn đã lựa chọn hoặc duyệt mức voucher và người nhận bao nhiêu lần?')
    .setHelpText('Tính mỗi lần ra quyết định hoặc duyệt là một lần, không tính theo số voucher phát ra; có thể ước lượng và dùng cùng cách đếm.')
    .setValidation(countValidation)
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('Q4. Ở lần gần nhất, bạn đã dựa vào những cách nào để lựa chọn voucher?')
    .setChoiceValues([
      'Excel/Google Sheets hoặc tính toán thủ công.',
      'Quy tắc cố định hoặc phân nhóm khách hàng có sẵn.',
      'Báo cáo lịch sử đặt chuyến và sử dụng ưu đãi.',
      'Kết quả A/B test hoặc thử nghiệm có nhóm đối chứng.',
      'Công cụ tự động đề xuất/tối ưu mức voucher.',
      'Kinh nghiệm cá nhân hoặc trao đổi với đồng nghiệp.',
      'Không rõ/không nhớ.'
    ])
    .showOtherOption(true)
    .setRequired(true);
  addChoiceQuestion(form,
    'Q5. Ở lần gần nhất, từ khi bắt đầu xem dữ liệu đến khi chốt quyết định voucher, bạn mất khoảng bao lâu?',
    ['Dưới 5 phút.', 'Từ 5 đến dưới 15 phút.', 'Từ 15 đến dưới 30 phút.',
      'Từ 30 đến 60 phút.', 'Trên 60 phút.', 'Không nhớ/không đo được.']);
  addChoiceQuestion(form,
    'Q6. Kết quả công việc ở lần gần nhất là gì?',
    ['Đã chốt được mức voucher và người nhận.',
      'Chỉ chốt được một phần, còn phải bổ sung hoặc kiểm tra.',
      'Chưa chốt được.', 'Đã dừng vì không cần tiếp tục.', 'Không nhớ.']);
  form.addParagraphTextItem()
    .setTitle('Q7. Điều gì gây khó khăn nhất trong lần đó, nếu có?')
    .setHelpText('Mô tả theo trải nghiệm thực tế. Nếu không gặp khó khăn, có thể ghi “Không gặp khó khăn” và điều giúp công việc thuận lợi. Không nêu tên người, công ty hoặc khách hàng.')
    .setRequired(true);
  form.addGridItem()
    .setTitle('Q8. Trong 30 ngày qua, mỗi tình huống sau đã xảy ra bao nhiêu lần khi bạn làm công việc này?')
    .setHelpText('Một lần ra quyết định có thể gặp nhiều tình huống. Chọn 0 nếu không xảy ra; không rõ thì chọn “Không rõ/không theo dõi”.')
    .setRows([
      'Khó xác định ưu đãi có tạo thêm chuyến so với không ưu đãi hay không.',
      'Phải điều chỉnh voucher vì giới hạn ngân sách hoặc biên lợi nhuận.',
      'Khó giải thích lý do chọn mức voucher hoặc nhóm người nhận.'
    ])
    .setColumns(['0 lần', '1 lần', '2–3 lần', '4–5 lần', 'Từ 6 lần', 'Không rõ/không theo dõi'])
    .setRequired(true);
  form.addParagraphTextItem()
    .setTitle('Q9. Bạn có thể kể một trường hợp cụ thể trong 30 ngày qua, cách đã xử lý và kết quả không?')
    .setHelpText('Có thể kể trường hợp gặp hoặc không gặp trở ngại. Chỉ nêu điều đã quan sát; nếu nói về thời gian/chi phí thì phân biệt số ghi nhận và số tự ước lượng. Có thể ghi “Không có trường hợp để chia sẻ”; không cung cấp dữ liệu bí mật hoặc nhận diện cá nhân.')
    .setRequired(true);
  addChoiceQuestion(form,
    'Q10. Ở lần gần nhất, bạn đã kiểm tra hiệu quả tăng thêm của voucher bằng cách nào?',
    ['So sánh với nhóm không nhận ưu đãi trong thử nghiệm có kiểm soát.',
      'So sánh số chuyến/doanh thu trước và sau chiến dịch.',
      'Theo dõi số lượt sử dụng voucher.',
      'Dựa vào kinh nghiệm hoặc phản hồi của đội vận hành.',
      'Chưa đánh giá hiệu quả tăng thêm.', 'Không rõ/không nhớ.'])
    .showOtherOption(true);

  consent.setChoices([
    consent.createChoice('Đồng ý', screeningPage),
    consent.createChoice('Không đồng ý', FormApp.PageNavigationType.SUBMIT)
  ]);
  const eligibleRoles = [
    'Quản lý tăng trưởng/marketing: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe',
    'Phụ trách vận hành: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe',
    'Phụ trách kinh doanh/chính sách: trực tiếp chọn hoặc duyệt mức voucher và người nhận cho dịch vụ gọi xe'
  ];
  const excludedRoles = [
    'Chỉ triển khai mã hoặc quảng cáo theo quyết định của người khác',
    'Chọn/duyệt voucher cho ngành khác, không phải dịch vụ gọi xe',
    'Chỉ sử dụng voucher với tư cách khách hàng',
    'Là thành viên nhóm EVPromoAI',
    'Không thuộc các vai trò trên hoặc chưa làm công việc này trong 30 ngày qua'
  ];
  role.setChoices(
    eligibleRoles.map(label => role.createChoice(label, experiencePage)).concat(
      excludedRoles.map(label => role.createChoice(label, FormApp.PageNavigationType.SUBMIT))
    )
  );

  properties.setProperty('EVPROMOAI_SURVEY_FORM_ID', form.getId());
  return logSurveyLinks(form);
}

function addChoiceQuestion(form, title, choices) {
  return form.addMultipleChoiceItem()
    .setTitle(title)
    .setChoiceValues(choices)
    .setRequired(true);
}

function logSurveyLinks(form) {
  const links = {editUrl: form.getEditUrl(), responseUrl: form.getPublishedUrl()};
  Logger.log('Link chỉnh sửa (nội bộ nhóm): ' + links.editUrl);
  Logger.log('Link trả lời (chỉ dùng sau khi publish): ' + links.responseUrl);
  return links;
}
