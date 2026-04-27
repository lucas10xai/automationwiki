---
title: "Quản lý Credential (Thông tin xác thực)"
tags: [n8n, credentials, security, authentication]
publish: true
---

> [!nav] Điều hướng
> **Tới trang chủ:** [[index|Wiki N8N Automation]]
> **Bài trước:** [[10-Data Transformation & Flow Control Nodes trong n8n]]
> **Bài tiếp theo:** Trở về [[index|Mục lục chính]]


![Cover Image](https://images.unsplash.com/photo-1614064641913-6b7140414c71?w=1200&q=80)

# Quản lý Credential (Thông tin xác thực)

> [!info] Mục tiêu bài học
> Chào mừng bạn đến với bài học về bảo mật và kết nối trong n8n! Mục tiêu chính của buổi học này là giúp bạn hiểu rõ về **Credential** - khái niệm không thể thiếu khi làm việc với các dịch vụ bên ngoài. 
> 
> Sau khi hoàn thành bài học, bạn sẽ có khả năng:
> - **Hiểu rõ Credential là gì**: Nắm vững định nghĩa, vai trò và tầm quan trọng của Credential trong việc kết nối an toàn.
> - **Biết khi nào cần sử dụng**: Nhận diện được các trường hợp bắt buộc phải thiết lập Credential để workflow có thể hoạt động.
> - **Nắm vững lợi ích**: Hiểu được các lợi ích của việc quản lý Credential tập trung, như tái sử dụng và dễ dàng bảo trì.
> - **Thực hành thiết lập**: Tự tin thực hiện các bước thiết lập một Credential OAuth 2.0 với một dịch vụ phổ biến như Google Drive.
> 
> Hãy cùng nhau tìm hiểu cách tạo ra những "chiếc chìa khóa" an toàn để mở ra cánh cửa kết nối vô tận cho workflow của bạn!

---

## 1. Credential là gì? - "Chìa khóa" cho Workflow

### 1.1. Giới thiệu và Định nghĩa
Trong n8n, **Credential** đóng vai trò như những chiếc chìa khóa giúp workflow kết nối và tương tác an toàn với các dịch vụ bên ngoài. Đây là một phần không thể thiếu để tự động hóa các tác vụ liên quan đến API, tài khoản, và cơ sở dữ liệu.

- **Hiểu đơn giản**: Credential chính là chiếc chìa khóa mà n8n dùng để "mở cửa" và làm việc an toàn với các ứng dụng khác như Google Sheets, Slack, hay Gmail.
- **Về mặt kỹ thuật**: Credential là một bộ thông tin xác thực được lưu trữ an toàn, chứa các chi tiết nhạy cảm như:
    - API keys
    - Username và Password
    - Token (ví dụ: Token OAuth)

Mục tiêu của Credential là vừa bảo mật thông tin nhạy cảm, vừa cho phép workflow tương tác liền mạch với các ứng dụng khác.

---

## 2. Khi nào cần thiết lập Credential?

### 2.1. Các trường hợp cần thiết lập
Bạn sẽ cần thiết lập Credential bất cứ khi nào workflow của bạn cần "chứng minh danh tính" để truy cập một hệ thống bên ngoài. Cụ thể:
- **Kết nối với dịch vụ bên ngoài**: Khi bạn muốn workflow đọc/ghi dữ liệu từ Google Sheets, gửi tin nhắn tới Slack, hay gửi mail bằng Gmail.
- **Tự động hóa tác vụ cần "đăng nhập"**: Ví dụ như tự động tải file lên Google Drive cá nhân của bạn.
- **Sử dụng API của bên thứ ba**: Khi bạn dùng node HTTP Request để gọi đến một API yêu cầu xác thực bằng API Key hoặc Token.
- **Truy cập Cơ sở dữ liệu**: Để đọc hoặc ghi dữ liệu từ các hệ quản trị cơ sở dữ liệu như PostgreSQL, MySQL, v.v.

### 2.2. Lợi ích của việc quản lý Credential
Quản lý Credential tập trung trong n8n mang lại nhiều lợi ích:
- **Tái sử dụng**: Bạn chỉ cần tạo Credential một lần và có thể dùng lại trên nhiều workflow khác nhau.
- **Quản lý an toàn**: Tất cả thông tin nhạy cảm được quản lý tập trung tại một nơi duy nhất, rất an toàn và tiện lợi.
- **Dễ dàng cập nhật và bảo trì**: Khi mật khẩu hay API key thay đổi, bạn chỉ cần cập nhật ở một nơi duy nhất, tất cả các workflow sử dụng nó sẽ tự động được áp dụng theo.

---

## 3. Hướng dẫn thiết lập Credential (Ví dụ với Google Drive)

Chúng ta sẽ thực hành thiết lập Credential cho Google Drive, một ứng dụng rất phổ biến.

### 3.1. Các thuật ngữ quan trọng
Trước khi bắt đầu, hãy làm quen với một số khái niệm cơ bản, đặc biệt là với phương thức xác thực OAuth 2.0:
- **OAuth (Open Authorization)**: Giao thức ủy quyền an toàn để n8n có thể truy cập tài nguyên của bạn trên một dịch vụ khác mà không cần biết mật khẩu của bạn.
- **Client ID**: Mã định danh duy nhất cho ứng dụng của bạn (trong trường hợp này là n8n).
- **Client Secret**: Một "mật khẩu" bí mật, chỉ ứng dụng của bạn và dịch vụ (Google) biết.
- **Authorized Redirect URL**: URL mà Google sẽ chuyển hướng bạn về lại n8n sau khi bạn cấp quyền thành công.

*Trong đó, Client ID và Client Secret là hai thông tin quan trọng nhất bạn cần lấy từ Google để cung cấp cho n8n.*

### 3.2. Quy trình thiết lập từng bước
Quy trình này gồm 2 giai đoạn chính: lấy thông tin xác thực từ Google Cloud và cấu hình trên n8n.

#### Giai đoạn 1: Trên Google Cloud Platform
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/) và tạo một **New Project**. Đây là nơi quản lý tất cả các kết nối API của bạn.
2. Trên thanh menu bên trái, vào **APIs & Services** > **Library**.
3. Tìm kiếm "Google Drive API" và nhấn **Enable** để kích hoạt.
4. Sau khi kích hoạt, quay lại menu bên trái, chọn **Credentials**.
5. Nhấn **+ Create credentials** và chọn **OAuth client ID**.
6. Nếu được yêu cầu, nhấn **Configure Consent Screen**. Chọn **External** và điền các thông tin cần thiết. Sau đó quay lại bước tạo Credentials.
7. Trong phần "Application type", chọn **Web application**.
8. Trong phần "Authorized redirect URIs", nhấn **+ Add URI**.

