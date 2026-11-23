## 1. Giới thiệu dự án

**Tên dự án:** SalesPro CRM  
**Loại hệ thống:** Website quản lý quan hệ khách hàng (CRM – Customer Relationship Management)  
**Định hướng:** Hỗ trợ doanh nghiệp quản lý khách hàng, đơn hàng, nhân viên bán hàng và hoạt động chăm sóc khách hàng trên một nền tảng tập trung.

### Mục tiêu
- Lưu trữ và quản lý thông tin khách hàng có hệ thống.
- Theo dõi lịch sử mua hàng và tương tác với khách hàng.
- Quản lý đơn hàng, sản phẩm và doanh thu.
- Phân công công việc cho nhân viên.
- Cung cấp báo cáo giúp người quản lý theo dõi tình hình kinh doanh.

## 2. Đối tượng sử dụng

| Vai trò | Quyền và nhiệm vụ chính |
|---|---|
| Admin | Quản lý tài khoản, phân quyền, dữ liệu và cấu hình hệ thống |
| Quản lý | Theo dõi khách hàng, đơn hàng, nhân viên và báo cáo |
| Nhân viên bán hàng | Quản lý khách hàng được giao, tạo đơn và cập nhật tiến độ |
| Nhân viên chăm sóc khách hàng | Ghi nhận tương tác, phản hồi và lịch chăm sóc |

## 3. Các chức năng chính

### 3.1. Đăng nhập và phân quyền
- Đăng nhập, đăng xuất.
- Đổi mật khẩu.
- Phân quyền theo vai trò.
- Chặn người dùng truy cập chức năng không được cấp quyền.

### 3.2. Dashboard – Tổng quan
Hiển thị các chỉ số:
- Tổng số khách hàng.
- Số khách hàng mới trong tháng.
- Tổng số đơn hàng.
- Đơn hàng đang xử lý.
- Doanh thu theo ngày, tháng hoặc năm.
- Biểu đồ doanh thu và tình trạng đơn hàng.

### 3.3. Quản lý khách hàng
- Thêm, xem, sửa và xóa khách hàng.
- Tìm kiếm theo tên, số điện thoại hoặc email.
- Lọc theo nhóm khách hàng và nhân viên phụ trách.
- Phân loại khách hàng: tiềm năng, đang giao dịch, thân thiết.
- Xem lịch sử mua hàng và lịch sử chăm sóc.
- Ghi chú thông tin cần lưu ý.

### 3.4. Quản lý sản phẩm
- Thêm, sửa, xóa và xem sản phẩm.
- Quản lý mã sản phẩm, tên, giá bán và số lượng tồn.
- Tìm kiếm và lọc sản phẩm.
- Bật hoặc tắt trạng thái kinh doanh.

### 3.5. Quản lý đơn hàng
- Tạo đơn hàng cho khách hàng.
- Thêm nhiều sản phẩm vào một đơn.
- Tự động tính tổng tiền.
- Cập nhật trạng thái: mới tạo, đang xử lý, hoàn thành, đã hủy.
- Xem chi tiết và lịch sử cập nhật đơn hàng.

### 3.6. Quản lý công việc và lịch chăm sóc
- Tạo nhiệm vụ gọi điện, gửi email hoặc gặp khách hàng.
- Giao nhiệm vụ cho nhân viên.
- Đặt ngày đến hạn.
- Cập nhật trạng thái: cần làm, đang làm, hoàn thành.
- Ghi lại kết quả sau mỗi lần liên hệ.

### 3.7. Báo cáo và thống kê
- Thống kê doanh thu theo khoảng thời gian.
- Thống kê số lượng đơn hàng theo trạng thái.
- Thống kê khách hàng mới.
- Thống kê hiệu quả bán hàng theo nhân viên.
- Xuất báo cáo CSV hoặc Excel (có thể triển khai ở giai đoạn nâng cao).

## 4. Cấu trúc các trang

1. `/login` – Đăng nhập.
2. `/dashboard` – Tổng quan.
3. `/customers` – Danh sách khách hàng.
4. `/customers/:id` – Chi tiết khách hàng.
5. `/products` – Danh sách sản phẩm.
6. `/orders` – Danh sách đơn hàng.
7. `/orders/:id` – Chi tiết đơn hàng.
8. `/tasks` – Công việc và lịch chăm sóc.
9. `/reports` – Báo cáo, thống kê.
10. `/users` – Quản lý tài khoản (Admin).

## 5. Công nghệ đề xuất

| Thành phần | Công nghệ |
|---|---|
| Frontend | ReactJS |
| Ngôn ngữ giao diện | HTML, CSS, JavaScript |
| CSS framework | Tailwind CSS hoặc Bootstrap |
| Backend | Node.js và Express |
| Cơ sở dữ liệu | MySQL |
| Biểu đồ | Chart.js |
| Thiết kế giao diện | Figma |
| Quản lý mã nguồn | Git và GitHub |

> Nếu mới bắt đầu, có thể làm phiên bản HTML/CSS/JavaScript trước, sau đó tích hợp React, backend và MySQL.

## 6. Thiết kế cơ sở dữ liệu dự kiến

Các bảng chính:

### `users`
- `id` – Khóa chính.
- `full_name` – Họ tên.
- `email` – Email đăng nhập.
- `password_hash` – Mật khẩu đã băm.
- `role` – Vai trò.
- `created_at` – Ngày tạo.

