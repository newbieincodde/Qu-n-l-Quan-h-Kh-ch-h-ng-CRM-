💡 Ý TƯỞNG DỰ ÁN: "MEDCARE CRM — HỆ THỐNG QUẢN TRỊ BỆNH NHÂN & TỰ ĐỘNG HÓA CHĂM SÓC Y TẾ"
🎯 1. CÂU CHUYỆN THƯƠNG HIỆU & BỐI CẢNH (STORYLINE)
Bối cảnh thực tế: Nhóm lấy bối cảnh tại "Trung tâm Y tế Đa khoa MedCare (Đồng Nai)" — một cơ sở y tế tầm trung đang trong quá trình chuyển đổi số.
Vấn đề của phòng khám cũ:
Mỗi ngày tiếp đón 100+ bệnh nhân nhưng nhân viên chỉ ghi chép trên sổ hoặc file Excel rời rạc.
Bệnh nhân khám xong ra về là phòng khám... mất liên lạc luôn, không ai nhắc lịch tái khám, không hỏi thăm xem uống thuốc có bị dị ứng không.
Bệnh nhân trung thành (đến khám nhiều lần, chi tiêu lớn) không nhận được bất kỳ ưu đãi hay sự chăm sóc riêng biệt nào so với khách vãng lai.
Ý tưởng đột phá của MedCare CRM:
Xây dựng một hệ thống Web CRM khép kín giúp: Thu thập khách từ ngoài Web 
→
→ Lọc danh sách cần gọi mỗi sáng 
→
→ Tự động phân hạng tri ân Đồng/Bạc/Vàng 
→
→ Khảo sát độ hài lòng sau điều trị.
🧩 2. Ý TƯỞNG CỤ THỂ CHO TỪNG PHÂN HỆ (GẮN VỚI 4 THÀNH VIÊN)

Dựa vào bài cũ, nhóm bạn sẽ chia ý tưởng thành 4 khối chức năng độc lập cực kỳ logic:

