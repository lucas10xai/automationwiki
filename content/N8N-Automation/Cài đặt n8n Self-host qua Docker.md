---
publish: false
title: "Cài đặt n8n Self-host qua Docker"
tags: []
---

I. Mục tiêu & Giới thiệu
● Mục tiêu chính: Bài học này sẽ hướng dẫn bạn từng bước cài đặt
và vận hành phiên bản n8n self-host (tự quản lý) trên máy tính cá
nhân của mình bằng Docker. Kết thúc bài lab, bạn sẽ có một "trạm
điều khiển" tự động hóa mạnh mẽ, hoàn toàn thuộc quyền sở hữu
của bạn, sẵn sàng để xây dựng bất kỳ quy trình làm việc nào mà
không gặp giới hạn.
II. Chuẩn bị (Trang bị "Nền tảng" cho n8n)
Trước khi xây dựng "trạm điều khiển", chúng ta cần chuẩn bị môi trường
và các công cụ cần thiết.
2.1. Lợi ích chính của việc Self-host n8n
● Toàn quyền kiểm soát dữ liệu: Toàn bộ thông tin nhạy cảm như
credentials, API keys và lịch sử thực thi (logs) đều được lưu trữ
trên máy chủ của bạn, không phải trên một nền tảng bên thứ ba.
● Không giới hạn: Phá vỡ mọi rào cản về số lượng workflow, số bước
trong workflow và số lần thực thi thường thấy ở các gói miễn phí
trên cloud.
● Tùy chỉnh nâng cao: Cho phép bạn tinh chỉnh sâu hơn về các biến
môi trường, cấu hình và tích hợp các tính năng mà phiên bản cloud
không hỗ trợ.
● Tiết kiệm chi phí: Về lâu dài, self-host có thể tiết kiệm đáng kể chi
phí so với việc trả phí cho các gói dịch vụ cloud, đặc biệt khi bạn có
nhu cầu tự động hóa cao.
2.2. Yêu cầu cần có
● Hệ điều hành: Windows 10/11 (khuyến nghị kích hoạt WSL 2) hoặc
macOS.
● Phần mềm bắt buộc: Docker Desktop đã được cài đặt và đang ở
trạng thái hoạt động (Running).

○ Link tải chính thức: Docker: Accelerated Container
Application Development
2.3. Kiểm tra trạng thái Docker
Sau khi cài đặt, hãy mở Terminal (trên macOS) hoặc PowerShell (trên
Windows) và chạy các lệnh sau để đảm bảo Docker đã sẵn sàng:
Kiểm tra Docker có đang chạy không:
docker info

○ Kết quả mong đợi: Hiển thị một loạt thông tin hệ thống của
Docker (phiên bản, số container, số image...).
○ Nếu gặp lỗi: Cannot connect to the Docker daemon, nghĩa là
Docker Desktop chưa được khởi động.

● Khi thành công chạy docker

Kiểm tra phiên bản:
docker --version

○ Kết quả mong đợi: Hiển thị phiên bản Docker bạn đang cài, ví
dụ: Docker version 20.10.17.

Liệt kê tất cả container đã có (kể cả đã dừng):
docker ps -a

III. Cài đặt n8n với Docker
Chúng ta có hai phương pháp: sử dụng giao diện đồ họa của Docker
Desktop (đơn giản, nhanh gọn) hoặc sử dụng dòng lệnh với Docker
Compose (mạnh mẽ, dễ quản lý hơn).
3.1. Phương pháp 1: Cài đặt nhanh qua Docker Desktop (Giao diện đồ
họa)
Đây là cách dễ dàng nhất cho người mới bắt đầu.
● Bước 1: Mở ứng dụng Docker Desktop.
● Bước 2: Trên thanh tìm kiếm ở đầu trang, gõ n8nio/n8n và nhấn
Enter.
● Bước 3: Ở kết quả, nhấn nút Pull để tải image về máy. Sau khi tải
xong, nút này sẽ chuyển thành Run.
● Bước 4: Nhấn nút Run. Một cửa sổ tùy chọn sẽ hiện ra. Bạn có thể
đặt tên cho container và quan trọng nhất là cấu hình Port, sau đó
nhấn Run.
3.2. Phương pháp 2: Cài đặt qua Terminal với Docker Compose
Phương pháp này mang lại khả năng kiểm soát cao hơn và đảm bảo dữ
liệu của bạn được lưu trữ bền vững.
Bước 1: Tạo thư mục lưu trữ dữ liệu
Đây là bước cực kỳ quan trọng để đảm bảo workflows và credentials của
bạn không bị mất khi container bị xóa hoặc tạo lại.
Trên Windows (dùng PowerShell):
mkdir C:\n8n-data
cd C:\n8n-data

