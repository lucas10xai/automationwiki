---
publish: false
title: "Cài đặt n8n trên Instance EC2 Amazon Web Service"
tags: []
---

I. Mục tiêu
Sau khi hoàn thành bài học này, bạn sẽ có khả năng tự tay triển khai một
phiên bản n8n của riêng mình trên nền tảng đám mây Amazon Web
Services (AWS), một kỹ năng nền tảng để xây dựng các hệ thống tự động
hóa ổn định và có khả năng mở rộng.
● Về Kiến thức:
○ Nắm được EC2 trong AWS: Giải thích được vai trò của EC2
như một máy chủ ảo (Virtual Machine) chạy trên hạ tầng
đám mây của Amazon.
○ Hiểu rõ cách triển khai n8n trên EC2: Biết được lợi ích của
việc cài đặt n8n trên EC2 thay vì máy cục bộ, bao gồm tính
ổn định, khả năng mở rộng, và khả năng truy cập từ xa.
○ Nhận biết các thành phần liên quan: Hiểu rõ vai trò của
Security Group (tường lửa ảo), Elastic IP (IP tĩnh), và cách
cấu hình Port để n8n có thể được truy cập từ Internet.

● Về Kỹ năng:
○ Tạo và cấu hình EC2 Instance: Tự tay khởi tạo một máy chủ
ảo Ubuntu trên AWS EC2 và cấu hình bảo mật cơ bản (mở
port 22 cho SSH và 5678 cho n8n).
○ Cài đặt Docker: Thực hiện đầy đủ các bước cài đặt Docker
trên máy chủ Ubuntu để tạo môi trường container hóa.
○ Triển khai n8n: Sử dụng Docker để chạy container n8n một
cách nhanh chóng và hiệu quả.
○ Kết nối và kiểm thử: Truy cập vào giao diện n8n thông qua
địa chỉ IP công khai để xác nhận rằng quá trình cài đặt đã
thành công.

II. Chuẩn bị
● Tài khoản AWS: Bạn cần có một tài khoản AWS. Nếu chưa có, bạn
có thể đăng ký và tận dụng các dịch vụ trong gói Free Tier (miễn
phí) của Amazon.
● Slide trình chiếu: Các slide lý thuyết liên quan đến bài học.

III. Các Bước Cài Đặt
Bước 1: Tạo và Cấu hình EC2 Instance trên AWS
1. Đăng nhập vào AWS Management Console và tìm đến dịch vụ
EC2.
2. Nhấn vào nút "Launch instance".
3. Chọn Amazon Machine Image (AMI): Trong ô tìm kiếm, gõ
"Ubuntu" và chọn phiên bản Ubuntu Server mới nhất (thường nằm
trong gói Free Tier).
4. Chọn Instance Type: Chọn t2.micro vì nó đủ dùng cho việc học và
nằm trong gói Free Tier.
5. Tạo Key Pair:
○ Trong mục "Key pair (login)", nhấn "Create new key pair".
○ Đặt tên cho key pair (ví dụ: n8n-server-key), chọn định dạng
.pem và nhấn "Create key pair".
○ Trình duyệt sẽ tự động tải về một file .pem. Hãy lưu file này ở
một nơi an toàn, vì đây là chìa khóa duy nhất để bạn có thể
truy cập vào máy chủ.

6. Cấu hình Security Group (Tường lửa):
○ Trong mục "Network settings", nhấn "Edit".
○ Giữ lại quy tắc (rule) mặc định cho SSH (port 22).
○ Nhấn "Add security group rule" để thêm một quy tắc mới:
■ Type: Chọn Custom TCP.
■ Port Range: Gõ 5678 (đây là port mặc định của n8n).
■ Source type: Chọn Anywhere (0.0.0.0/0).

7. Nhấn "Launch instance" và chờ vài phút để AWS khởi tạo máy chủ
ảo của bạn.
Bước 2: Kết nối đến EC2 Instance qua SSH
8. Từ danh sách các Instance, chọn instance bạn vừa tạo và sao chép
địa chỉ Public IPv4 address.
9. Mở Terminal (trên macOS/Linux) hoặc Command
Prompt/PowerShell (trên Windows).
10. Di chuyển đến thư mục chứa file .pem bạn đã tải về.

11. Cấp quyền chỉ đọc cho file .pem (bước này rất quan trọng):
chmod 400 ten-file-cua-ban.pem
5. Sử dụng lệnh sau để kết nối, thay thế ten-file-cua-ban.pem và
<public_ip_address> bằng thông tin của bạn:

ssh -i "ten-file-cua-ban.pem" ubuntu@<public_ip_address>
Bước 3: Cài đặt Docker trên Server
1. Sau khi đã kết nối SSH thành công, hãy cập nhật danh sách các gói
phần mềm trên server:
sudo apt-get update
2. Thực hiện các bước cài đặt Docker theo hướng dẫn chính thức và
mới nhất từ trang chủ Docker tại đây: Install Docker Engine on
Ubuntu. Việc này đảm bảo bạn luôn có phiên bản ổn định và an
toàn nhất.
Bước 4: Triển khai n8n bằng Docker
Tạo một Docker Volume: Bước này để đảm bảo dữ liệu (workflows,
credentials) của bạn không bị mất mỗi khi container được khởi động lại.
3. Tạo một Docker Volume: Bước này để đảm bảo dữ liệu (workflows,
credentials) của bạn không bị mất mỗi khi container được khởi
động lại.
sudo docker volume create n8n_data
4. Khởi tạo container n8n: Chạy lệnh sau để tải image n8n về và khởi
chạy nó.
```
sudo docker run -d --name n8n \
-p 5678:5678 \
-v n8n_data:/home/node/.n8n \
docker.n8n.io/n8nio/n8n
```
Bước 5: Truy cập và Kiểm thử n8n
5. Mở trình duyệt web trên máy tính của bạn.

6. Trên thanh địa chỉ, gõ: http://<public_ip_address>:5678 (thay
<public_ip_address> bằng địa chỉ IP của EC2 Instance).
3. Nếu mọi thứ thành công, bạn sẽ thấy giao diện chào mừng và thiết
lập tài khoản quản trị của n8n.
4. Hoàn tất các bước thiết lập để bắt đầu sử dụng n8n trên máy chủ
của riêng bạn!
IV. Lưu ý quan trọng
● Bảo mật file .pem: Tuyệt đối không chia sẻ file này. Nếu mất file,
bạn sẽ không thể truy cập vào server của mình nữa.
● Volume trong Docker: Luôn sử dụng volume (-v
n8n_data:/home/node/.n8n) khi chạy n8n trong môi trường thực tế
để đảm bảo dữ liệu được lưu trữ bền vững.
● Security Group: Quy tắc cho phép truy cập từ "Anywhere"
(0.0.0.0/0) là để tiện cho việc học. Trong môi trường production,
bạn nên giới hạn chỉ cho phép truy cập từ các địa chỉ IP tin cậy.



---
**Bài trước:** [[2. Giới thiệu n8n và triết lý low-code]]
**Bài tiếp theo:** [[Quản lí Credential (Thông tin xác thực)]]
