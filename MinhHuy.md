# Quá trình lên ý tưởng MedCare CRM cùng ChatGPT

| Thông tin | Nội dung |
|---|---|
| Sinh viên | Minh Huy |
| Dự án | MedCare CRM – Hệ thống đăng ký và quản lý khám bệnh trực tuyến |
| Học phần | Thiết kế Web – Đại học Lạc Hồng (LHU) |
| Công cụ trao đổi ý tưởng | ChatGPT / Antigravity AI |
| Cập nhật | 23/11/2026 |

---

## 1. Xác định CRM cần giải quyết việc gì

Tôi bắt đầu bằng câu hỏi liệu CRM có thể tập trung vào hai việc là **phân bổ khách hàng** và **chăm sóc khách hàng** hay không. ChatGPT giải thích rằng phân bổ là giao hồ sơ hoặc yêu cầu cho nhân viên phụ trách, còn chăm sóc là ghi lại nội dung trao đổi, phản hồi của khách và thời điểm cần liên hệ tiếp.

Ví dụ ban đầu là một khách để lại số điện thoại, quản lý giao cho nhân viên tư vấn, nhân viên ghi lại yêu cầu báo giá và hẹn gọi lại vào thứ Sáu. Đến ngày hẹn, khách xuất hiện trong danh sách **Cần chăm sóc hôm nay**. Từ ví dụ đó, hai bên phác thảo ba màn hình gồm Trang chủ, Danh bạ và Form chăm sóc.

## 2. Phương án 1 – CRM chăm sóc sau bán hàng

Tôi đề xuất một website bán hàng có phần CRM để khách phản hồi về tình trạng sản phẩm hoặc yêu cầu đổi trả. ChatGPT gợi ý áp dụng cho shop điện tử và phụ kiện, nơi có thể minh họa bằng các ca giao sai mẫu, sản phẩm bị lỗi hoặc đổi hàng.

**Luồng minh họa** — Khách báo tai nghe chỉ nghe được một bên → nhân viên tra hồ sơ và xác nhận mã đơn → tạo yêu cầu đổi hàng → quản lý giao người xử lý → nhân viên ghi kết quả và hẹn ngày báo lại → yêu cầu hiện trên Trang chủ vào ngày hẹn.

## 3. Phương án 2 – CRM đặt lịch khám và hỗ trợ bệnh nhân

Tôi đề xuất cho bệnh nhân đặt lịch trực tuyến, xác minh CCCD và BHYT, tìm bệnh viện gần mình. ChatGPT diễn giải thành hai luồng: bệnh nhân tìm cơ sở, đặt lịch; nhân viên tiếp nhận, phân công và theo dõi.

| Nội dung tôi đưa ra | Cách ChatGPT gợi ý triển khai |
|---|---|
| Xác minh CCCD và BHYT | Dùng dữ liệu giả mô phỏng trạng thái **Chưa xác minh / Đã xác minh** |
| Đề xuất cơ sở gần bệnh nhân | Lọc theo chuyên khoa, sắp xếp theo khoảng cách hoặc lịch trống sớm nhất |
| Phân bổ bệnh nhân | Lễ tân phân công nhân viên xác nhận, nhắc hẹn hoặc hỗ trợ đổi lịch |
| Giải đáp thắc mắc | Mục hỏi đáp; câu hỏi liên quan hồ sơ chuyển cho nhân viên phụ trách |

## 4. Đối chiếu hai phương án với đề học phần

| Yêu cầu trong đề | Phương án shop điện tử | Phương án MedCare CRM |
|---|---|---|
| Form Leads HTML5 | Ghi nhận người quan tâm sản phẩm | Ghi nhận người muốn tư vấn/đặt lịch lần đầu |
| CSS Transition khảo sát | Hiệu ứng chọn mức hài lòng sau đổi trả | Hiệu ứng chọn mức hài lòng về trải nghiệm đặt lịch |
| JS xếp hạng Đồng/Bạc/Vàng | Cộng giá trị đơn hàng | Cộng giá trị giao dịch dịch vụ |
| Trang chủ | Khách cần gọi lại / cập nhật đổi trả | Bệnh nhân cần xác nhận lịch / nhắc hẹn |
| Trang Danh bạ | Thông tin liên hệ, đơn hàng, lịch sử | Thông tin liên hệ, lịch hẹn, lịch sử |
| Form chăm sóc | Ghi phản hồi, đổi trả, người xử lý | Ghi phản hồi, đổi lịch, người phụ trách |

## 5. Phạm vi bản demo MedCare CRM

Phương án được chọn là **mô phỏng cho một phòng khám** — tập trung tiếp nhận đăng ký, phân công nhân viên và hỗ trợ đổi lịch. Kịch bản thuyết trình: người dùng gửi form tư vấn → nhân viên xác nhận lịch → ghi yêu cầu đổi giờ vào Form chăm sóc → hẹn ngày gọi lại → hồ sơ hiện Trang chủ → xem hạng JavaScript → khảo sát CSS Transition.

---

## 🛠️ Lịch Sử Sửa Chữa Với AI

### Navbar & Giao Diện Trang Chủ

| Ngày | Nội dung sửa | File thay đổi | Kết quả |
|:---|:---|:---|:---|
| 23/11/2026 | Thêm font **Nunito** cho navbar, tăng font-weight logo/nav/hotline | `css/medpro-style.css`, `index.html` | Font sắc nét, chuyên nghiệp hơn |
| 23/11/2026 | Giảm kích cỡ hotline badge, thêm `height: 36px` cố định | `css/medpro-style.css` | Badge thẳng hàng với logo và nav-links |
| 23/11/2026 | Thu gọn toàn bộ navbar: height 72→60px, font 14.5→13px, căn giữa nav-links | `css/medpro-style.css`, `index.html` | Navbar 1 hàng thẳng hàng hoàn toàn |

### Trang Đăng Nhập (Login)

| Ngày | Nội dung sửa | File thay đổi | Kết quả |
|:---|:---|:---|:---|
| 23/11/2026 | Redesign form login theo mẫu shadcn/ui — thêm class `lf-*`, FieldGroup/Field/Separator | `pages/login.html`, `css/auth.css` | Form gọn, label rõ, input 40px, separator đẹp |
| 23/11/2026 | Đổi vị trí 2 panel: form sang trái, nội dung sang phải (dùng CSS `order`) | `css/auth.css` | Form đăng nhập bên trái, thẻ y tế bên phải |
| 23/11/2026 | Thay nền gradient xanh → ảnh bác sĩ thực tế + dark overlay 62% | `css/auth.css`, `assets/images/login-bg.jpg` | Nền ảnh rõ nét, chữ trắng vẫn đọc được |
| 23/11/2026 | Cập nhật ảnh nền login chất lượng cao hơn | `assets/images/login-bg.jpg` | Ảnh sắc nét, đẹp hơn |
| 23/11/2026 | Xóa Demo Card & Role Tabs để tăng bảo mật | `pages/login.html` | Chỉ còn form đăng nhập thuần — không lộ tài khoản mẫu |
| 23/11/2026 | Navbar: xóa "Vào CRM Portal", thêm nút "Đăng Ký" nối đến `register.html` | `index.html` | Luồng: Trang chủ → Đăng Ký / Đăng Nhập, dữ liệu lưu qua `auth.js` + LocalStorage |

---

> [!NOTE]
> Các lần sửa tiếp theo sẽ được bổ sung vào bảng tương ứng bên trên.
