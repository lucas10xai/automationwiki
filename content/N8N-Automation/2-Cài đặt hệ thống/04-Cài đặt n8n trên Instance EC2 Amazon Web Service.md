---
title: "Cài đặt n8n trên Instance EC2 Amazon Web Service"
tags: [n8n, deployment, aws, ec2, docker]
publish: true
---

> [!nav] Điều hướng
> **Tới trang chủ:** [[index|Wiki N8N Automation]]
> **Bài trước:** [[03-Cài đặt n8n Self-host qua Docker]]
> **Bài tiếp theo:** [[05-Cài đặt n8n trên Instance Raspberry Pi]]


![Cover Image](https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80)

# Cài đặt n8n trên Instance EC2 Amazon Web Service

> [!info] Mục tiêu
> Bài học này hướng dẫn bạn tự tay triển khai một phiên bản n8n của riêng mình trên nền tảng đám mây Amazon Web Services (AWS) EC2. Đây là một kỹ năng nền tảng để xây dựng các hệ thống tự động hóa ổn định và có khả năng mở rộng.

---

## 1. Kiến thức nền tảng
- **EC2 trong AWS**: EC2 đóng vai trò như một máy chủ ảo (Virtual Machine) chạy trên hạ tầng đám mây của Amazon.
- **Triển khai n8n trên EC2**: Mang lại tính ổn định, khả năng mở rộng và dễ dàng truy cập từ xa 24/7 so với việc cài đặt trên máy cục bộ.
- **Thành phần liên quan**: Hiểu rõ vai trò của Security Group (tường lửa ảo), Elastic IP (IP tĩnh), và cách cấu hình Port để n8n có thể được truy cập từ Internet một cách an toàn.

---

## 2. Chuẩn bị

- **Tài khoản AWS**: Bạn cần có một tài khoản AWS. Nếu chưa có, bạn có thể đăng ký và tận dụng các dịch vụ trong gói Free Tier (miễn phí) của Amazon để thực hành.

---

## 3. Các Bước Cài Đặt

### Bước 1: Tạo và Cấu hình EC2 Instance trên AWS
1. Đăng nhập vào AWS Management Console và tìm đến dịch vụ **EC2**.
2. Nhấn vào nút **Launch instance**.
3. **Chọn Amazon Machine Image (AMI)**: Trong ô tìm kiếm, gõ "Ubuntu" và chọn phiên bản Ubuntu Server mới nhất (thường nằm trong gói Free Tier).
4. **Chọn Instance Type**: Chọn `t2.micro` (đủ dùng cho việc học và nằm trong gói Free Tier).
5. **Tạo Key Pair**:
    - Trong mục "Key pair (login)", nhấn **Create new key pair**.
    - Đặt tên cho key pair (ví dụ: `n8n-server-key`), chọn định dạng `.pem` và nhấn **Create key pair**.
    - Trình duyệt sẽ tự động tải về một file `.pem`. Hãy lưu file này ở một nơi an toàn, vì đây là chìa khóa duy nhất để bạn có thể truy cập vào máy chủ qua SSH.
6. **Cấu hình Security Group (Tường lửa)**:
    - Trong mục "Network settings", nhấn **Edit**.
    - Giữ lại quy tắc (rule) mặc định cho SSH (port `22`).
    - Nhấn **Add security group rule** để thêm một quy tắc mới:
        - **Type**: Chọn Custom TCP.
        - **Port Range**: Gõ `5678` (đây là port mặc định của n8n).
        - **Source type**: Chọn Anywhere (`0.0.0.0/0`).
7. Nhấn **Launch instance** và chờ vài phút để AWS khởi tạo máy chủ ảo của bạn.

### Bước 2: Kết nối đến EC2 Instance qua SSH
1. Từ danh sách các Instance, chọn instance bạn vừa tạo và sao chép địa chỉ **Public IPv4 address**.
2. Mở Terminal (trên macOS/Linux) hoặc Command Prompt/PowerShell (trên Windows).
3. Di chuyển đến thư mục chứa file `.pem` bạn đã tải về.
4. Cấp quyền chỉ đọc cho file `.pem` (bước này rất quan trọng):
```bash
chmod 400 ten-file-cua-ban.pem
```
5. Sử dụng lệnh sau để kết nối, thay thế `ten-file-cua-ban.pem` và `<public_ip_address>` bằng thông tin của bạn:
```bash
ssh -i "ten-file-cua-ban.pem" ubuntu@<public_ip_address>
```

### Bước 3: Cài đặt Docker trên Server
1. Sau khi đã kết nối SSH thành công, hãy cập nhật danh sách các gói phần mềm trên server:
```bash
sudo apt-get update
```
2. Thực hiện các bước cài đặt Docker. Bạn có thể sử dụng script cài đặt tự động từ Docker để đảm bảo luôn có phiên bản ổn định nhất:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Bước 4: Triển khai n8n bằng Docker
1. **Tạo một Docker Volume**: Đảm bảo dữ liệu (workflows, credentials) của bạn không bị mất mỗi khi container được khởi động lại.
```bash
sudo docker volume create n8n_data
```
2. **Khởi tạo container n8n**: Chạy lệnh sau để tải image n8n về và khởi chạy nó (chạy ngầm).
```bash
sudo docker run -d --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

### Bước 5: Truy cập và Kiểm thử n8n
1. Mở trình duyệt web trên máy tính của bạn.
2. Trên thanh địa chỉ, gõ: `http://<public_ip_address>:5678` (thay `<public_ip_address>` bằng địa chỉ IP của EC2 Instance).
3. Nếu mọi thứ thành công, bạn sẽ thấy giao diện chào mừng và thiết lập tài khoản quản trị ban đầu của n8n.
4. Hoàn tất các bước thiết lập để bắt đầu sử dụng n8n trên máy chủ đám mây của riêng bạn!

---

## 4. Lưu ý quan trọng

> [!warning] Bảo mật & Quản lý dữ liệu
> - **Bảo mật file `.pem`**: Tuyệt đối không chia sẻ file này. Nếu mất file, bạn sẽ không thể truy cập vào server của mình nữa.
> - **Volume trong Docker**: Luôn sử dụng volume (`-v n8n_data:/home/node/.n8n`) khi chạy n8n trong môi trường thực tế để đảm bảo dữ liệu được lưu trữ bền vững kể cả khi xóa container.
> - **Security Group**: Quy tắc cho phép truy cập từ "Anywhere" (`0.0.0.0/0`) là để tiện cho việc học. Trong môi trường production, bạn nên giới hạn chỉ cho phép truy cập từ các địa chỉ IP tin cậy, hoặc sử dụng Reverse Proxy (Nginx, Traefik, Caddy) kèm SSL để tăng cường bảo mật.

---

> [!nav] Điều hướng
> **Bài trước:** [[03-Cài đặt n8n Self-host qua Docker]]
> **Bài tiếp theo:** [[05-Cài đặt n8n trên Instance Raspberry Pi]]
