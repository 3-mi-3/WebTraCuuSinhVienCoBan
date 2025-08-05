# WEB TRA CỨU SINH VIÊN CƠ BẢN
## Giới thiệu
Project bao gồm 2 ứng dụng web:
* App 1: Thêm, sửa, xóa, hiển thị danh sách, tìm kiếm sinh viên
* App 2: Gọi API từ App 1 để tìm kiếm thông tin sinh viên theo mã
## Công nghệ và thuật toán sử dụng
* Python Flask – Backend xử lý server
* HTML + Bootstrap – Giao diện người dùng
* Firebase: lưu trữ CSDL
## Giao diện minh họa
**Giao diện App 1**
<img width="1359" height="621" alt="image" src="https://github.com/user-attachments/assets/a656ffb6-c79b-4d8f-8e68-305e0ca1173b" />
**Giao diện App 2**
<img width="1361" height="626" alt="image" src="https://github.com/user-attachments/assets/326517f6-23b6-4e84-818c-d86d6625da47" />
## Hướng dẫn cài đặt
**Yêu cầu:**
* Python 3.10 trở lên
* Các thư viện: flask, firebase-admin, requests
* File cấu hình Firebase: qlsinhvien-6204c-firebase-adminsdk-xxx.json hoặc file tương ứng từ Firebase project của bạn

**Cài đặt:**
1. Clone repo: git clone https://github.com/your-username/WebTraCuuSinhVienCoBan.git
2. Tạo Firebase Project của bạn và tải về file Firebase .json, thay thế đường dẫn file vào dòng `cred = credentials.Certificate("qlsinhvien-6204c-firebase-adminsdk-fbsvc-35ea0603be.json")` trong file app1.py
3. Cài thư viện: `pip install flask firebase-admin requests`
4. Chạy server: python app1.py và app2.py
5. Mở trình duyệt và truy cập: http://localhost:5000 cho App 1 và http://localhost:5001 cho App 2