Trên macOS/Ubuntu (dùng Terminal):
mkdir ~/n8n-data
cd ~/n8n-data
Bước 2: Tạo file cấu hình docker-compose.yml
Trong thư mục n8n-data bạn vừa tạo, hãy tạo một file mới tên là
docker-compose.yml và dán nội dung sau vào:
version: '3.7'

services:
n8n:
image: n8nio/n8n
restart: always
ports:
- "127.0.0.1:5678:5678"
volumes:
- ./n8n_local_data:/home/node/.n8n

● Giải thích các thông số chính:
○ image: n8nio/n8n: Sử dụng image Docker chính thức và mới
nhất của n8n.
○ restart: always: Tự động khởi động lại container n8n nếu nó
bị dừng đột ngột (ví dụ: do khởi động lại máy tính).
○ ports: - "127.0.0.1:5678:5678": Ánh xạ cổng 5678 bên trong
container ra cổng 5678 trên máy của bạn. 127.0.0.1
(localhost) đảm bảo chỉ có bạn mới truy cập được, tăng tính
bảo mật.
○ volumes: - ./n8n_local_data:/home/node/.n8n: Đây là phần
quan trọng nhất. Nó ánh xạ thư mục n8n_local_data (sẽ được
tự động tạo bên trong thư mục n8n-data của bạn) với thư
mục dữ liệu bên trong container. Toàn bộ workflows và
credentials sẽ được lưu tại đây.

Bước 3: Khởi chạy n8n
Vẫn trong Terminal/PowerShell tại thư mục n8n-data, chạy lệnh sau:
docker-compose up -d

Trên docker desktop bạn có thể thấy 1 container đã được tạo ra

Lệnh này sẽ đọc file docker-compose.yml, tải image n8n (nếu chưa có)
và khởi chạy container trong chế độ nền (-d).
IV. Truy cập và Quản lý n8n
4.1. Truy cập n8n lần đầu
● Mở trình duyệt web của bạn và truy cập địa chỉ:
http://localhost:5678
● Lần đầu tiên, n8n sẽ yêu cầu bạn thiết lập tài khoản quản trị
(Owner account). Hãy điền thông tin và hoàn tất quá trình.
4.2. Xác nhận dữ liệu được lưu trữ đúng cách
● Quay lại thư mục n8n-data trên máy tính của bạn.
● Bạn sẽ thấy một thư mục con mới có tên n8n_local_data được tự
động tạo ra. Bên trong thư mục này là các file cấu hình và cơ sở dữ
liệu. Đây là bằng chứng cho thấy dữ liệu của bạn đang được lưu trữ
bền vững bên ngoài container.
4.3. Các lệnh quản lý thiết yếu
Để quản lý n8n, bạn luôn chạy các lệnh này từ bên trong thư mục
n8n-data.
● Dừng n8n:
docker-compose down

● Khởi động lại:
docker-compose restart

● Xem logs (để tìm lỗi):
docker-compose logs -f n8n

● Cập nhật phiên bản n8n mới nhất:
docker-compose pull n8n

docker-compose up -d

V. Khắc phục sự cố & Lưu ý quan trọng
Lỗi Cổng (Port Conflict): Nếu bạn nhận được thông báo lỗi rằng cổng
5678 đã được sử dụng, đơn giản hãy đổi cổng trong file
docker-compose.yml. Ví dụ, đổi thành 5679:
ports:
- "127.0.0.1:5679:5678"
● Sau đó lưu file và chạy lại docker-compose up -d. Bạn sẽ truy cập
n8n tại http://localhost:5679.
● Lỗi Quyền ghi (Permission Denied) trên Linux/macOS: Đôi khi
Docker không có quyền ghi vào thư mục volumes bạn đã tạo. Đây
là một vấn đề nâng cao, nhưng giải pháp thường liên quan đến việc
cấp quyền sở hữu thư mục cho người dùng hiện tại (sudo chown
$(whoami) -R ~/n8n-data).
● Container không khởi động: Nếu bạn không thể truy cập n8n, hãy
dùng lệnh docker-compose logs n8n để đọc thông báo lỗi chi tiết.
Đây là bước đầu tiên và quan trọng nhất để chẩn đoán vấn đề.
● Lưu ý quan trọng nhất: Luôn đảm bảo rằng dòng volumes trong file
docker-compose.yml của bạn được cấu hình chính xác. Nếu không,
toàn bộ công sức xây dựng workflow của bạn sẽ biến mất khi
container bị xóa. 
---
**Bài trước:** [[2. Giới thiệu n8n và triết lý low-code]]
**Bài tiếp theo:** [[Quản lí Credential (Thông tin xác thực)]]
