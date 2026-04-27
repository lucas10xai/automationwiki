---
title: "Cài đặt n8n Self-host qua Docker"
tags: [n8n, docker, self-host, deployment]
publish: true
---

> [!nav] Điều hướng
> **Tới trang chủ:** [[index|Wiki N8N Automation]]
> **Bài trước:** [[index|🏠 Wiki N8N - Trang chủ]]
> **Bài tiếp theo:** [[04-Cài đặt n8n trên Instance EC2 Amazon Web Service]]


![Cover Image](https://images.unsplash.com/photo-1605745341112-85968b19335b?w=1200&q=80)

# Cài đặt n8n Self-host qua Docker

## 1. Mục tiêu & Giới thiệu
**Mục tiêu chính:** Bài học này sẽ hướng dẫn bạn từng bước cài đặt và vận hành phiên bản n8n self-host (tự quản lý) trên máy tính cá nhân của mình bằng Docker. 

Kết thúc bài lab, bạn sẽ có một "trạm điều khiển" tự động hóa mạnh mẽ, hoàn toàn thuộc quyền sở hữu của bạn, sẵn sàng để xây dựng bất kỳ quy trình làm việc nào mà không gặp giới hạn.

---

## 2. Chuẩn bị (Trang bị "Nền tảng" cho n8n)
Trước khi xây dựng "trạm điều khiển", chúng ta cần chuẩn bị môi trường và các công cụ cần thiết.

### 2.1. Lợi ích chính của việc Self-host n8n
- **Toàn quyền kiểm soát dữ liệu:** Toàn bộ thông tin nhạy cảm như credentials, API keys và lịch sử thực thi (logs) đều được lưu trữ trên máy chủ của bạn, không phải trên một nền tảng bên thứ ba.
- **Không giới hạn:** Phá vỡ mọi rào cản về số lượng workflow, số bước trong workflow và số lần thực thi thường thấy ở các gói miễn phí trên cloud.
- **Tùy chỉnh nâng cao:** Cho phép bạn tinh chỉnh sâu hơn về các biến môi trường, cấu hình và tích hợp các tính năng mà phiên bản cloud không hỗ trợ.
- **Tiết kiệm chi phí:** Về lâu dài, self-host có thể tiết kiệm đáng kể chi phí so với việc trả phí cho các gói dịch vụ cloud, đặc biệt khi bạn có nhu cầu tự động hóa cao.

### 2.2. Yêu cầu cần có
- **Hệ điều hành:** Windows 10/11 (khuyến nghị kích hoạt WSL 2), macOS, hoặc Linux.
- **Phần mềm bắt buộc:** Docker Desktop đã được cài đặt và đang ở trạng thái hoạt động (Running).
  - *Link tải chính thức:* [Docker: Accelerated Container Application Development](https://www.docker.com/)

### 2.3. Kiểm tra trạng thái Docker
Sau khi cài đặt, hãy mở Terminal (trên macOS/Linux) hoặc PowerShell (trên Windows) và chạy các lệnh sau để đảm bảo Docker đã sẵn sàng:

**Kiểm tra Docker có đang chạy không:**
```bash
docker info
```
- *Kết quả mong đợi:* Hiển thị một loạt thông tin hệ thống của Docker (phiên bản, số container, số image...).
- *Nếu gặp lỗi:* `Cannot connect to the Docker daemon`, nghĩa là Docker Desktop chưa được khởi động.

**Kiểm tra phiên bản:**
```bash
docker --version
```

**Liệt kê tất cả container đã có (kể cả đã dừng):**
```bash
docker ps -a
```

---

## 3. Cài đặt n8n với Docker
Chúng ta có hai phương pháp: sử dụng giao diện đồ họa của Docker Desktop (đơn giản, nhanh gọn) hoặc sử dụng dòng lệnh với Docker Compose (mạnh mẽ, dễ quản lý hơn).

### 3.1. Phương pháp 1: Qua Docker Desktop (Giao diện đồ họa)
Đây là cách dễ dàng nhất cho người mới bắt đầu.
1. Mở ứng dụng Docker Desktop.
2. Trên thanh tìm kiếm ở đầu trang, gõ `n8nio/n8n` và nhấn Enter.
3. Ở kết quả, nhấn nút **Pull** để tải image về máy. Sau khi tải xong, nút này sẽ chuyển thành **Run**.
4. Nhấn nút **Run**. Một cửa sổ tùy chọn sẽ hiện ra. Bạn có thể đặt tên cho container và quan trọng nhất là cấu hình **Port** (ví dụ: `5678`), sau đó nhấn Run.

### 3.2. Phương pháp 2: Qua Terminal với Docker Compose (Khuyên dùng)
Phương pháp này mang lại khả năng kiểm soát cao hơn và đảm bảo dữ liệu của bạn được lưu trữ bền vững.

**Bước 1: Tạo thư mục lưu trữ dữ liệu**
Đây là bước cực kỳ quan trọng để đảm bảo workflows và credentials của bạn không bị mất khi container bị xóa hoặc tạo lại.

Trên Windows (dùng PowerShell):
```powershell
mkdir C:\n8n-data
cd C:\n8n-data
```

Trên macOS/Ubuntu (dùng Terminal):
```bash
mkdir ~/n8n-data
cd ~/n8n-data
```

**Bước 2: Tạo file cấu hình docker-compose.yml**
Trong thư mục `n8n-data` bạn vừa tạo, hãy tạo một file mới tên là `docker-compose.yml` và dán nội dung sau vào:

```yaml
version: '3.7'

services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "127.0.0.1:5678:5678"
    volumes:
      - ./n8n_local_data:/home/node/.n8n
```

> [!info] Giải thích các thông số chính:
> - `image: n8nio/n8n`: Sử dụng image Docker chính thức và mới nhất của n8n.
> - `restart: always`: Tự động khởi động lại container n8n nếu nó bị dừng đột ngột.
> - `ports: "127.0.0.1:5678:5678"`: Ánh xạ cổng 5678 bên trong container ra cổng 5678 trên localhost của bạn (đảm bảo bảo mật).
> - `volumes: ./n8n_local_data:/home/node/.n8n`: Ánh xạ thư mục `n8n_local_data` với thư mục dữ liệu bên trong container. Toàn bộ workflows sẽ được lưu tại đây.

**Bước 3: Khởi chạy n8n**
Vẫn trong Terminal/PowerShell tại thư mục `n8n-data`, chạy lệnh sau:
```bash
docker-compose up -d
```
Lệnh này sẽ đọc file `docker-compose.yml`, tải image n8n (nếu chưa có) và khởi chạy container trong chế độ nền (`-d`). Trên Docker Desktop bạn có thể thấy 1 container đã được tạo ra.

---

## 4. Truy cập và Quản lý n8n
### 4.1. Truy cập n8n lần đầu
- Mở trình duyệt web của bạn và truy cập địa chỉ: `http://localhost:5678`
- Lần đầu tiên, n8n sẽ yêu cầu bạn thiết lập tài khoản quản trị (Owner account). Hãy điền thông tin và hoàn tất quá trình.

### 4.2. Xác nhận dữ liệu được lưu trữ đúng cách
- Quay lại thư mục `n8n-data` trên máy tính của bạn.
- Bạn sẽ thấy một thư mục con mới có tên `n8n_local_data` được tự động tạo ra. Bên trong thư mục này là các file cấu hình và SQLite database. Đây là bằng chứng cho thấy dữ liệu của bạn đang được backup an toàn.

### 4.3. Các lệnh quản lý thiết yếu
Để quản lý n8n, bạn luôn chạy các lệnh này từ bên trong thư mục `n8n-data`.

- **Dừng n8n:** `docker-compose down`
- **Khởi động lại:** `docker-compose restart`
- **Xem logs (để tìm lỗi):** `docker-compose logs -f n8n`
- **Cập nhật phiên bản n8n mới nhất:**
  ```bash
  docker-compose pull n8n
  docker-compose up -d
  ```

---

## 5. Khắc phục sự cố & Lưu ý quan trọng
> [!warning] Khắc phục sự cố thường gặp
> - **Lỗi Cổng (Port Conflict):** Nếu cổng 5678 đã được sử dụng, hãy đổi cổng trong file `docker-compose.yml`. Ví dụ: đổi thành `127.0.0.1:5679:5678`. Sau đó truy cập `http://localhost:5679`.
> - **Lỗi Quyền ghi (Permission Denied) trên Linux/macOS:** Đôi khi Docker không có quyền ghi vào thư mục volumes. Giải pháp thường là cấp quyền sở hữu thư mục cho người dùng hiện tại: `sudo chown $(whoami) -R ~/n8n-data`.
> - **Container không khởi động:** Nếu bạn không thể truy cập n8n, hãy dùng lệnh `docker-compose logs n8n` để đọc thông báo lỗi chi tiết.
> - **Lưu ý quan trọng nhất:** Luôn đảm bảo rằng dòng `volumes` trong file `docker-compose.yml` được cấu hình chính xác. Nếu không, toàn bộ công sức xây dựng workflow của bạn sẽ biến mất khi container bị xóa.

---

> [!nav] Điều hướng
> **Bài trước:** [[index|🏠 Wiki N8N - Trang chủ]]
> **Bài tiếp theo:** [[04-Cài đặt n8n trên Instance EC2 Amazon Web Service]]
