---
title: Phân biệt Trigger Node và Action Node
tags:
  - n8n
  - nodes
  - trigger
  - action
  - basic
publish: false
---

> [!nav] Điều hướng
> **Bài trước:** [[09-Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary]]
> **Bài tiếp theo:** [[07-Trigger Nodes & Action trong App Nodes]]


![Cover Image](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&q=80)

> [!info] Mục tiêu bài học
> Chào mừng bạn đến với bài học về các thành phần cốt lõi của n8n! Mục tiêu chính của buổi học này là giúp bạn hiểu và phân biệt rõ ràng hai viên gạch nền tảng xây dựng nên mọi quy trình tự động hóa: **Trigger Node** và **Action Node**.
> 
> Sau khi hoàn thành bài học, bạn sẽ có khả năng:
> - **Hiểu rõ khái niệm Workflow**: Nắm được định nghĩa, chức năng và các thành phần cấu tạo nên một workflow.
> - **Xác định vai trò của Trigger Node**: Giải thích được Trigger Node là gì, chức năng của nó và cách nhận dạng.
> - **Xác định vai trò của Action Node**: Giải thích được Action Node là gì, chức năng và cách nhận dạng.
> - **So sánh và phân biệt**: Tự tin chỉ ra những điểm khác biệt cốt lõi giữa hai loại node này, làm nền tảng cho việc xây dựng các workflow phức tạp.

---

## 1. Workflow là gì?

Trước khi đi vào chi tiết hai loại Node chính, chúng ta cần hiểu rõ khái niệm bao trùm: **Workflow**.

- **Khái niệm**: Một workflow là một chuỗi các bước tự động hóa được kết nối với nhau để thực hiện một tác vụ từ đầu đến cuối. Hãy hình dung nó như một chuỗi hiệu ứng domino: khi quân domino đầu tiên (Trigger) bị đẩy, nó sẽ kích hoạt một chuỗi các hành động (Actions) kế tiếp diễn ra theo một trật tự đã được định sẵn.
- **Chức năng**: Workflow cung cấp một hệ thống có cấu trúc rõ ràng, giúp chuẩn hóa các bước thực hiện, theo dõi tiến độ và đảm bảo công việc luôn diễn ra một cách suôn sẻ và nhất quán.
- **Thành phần**: Mọi workflow trong n8n đều được xây dựng từ hai thành phần cơ bản:
    - **Trigger Node**
    - **Action Node**

---

## 2. Trigger Node - "Người Gác Cổng"

### 2.1. Khái niệm
**Trigger Node** là điểm bắt đầu duy nhất của mọi workflow. Nó quyết định **KHI NÀO** và **TẠI SAO** workflow được kích hoạt.
Hãy tưởng tượng Trigger Node như một "người gác cổng" hoặc một cảm biến. Nó không làm gì cả cho đến khi một sự kiện cụ thể xảy ra. Nó luôn đứng ở vị trí đầu tiên và không thể có bất kỳ node nào kết nối vào đầu vào của nó.

### 2.2. Chức năng
Chức năng chính của Trigger Node là "lắng nghe" các sự kiện. Ví dụ:
- **Lên lịch trình (Cron Trigger)**: Kích hoạt workflow vào một thời điểm cố định (ví dụ: 9 giờ sáng mỗi ngày).
- **Nhận thư (Email Trigger)**: Kích hoạt khi có email mới đến một địa chỉ xác định.
- **Nhận dữ liệu (Webhook Trigger)**: Kích hoạt khi một ứng dụng khác gửi dữ liệu đến một URL đặc biệt.
- **Báo lỗi (Error Trigger)**: Kích hoạt khi một workflow khác gặp lỗi.

### 2.3. Đặc điểm nhận dạng
- **Vị trí & Số lượng**: Luôn là node đầu tiên của workflow và chỉ có một Trigger Node (đóng vai trò bắt đầu một luồng) trong đa số các trường hợp đơn giản.
- **Luồng dữ liệu**: Chỉ có "đầu ra" để truyền dữ liệu về sự kiện đã kích hoạt nó, **không có "đầu vào"** từ các node khác.
- **Sự kiện kích hoạt**: Nó chỉ hoạt động khi có một sự kiện cụ thể xảy ra. Ví dụ, khi một tin nhắn mới được nhận trong chat (Chat Trigger).

