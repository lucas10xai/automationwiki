---
title: "Cài đặt n8n trên Instance Raspberry Pi"
tags: [n8n, deployment, raspberry-pi, npm]
publish: true
---

> [!nav] Điều hướng
> **Tới trang chủ:** [[index|Wiki N8N Automation]]
> **Bài trước:** [[04-Cài đặt n8n trên Instance EC2 Amazon Web Service]]
> **Bài tiếp theo:** [[06-Phân biệt Trigger Node và Action Node]]


![Cover Image](https://images.unsplash.com/photo-1555661530-68c8e98db4e6?w=1200&q=80)

# Cài đặt n8n trên Instance Raspberry Pi

> [!info] Mục tiêu
> Bài học này hướng dẫn bạn biến một chiếc máy tính nhỏ gọn Raspberry Pi thành một máy chủ tự động hóa mạnh mẽ bằng cách cài đặt trực tiếp n8n lên đó thông qua `npm`. 
> 
> Sau bài học, bạn sẽ có một hệ thống n8n hoạt động 24/7 với chi phí điện năng tối thiểu, lý tưởng cho các dự án tự động hóa trong nhà hoặc văn phòng nhỏ.

---

## 1. Giới thiệu

Raspberry Pi là một máy tính đơn board giá rẻ, nổi tiếng với kích thước nhỏ gọn và khả năng tùy biến cao. Thay vì sử dụng Docker như các bài học trước, lần này chúng ta sẽ thực hiện một phương pháp cài đặt khác: **cài đặt n8n trực tiếp lên hệ điều hành thông qua npm (Node Package Manager)**. 

Cách tiếp cận này giúp bạn hiểu sâu hơn về môi trường hoạt động của n8n, vì n8n về cơ bản là một ứng dụng được xây dựng trên nền tảng Node.js.

---

## 2. Chuẩn bị

Để bắt đầu, bạn cần chuẩn bị các phần cứng và phần mềm sau:

- **Phần cứng**:
    - **Raspberry Pi 4 hoặc 5**: Khuyến nghị phiên bản có RAM từ 4GB trở lên để n8n chạy mượt mà.
    - **Thẻ nhớ microSD**: Dung lượng tối thiểu 16GB, class 10 hoặc cao hơn.
    - Nguồn điện phù hợp cho Raspberry Pi.
    - *(Tùy chọn cho lần cài đặt đầu tiên)*: Màn hình, bàn phím, chuột và dây cáp HDMI/micro-HDMI.
- **Phần mềm**:
    - **Hệ điều hành Raspberry Pi OS**: Sẽ được ghi (flash) lên thẻ nhớ.
    - **Kết nối mạng**: Dây LAN hoặc kết nối Wi-Fi.

---

## 3. Các bước cài đặt

### Bước 1: Cài đặt Hệ điều hành Raspberry Pi OS
1. Sử dụng công cụ **Raspberry Pi Imager** trên máy tính của bạn để ghi (flash) hệ điều hành Raspberry Pi OS lên thẻ nhớ microSD.
2. Trong quá trình cài đặt, hãy thiết lập tên người dùng, mật khẩu và quan trọng nhất là **bật chế độ SSH** trong phần cấu hình nâng cao. Việc này cho phép bạn điều khiển Raspberry Pi từ xa mà không cần đến màn hình và bàn phím.

### Bước 2: Kết nối đến Raspberry Pi qua SSH
1. Sau khi cài đặt xong, cắm thẻ nhớ vào Raspberry Pi, kết nối mạng và cấp nguồn.
2. Tìm địa chỉ IP nội bộ của Raspberry Pi (bạn có thể tìm trong trang quản trị của router/modem).
3. Mở Terminal (macOS/Linux) hoặc PowerShell (Windows) và kết nối bằng lệnh sau:
```bash
ssh ten_nguoi_dung@<raspberry_pi_ip>
```

### Bước 3: Cài đặt Node.js và npm
n8n cần môi trường Node.js để hoạt động. Chúng ta sẽ cài đặt phiên bản 18 LTS (hoặc 20 LTS) được khuyến nghị.

1. Chạy lần lượt các lệnh sau trong cửa sổ SSH của Raspberry Pi:
```bash
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```
2. Kiểm tra để chắc chắn rằng Node.js và npm đã được cài đặt thành công:
```bash
node -v
npm -v
```
*(Kết quả mong đợi: Bạn sẽ thấy số phiên bản của Node.js như `v18.x.x` và phiên bản của npm).*

### Bước 4: Cài đặt n8n bằng npm
Bây giờ, chúng ta sẽ cài đặt n8n như một gói phần mềm toàn cục trên hệ thống.

1. Chạy lệnh cài đặt toàn cục (`-g` là global):
```bash
sudo npm install -g n8n
```

### Bước 5: Khởi chạy và Truy cập n8n
1. **Lấy địa chỉ IP nội bộ**: Nếu bạn quên địa chỉ IP của Pi, hãy chạy lệnh `ifconfig` để xem lại.
2. **Cấu hình biến môi trường**: Để cho phép n8n chấp nhận kết nối qua HTTP trong mạng nội bộ, hãy chạy lệnh sau:
```bash
export N8N_SECURE_COOKIE=false
```
3. **Khởi chạy n8n**:
```bash
n8n
```
4. **Truy cập n8n**: Mở trình duyệt trên một máy tính khác trong cùng mạng LAN và truy cập vào địa chỉ:
```text
http://<dia_chi_ip_cua_pi>:5678
```
*(Nếu thành công, bạn sẽ thấy giao diện thiết lập tài khoản quản trị của n8n).*

---

## 4. Lưu ý quan trọng

> [!warning] Chú ý về Cấu hình và Mạng
> - **Phiên bản Node.js**: Hãy chắc chắn bạn cài đặt đúng phiên bản Node.js được khuyến nghị (ví dụ 18 LTS hoặc 20 LTS) để đảm bảo n8n hoạt động ổn định.
> - **Biến môi trường**: Lệnh `export N8N_SECURE_COOKIE=false` chỉ có tác dụng trong phiên terminal hiện tại. Để n8n luôn khởi động với cấu hình này, bạn cần thêm dòng lệnh đó vào file cấu hình của shell (ví dụ: `~/.bashrc` hoặc `~/.profile`).
> - **Truy cập từ mạng LAN**: Phương pháp cài đặt này lý tưởng cho việc sử dụng n8n trong mạng nội bộ. Việc public n8n ra ngoài internet đòi hỏi các bước cấu hình bảo mật nâng cao hơn (sử dụng domain, SSL, reverse proxy). Để duy trì service chạy 24/7, bạn có thể thiết lập `pm2` để quản lý tiến trình n8n.

---

> [!nav] Điều hướng
> **Bài trước:** [[04-Cài đặt n8n trên Instance EC2 Amazon Web Service]]
> **Bài tiếp theo:** [[06-Phân biệt Trigger Node và Action Node]]
