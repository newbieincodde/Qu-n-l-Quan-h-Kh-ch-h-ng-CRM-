# QUY CHUẨN CODE DÀNH CHO AI AGENT — MEDCARE CRM
Áp dụng cho mọi câu trả lời và mã nguồn sinh ra trong dự án này:

## 1. CÔNG NGHỆ BẮT BUỘC
- Chỉ sử dụng: HTML5 Semantic, CSS3, Vanilla JavaScript (ES6+), LocalStorage.
- TUYỆT ĐỐI KHÔNG dùng Framework (React, Vue, Angular), KHÔNG dùng backend (Node.js, Express, PHP).

## 2. DESIGN SYSTEM & CSS (KHÔNG TỰ BỊA RA CSS MỚI)
- Font chữ duy nhất: 'Be Vietnam Pro', sans-serif.
- Bảng màu chuẩn:
  + Màu chính (Brand Teal): #0F766E (--clr-primary-700)
  + Màu chữ chính (Slate): #0F172A (--clr-text-primary)
  + Màu nền thẻ: #FFFFFF, nền trang: #F8FAFC
- BẮT BUỘC sử dụng các class có sẵn trong `css/dashboard.css`:
  + Khung thẻ: .data-card, .data-card-header, .data-card-body
  + Ô nhập liệu: .form-group, .form-label, .form-control
  + Nút bấm: .btn, .btn-primary, .btn-secondary
  + Bảng dữ liệu: <table>, <thead>, <tbody>
  + Huy hiệu hạng: .badge-rank.gold, .badge-rank.silver, .badge-rank.bronze

## 3. PHẠM VI TRANG (SCOPE RULE)
- Mỗi thành viên chỉ chỉnh sửa trong trang được phân công.
- Không tự ý sửa đổi file data.js dùng chung.

🎯 GỌNG KÌM 2: ĐOẠN "THẦN CHÚ 5 DÒNG" (DÀNH CHO CHATGPT / CLAUDE / GEMINI TRÊN WEB)

Nếu các bạn trong nhóm chat với ChatGPT hoặc Claude trên trình duyệt web, các bạn đó không có file .md.

Bạn hãy soạn sẵn đoạn tin nhắn này và ghim (pin) lên nhóm Zalo của nhóm, dặn các bạn:

"Mỗi lần nhờ ChatGPT viết cái gì, copy đoạn này dán ở đầu trước khi hỏi:"

📋 ĐOẠN PROMPT MẪU (COPY DÁN VÀO ĐẦU CÂU HỎI CHATGPT):

*"Tôi đang làm bài tập nhóm dự án MedCare CRM (thuần HTML/CSS/JS, font 'Be Vietnam Pro', màu xanh Teal #0F766E và chữ Slate #0F172A).
Quy tắc bắt buộc:

Không dùng React hay thư viện ngoài.
Dùng các class CSS có sẵn của hệ thống: .data-card, .form-group, .form-label, .form-control, .btn-primary, thẻ <table>. KHÔNG tự tạo mã màu hay CSS mới.
Dữ liệu lấy từ mảng mẫu trong js/data.js.

Yêu cầu của tôi là: [Dán yêu cầu cần làm vào đây, ví dụ: Viết form nhập nhật ký chăm sóc khách hàng / Viết bảng danh sách khách hàng...]"*

🛡️ TẠI SAO CÁCH NÀY HIỆU QUẢ 100%?
AI bị "bịt mắt" không thể sáng tạo bậy bạ: Con AI nào nhận được đoạn prompt này cũng sẽ ngoan ngoãn sử dụng đúng tên class .data-card, .form-control, .btn-primary mà MedCare CRM đang có.
Code của 3 bạn copy ra dán vào web là ăn ngay: Không bị vỡ khung, không bị lệch màu, nút bấm vẫn đẹp long lanh đúng chuẩn của cả nhóm.
Các bạn có sẵn prompt xịn để dán vào báo cáo: 3 bạn chỉ việc copy chính đoạn prompt này đưa vào file prompt_log.md nộp cho trường, giảng viên đọc vào sẽ thấy câu lệnh cực kỳ bài bản và chuẩn chỉ!