#### Giai đoạn 2: Trên n8n và hoàn tất
1. Mở n8n, thêm node **Google Drive**. Trong mục "Credential", chọn **Create New**.
2. Một cửa sổ mới hiện ra, hãy sao chép (copy) dòng **OAuth Redirect URL**.
3. Quay lại trang Google Cloud, dán URL bạn vừa copy vào ô "Authorized redirect URIs" ở bước 8 phía trên. Nhấn **Create**.
4. Google Cloud sẽ hiển thị cho bạn **Your Client ID** và **Your Client Secret**. Hãy sao chép cả hai thông tin này.
5. Quay lại cửa sổ thiết lập Credential của n8n, dán Client ID và Client Secret vào các ô tương ứng.
6. Nhấn nút **Sign in with Google** và đăng nhập bằng tài khoản Google bạn đã dùng để thiết lập.
7. Bạn có thể thấy màn hình "Google hasn't verified this app". Nhấn **Nâng cao** và chọn đi tới để tiếp tục. Cấp các quyền được yêu cầu.
8. Nếu trang web báo "Account connected", bạn đã thiết lập thành công!

---

## 4. Tổng kết & Lưu ý

> [!check] Tổng kết
> - **Vai trò**: Credential là "chìa khóa xác thực" để n8n được cấp quyền truy cập vào các ứng dụng khác.
> - **Khi nào cần**: Khi kết nối với bất kỳ dịch vụ bên ngoài nào yêu cầu xác thực.
> - **Lợi ích**: Tạo một lần, dùng nhiều lần và dễ dàng bảo trì.
> - **Lưu ý quan trọng**: Client ID và Client Secret là những thông tin cực kỳ nhạy cảm. Tuyệt đối không chia sẻ chúng cho bất kỳ ai để đảm bảo an toàn bảo mật.

---

> [!nav] Điều hướng
> **Bài trước:** [[10-Data Transformation & Flow Control Nodes trong n8n]]
> **Bài tiếp theo:** Trở về [[index|Mục lục chính]]
