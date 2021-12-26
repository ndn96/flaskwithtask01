# A. Mục tiêu của Module này là:
## 1. Build giúp lưu lại các biểu quyết hoặc vote hoặc điểm danh vào 1 file.
## 2. Chỉ những người có MSV(Mã sinh viên) + CMND được cấp từ trước mới được quyền tạo vote.
## 3. Hiển thị các lựa chọn để vote.
## 4. Hiển thị danh sách người đã vote gồm những ai.
## 5. Thống kê số lượng top các vote và giá trị tương ứng.Ví dụ vote nhiều nhất là ai?Thấp nhất là ai.Tốp 3-5 là gồm những ai.
## 6. Người nào đã vote,sẽ không thể vote tiếp.
## 7. 

# B. Đặc tả của Module này:
## 0. Có các biến môi trường:
### 0.1 Nên đặt biến môi trường là ROUTE_PATH_API = '/api/v1/'
## 1. Route (đường dẫn): ROUTE_PATH_API+/vote/{id}/:

## 2. Set thời hạn truy cập 1 vote id nào đó theo time limit.
### 2.1 Sau time này,sẽ không thể vote nữa mà thay vào đó là hiện thông báo vote đã hết hạn.
# C. Hướng dẫn sử dụng code dự án này:
## 1. Vui lòng clone về local
## 2. Sau đó cài đặt các biến môi trường với pip như venv,flask.