[Khối 0: Cổng tiếp nhận Leads & Đăng nhập] ──> Bạn Ngọc Nhân (Nhóm trưởng)
[Khối 1: Bàn làm việc nhắc lịch mỗi sáng]   ──> Bạn giahuy (Trang Chủ Dashboard)
[Khối 2: Hồ sơ 360° & Phân hạng chi tiêu]  ──> Bạn minhhuy (Danh Bạ Khách Hàng)
[Khối 3: Nhật ký tư vấn & Khảo sát CSAT]   ──> Bạn quang (Form Chăm Sóc)
🟢 KHỐI 1 (BẠN Giahuy): Ý TƯỞNG "MỖI SÁNG MỞ MÁY BIẾT CẦN CHĂM SÓC AI"
Tên trang: Trang Chủ Dashboard (dashboard/index.html)
Ý tưởng cốt lõi: Nhân viên điều dưỡng mở máy tính đầu giờ sáng là thấy ngay việc cần làm, không cần tìm kiếm.
Các tính năng "ăn điểm":
Bảng "Danh sách khách cần liên hệ hôm nay": Tự động lọc ra 5–10 bệnh nhân có lịch hẹn tái khám trùng với ngày hiện tại (ví dụ: tái khám tiểu đường, thay băng vết mổ, tiêm chủng mũi 2).
4 Thẻ số liệu KPI tóm tắt:
Tổng số bệnh nhân quản lý: 50 người.
Cuộc gọi cần thực hiện hôm nay: 5 cuộc.
Tỷ lệ bệnh nhân quay lại tái khám: 88.5%.
Doanh thu dự kiến trong ngày: 12.500.000đ.
Biểu đồ Chart.js: Thống kê lượng bệnh nhân đến khám theo các ngày trong tuần.
🔵 KHỐI 2 (BẠN MinhHuy): Ý TƯỞNG "HỒ SƠ SỨC KHỎE 360° & TỰ ĐỘNG PHÂN HẠNG TRI ÂN"
Tên trang: Danh Bạ Khách Hàng (dashboard/customers.html)
Ý tưởng cốt lõi: Bệnh nhân không chỉ là một con số, mà là một khách hàng cần được phân hạng để chăm sóc theo chuẩn dịch vụ cao cấp.
Các tính năng "ăn điểm":
Bảng danh bạ thông minh: Tìm kiếm tức thời theo Tên hoặc Số điện thoại, lọc nhanh theo từng nhóm hạng thẻ.
Thuật toán JavaScript phân loại tự động (Trọng tâm đề bài LHU):
Thay vì nhân viên tự chọn bằng tay, hàm JS tự tính tổng số tiền khám bệnh (totalSpent) tích lũy:
🥉 Hạng Đồng (Bronze): Chi tiêu dưới 5 triệu 
→
→ Nhắc lịch định kỳ tiêu chuẩn.
🥈 Hạng Bạc (Silver): Chi tiêu từ 5 đến 15 triệu 
→
→ Ưu đãi giảm 5% xét nghiệm.
🥇 Hạng Vàng (Gold): Chi tiêu trên 15 triệu 
→
→ Có bác sĩ gia đình riêng, phòng chờ VIP.
Modal Hồ sơ điện tử 360° (EHR): Bấm vào bệnh nhân sẽ hiện popup toàn bộ lịch sử: nhóm máu, tiền sử dị ứng thuốc, các toa thuốc đã kê từ các lần khám trước.
🟡 KHỐI 3 (BẠN quang): Ý TƯỞNG "LẮNG NGHE & ĐO LƯỜNG ĐỘ HÀI LÒNG BỆNH NHÂN"
Tên trang: Form Chăm Sóc & Khảo Sát (dashboard/customer-care.html & surveys.html)
Ý tưởng cốt lõi: Đóng kín vòng lặp trải nghiệm người bệnh bằng việc thu nhận phản hồi sau khám.
Các tính năng "ăn điểm":
Form Nhật ký chăm sóc: Điều dưỡng sau khi gọi điện sẽ chọn tên khách, ghi lại tình trạng sức khỏe sau khi dùng thuốc, dặn dò của bác sĩ và bấm "Lưu nhật ký" (lưu vào localStorage).
Bảng Khảo sát CSAT (Áp dụng CSS Transition mượt mà):
Đánh giá 5 sao thái độ bác sĩ, thời gian chờ khám, cơ sở vật chất.
Hiệu ứng CSS Transition: Khi rê chuột qua các ngôi sao, sao tự phóng to 1.3 lần và đổi màu vàng cam mượt mà (transition: transform 0.2s, color 0.2s).
Thanh đo mức độ hài lòng tự động co giãn êm ái khi đổi điểm số.
🟣 KHỐI 0 (BẠN NGỌC NHÂN - NHÓM TRƯỞNG): Ý TƯỞNG "CỔNG MARKETING & TIẾP NHẬN BỆNH NHÂN TỪ XA"
Tên trang: Landing Page & Form Thu Thập Leads (index.html, pages/login.html, dashboard/leads.html)
Ý tưởng cốt lõi: Giúp phòng khám thu hút bệnh nhân mới từ Internet mà không cần tốn chi phí quảng cáo đắt đỏ.
Các tính năng "ăn điểm":
Landing Page chuyên nghiệp: Giới thiệu mạng lưới cơ sở, chuyên khoa, cẩm nang sức khỏe và popup đặt lịch khám online toàn quốc.
Form ghi nhận Leads (Bắt buộc trong đề bài LHU): Bệnh nhân đặt lịch trên Landing Page 
→
→ Dữ liệu tự động bay vào trang leads.html của phòng khám với đầy đủ Regex kiểm tra SĐT 10 số.
Phân tích CLV (Giá trị vòng đời khách hàng): Báo cáo trực quan nhóm khách hàng nào mang lại nguồn thu lớn nhất để định hướng kinh doanh y tế.
🏆 TẠI SAO Ý TƯỞNG NÀY ĐẢM BẢO ĐẠT ĐIỂM TỐI ĐA (RUBRIC ĐIỂM A)?
Tiêu chí chấm của Giảng viên	Ý tưởng MedCare CRM giải quyết thế nào?
1. Tính thực tiễn & Ý nghĩa xã hội	Đề tài Y tế số có tính nhân văn cao, vượt trội hơn các đề tài bán trà sữa, bán giày dép thông thường.
2. Đúng 100% yêu cầu kỹ thuật	Đầy đủ: Form HTML5 có Regex Leads, CSS Transition ở khảo sát CSAT, JavaScript tính điểm phân loại Đồng/Bạc/Vàng.
3. Cấu trúc 3 trang chuẩn mực	Phân công đúng 3 trang tối thiểu cho 3 bạn, nhóm trưởng bao quát cổng Portal.
4. Công nghệ thuần khiết (Pure Web)	Không dùng framework nặng nề, tốc độ tải trang dưới 0.5s, lưu dữ liệu LocalStorage mượt mà.
📝 BẠN CÓ THỂ COPY ĐOẠN NÀY LÀM TÓM TẮT DỰ ÁN TRONG ngocnhan.md:

*"Dự án MedCare CRM xây dựng giải pháp chuyển đổi số cho trung tâm y tế đa khoa với 4 trụ cột:

Cổng tiếp thị số: Thu hút bệnh nhân đặt lịch từ xa (Landing Page & Form Leads).
Vận hành mỗi ngày: Trang chủ tự động thông báo danh sách bệnh nhân cần gọi nhắc lịch tái khám hôm nay.
Cá nhân hóa dịch vụ: JavaScript tự động phân loại hạng thẻ Đồng · Bạc · Vàng dựa trên tổng chi tiêu để tri ân bệnh nhân thân thiết.
Nâng cao chất lượng: Form nhật ký chăm sóc sau điều trị kết hợp bảng khảo sát độ hài lòng ứng dụng CSS Transition mượt mà."*