---

## 3. Action Node - "Người Thực Thi"

### 3.1. Khái niệm
**Action Node** là các bước thực thi tác vụ sau khi workflow đã được kích hoạt bởi Trigger Node. Nó trả lời cho câu hỏi: "Sau khi được kích hoạt, workflow cần **LÀM GÌ**?".
Nếu Trigger Node là "người gác cổng" ra hiệu lệnh, thì các Action Node chính là những "người thực thi" cần mẫn thực hiện từng công đoạn của nhiệm vụ.

### 3.2. Chức năng
Mỗi Action Node nhận dữ liệu từ node trước đó, thực hiện một hành động cụ thể, và sau đó chuyển kết quả cho node tiếp theo.
*Ví dụ một chuỗi Action Node:*
1. **Action 1**: Lấy thông tin khách hàng từ đơn hàng mới (*Google Sheets Node*).
2. **Action 2**: Thêm thông tin khách hàng đó vào hệ thống CRM (*HubSpot Node*).
3. **Action 3**: Gửi một email cảm ơn đến khách hàng (*Gmail Node*).

### 3.3. Đặc điểm nhận dạng
- **Vị trí & Số lượng**: Luôn đứng sau Trigger Node hoặc một Action Node khác. Có thể có nhiều Action Node trong một workflow và chúng được kết nối nối tiếp hoặc song song với nhau.
- **Luồng dữ liệu**: Hoạt động hai chiều, vừa có "đầu vào" để nhận dữ liệu, vừa có "đầu ra" để gửi dữ liệu đi sau khi đã xử lý.

---

## 4. So sánh và Tổng kết

### 4.1. Bảng so sánh

| Tiêu chí | Trigger Node | Action Node |
| :--- | :--- | :--- |
| **Mục đích** | Trả lời câu hỏi: "Khi nào workflow bắt đầu?" | Trả lời câu hỏi: "Làm gì sau khi bắt đầu?" |
| **Vị trí** | Luôn đứng đầu tiên của luồng thực thi | Đứng sau Trigger hoặc Action Node khác |
| **Số lượng** | Ít (Thường là một điểm kích hoạt chính) | Có thể có nhiều, liên kết thành chuỗi |
| **Luồng dữ liệu** | Chỉ gửi dữ liệu đi (chỉ có **đầu ra**) | Nhận dữ liệu vào và gửi đi (có **đầu vào** và **đầu ra**) |
| **Ví dụ** | Webhook, Cron, Email Trigger, Tally Trigger | Google Sheets, Slack, HTTP Request, Gmail |

### 4.2. Ý nghĩa
Hiểu rõ sự khác biệt giữa Trigger Node và Action Node là chìa khóa để thiết kế các quy trình tự động hóa logic và hiệu quả. Trigger Node quyết định **"điểm khởi đầu"**, trong khi chuỗi Action Node quyết định **"lộ trình"** mà dữ liệu sẽ đi và những gì sẽ xảy ra trên lộ trình đó.

> [!check] Tổng kết
> Qua bài học hôm nay, chúng ta đã phân biệt rõ ràng hai thành phần cơ bản của một workflow:
> - **Trigger Node (Người Gác Cổng)**: Khởi tạo hoặc kích hoạt quy trình tự động hóa. Nó luôn là node duy nhất và đứng đầu tiên.
> - **Action Node (Người Thực Thi)**: Thực hiện các nhiệm vụ hoặc hành động cụ thể trong quy trình. Nó là các node đứng sau Trigger và có thể có nhiều.
> 
> Nắm vững hai khái niệm này sẽ giúp bạn tự tin hơn trong việc đọc, hiểu và xây dựng các workflow của riêng mình.

---

> [!nav] Điều hướng
> **Bài trước:** [[09-Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary]]
> **Bài tiếp theo:** [[07-Trigger Nodes & Action trong App Nodes]]