### `customers`
- `id` – Khóa chính.
- `name` – Tên khách hàng.
- `phone` – Số điện thoại.
- `email` – Email.
- `address` – Địa chỉ.
- `customer_type` – Loại khách hàng.
- `assigned_user_id` – Nhân viên phụ trách.
- `created_at` – Ngày tạo.

### `products`
- `id` – Khóa chính.
- `product_code` – Mã sản phẩm.
- `name` – Tên sản phẩm.
- `price` – Giá bán.
- `stock_quantity` – Số lượng tồn.
- `status` – Trạng thái.

### `orders`
- `id` – Khóa chính.
- `customer_id` – Khách hàng đặt hàng.
- `created_by` – Nhân viên tạo đơn.
- `order_date` – Ngày tạo đơn.
- `total_amount` – Tổng tiền.
- `status` – Trạng thái đơn hàng.

### `order_items`
- `id` – Khóa chính.
- `order_id` – Đơn hàng.
- `product_id` – Sản phẩm.
- `quantity` – Số lượng.
- `unit_price` – Đơn giá tại thời điểm đặt.
- `subtotal` – Thành tiền.

### `tasks`
- `id` – Khóa chính.
- `customer_id` – Khách hàng liên quan.
- `assigned_user_id` – Nhân viên được giao.
- `title` – Nội dung công việc.
- `due_date` – Hạn hoàn thành.
- `status` – Trạng thái.
- `result_note` – Kết quả hoặc ghi chú.

### `customer_interactions`
- `id` – Khóa chính.
- `customer_id` – Khách hàng.
- `user_id` – Nhân viên thực hiện.
- `interaction_type` – Loại tương tác.
- `content` – Nội dung trao đổi.
- `created_at` – Thời gian tương tác.

## 7. Quan hệ dữ liệu cơ bản

- Một nhân viên có thể phụ trách nhiều khách hàng.
- Một khách hàng có thể có nhiều đơn hàng.
- Một đơn hàng có nhiều dòng sản phẩm trong `order_items`.
- Một sản phẩm có thể xuất hiện trong nhiều dòng đơn hàng.
- Một khách hàng có thể có nhiều nhiệm vụ chăm sóc.
- Một khách hàng có thể có nhiều lịch sử tương tác.

## 8. Gợi ý giao diện

### Phong cách
- Giao diện quản trị hiện đại, tối giản.
- Sidebar bên trái để điều hướng.
- Thanh trên cùng hiển thị tìm kiếm, thông báo và tài khoản.
- Khu vực nội dung có thẻ thống kê, bảng dữ liệu và biểu đồ.
- Ưu tiên bố cục rõ ràng, dễ sử dụng trên máy tính và điện thoại.

### Các thành phần nên có
- Sidebar điều hướng.
- Thanh tìm kiếm.
- Bộ lọc dữ liệu.
- Bảng có phân trang.
- Hộp thoại thêm/sửa dữ liệu.
- Thông báo thành công hoặc lỗi.
- Biểu đồ doanh thu.

## 9. Lộ trình thực hiện

| Giai đoạn | Công việc |
|---|---|
| 1. Phân tích | Xác định yêu cầu, người dùng và chức năng |
| 2. Thiết kế | Vẽ wireframe, thiết kế giao diện và sơ đồ database |
| 3. Frontend | Xây dựng các trang và thành phần giao diện |
| 4. Backend | Xây dựng API, đăng nhập và phân quyền |
| 5. Database | Tạo bảng, khóa và quan hệ dữ liệu |
| 6. Tích hợp | Kết nối frontend, backend và database |
| 7. Kiểm thử | Kiểm tra chức năng, dữ liệu và phân quyền |
| 8. Hoàn thiện | Sửa lỗi, viết tài liệu và chuẩn bị thuyết trình |

## 10. Phạm vi phiên bản đầu tiên (MVP)

Để tránh dự án quá lớn, nên ưu tiên hoàn thành:
1. Đăng nhập và phân quyền cơ bản.
2. Dashboard tổng quan.
3. CRUD khách hàng.
4. CRUD sản phẩm.
5. Tạo và quản lý đơn hàng.
6. Quản lý công việc chăm sóc khách hàng.
7. Thống kê doanh thu cơ bản.

Các chức năng như gửi email tự động, thông báo nâng cao, xuất báo cáo nhiều định dạng và tích hợp AI có thể để ở giai đoạn mở rộng.

## 11. Tiêu chí kiểm thử gợi ý

- Người chưa đăng nhập không thể truy cập trang quản trị.
- Nhân viên không thể sử dụng chức năng chỉ dành cho Admin.
- Không cho lưu khách hàng nếu thiếu trường bắt buộc.
- Không cho tạo đơn với số lượng sản phẩm không hợp lệ.
- Tổng tiền đơn hàng phải khớp với tổng các dòng sản phẩm.
- Khi cập nhật trạng thái đơn hàng, dữ liệu phải được lưu chính xác.
- Tìm kiếm và bộ lọc phải trả về kết quả phù hợp.

## 12. Hướng phát triển trong tương lai

- Gửi email chăm sóc khách hàng.
- Tích hợp chatbot hỗ trợ.
- Gợi ý nhóm khách hàng cần chăm sóc.
- Tự động nhắc lịch cho nhân viên.
- Tích hợp nhiều chi nhánh.
- Phân tích xu hướng doanh thu.

---

**Kết luận:** SalesPro CRM là một đề tài website có tính ứng dụng thực tế, giúp người học thực hành thiết kế giao diện, xây dựng API, quản lý cơ sở dữ liệu, xác thực người dùng và phân quyền. Nên hoàn thành các chức năng cốt lõi trước khi phát triển tính năng nâng cao.
