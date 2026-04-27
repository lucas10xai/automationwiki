---
title: "Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary"
tags: [n8n, data-format, json, binary, dataflow]
publish: true
---

> [!nav] Điều hướng
> **Tới trang chủ:** [[index|Wiki N8N Automation]]
> **Bài trước:** [[08-Core Nodes & Nguyên tắc Dataflow trong n8n]]
> **Bài tiếp theo:** [[10-Data Transformation & Flow Control Nodes trong n8n]]


![Cover Image](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&q=80)

# Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary

> [!info] Mục tiêu bài học
> Chào mừng bạn đến với bài học tìm hiểu về "nguyên liệu" cốt lõi của mọi workflow!
> 
> Mục tiêu chính của buổi học này là giúp bạn hiểu rõ hai định dạng dữ liệu cơ bản mà n8n sử dụng để vận hành: **JSON** và **Binary**. Sau khi hoàn thành bài học, bạn sẽ có khả năng:
> - **Hiểu rõ về JSON:** Nắm vững khái niệm, vai trò, cấu trúc và cách sử dụng Expressions để tham chiếu, lấy dữ liệu từ JSON.
> - **Hiểu rõ về Binary:** Nắm vững khái niệm, vai trò của dữ liệu Binary (dữ liệu file) và các quy trình xử lý chính trong workflow.
> - **Phân biệt được hai định dạng:** Nhận biết và phân biệt rõ ràng bản chất, cách đọc và cách xử lý của JSON so với Binary.
> 
> Việc nắm vững cách dữ liệu được cấu trúc và luân chuyển sẽ giúp bạn làm chủ hoàn toàn các quy trình tự động hóa của mình.

---

## 1. JSON - "Ngôn ngữ giao tiếp" của các Node

### 1.1. Khái niệm
**JSON** (viết tắt của *JavaScript Object Notation*) là một định dạng dữ liệu văn bản gọn nhẹ, dễ đọc cho người và dễ phân tích cho máy. Nó được xây dựng dựa trên các cặp "thuộc tính - giá trị" (hay "key - value").

### 1.2. Vai trò và Cấu trúc
- **Vai trò:** Trong n8n, JSON là định dạng dữ liệu chính để lưu trữ và vận chuyển thông tin có cấu trúc giữa các node. Hãy coi nó như ngôn ngữ chung mà tất cả các node sử dụng để "nói chuyện" và trao đổi thông tin với nhau.
- **Cấu trúc:**
	- **Đối tượng (Object):** Được bao bọc bởi cặp dấu ngoặc nhọn `{}`. Một đối tượng chứa một tập hợp các cặp key-value.
	- **Mảng (Array):** Được bao bọc bởi cặp dấu ngoặc vuông `[]`. Một mảng chứa một danh sách các giá trị.
	- **Cặp Key-Value:** Dữ liệu được tổ chức theo các cặp `"key": "value"`. Key luôn là một chuỗi văn bản đặt trong dấu ngoặc kép `""`.

### 1.3. Cách "đọc" dữ liệu JSON (Expressions)
Để lấy thông tin từ một khối dữ liệu JSON, chúng ta sử dụng **Expressions**.

- **Cú pháp:** Mọi expression trong n8n đều được đặt trong cặp dấu ngoặc kép và ngoặc nhọn `{{ }}`.
- **Cách sử dụng:** Chúng bản dùng ký pháp dấu chấm (`.`) để truy cập vào các cấp dữ liệu.

> [!example] Ví dụ:
> Giả sử bạn có một cấu trúc JSON về đơn hàng:
> - **Lấy mã đơn hàng:**
>   `{{ $json.orderId }}`
> - **Lấy email của khách hàng:**
>   `{{ $json.customer.email }}`
> - **Lấy tên của sản phẩm đầu tiên trong danh sách:**
>   `{{ $json.items[0].itemName }}` *(Lưu ý: phần tử đầu tiên trong mảng có chỉ số là 0).*

---

## 2. Binary - "Hành lý" của Workflow

### 2.1. Khái niệm
Dữ liệu **Binary** trong n8n đại diện cho bất kỳ loại file nào, chẳng hạn như ảnh (`.jpg`, `.png`), tài liệu (`.pdf`, `.docx`), file nén (`.zip`), hoặc video (`.mp4`). Đây không phải là văn bản có thể đọc trực tiếp, mà là dữ liệu thô tạo nên một file hoàn chỉnh.

### 2.2. Vai trò
Dữ liệu Binary đóng vai trò thiết yếu trong việc lưu trữ và truyền tải mọi loại thông tin trong máy tính. Trong n8n, vai trò chính của nó là cho phép bạn xử lý các file trong workflow của mình.

### 2.3. Các thao tác xử lý dữ liệu Binary
Bạn có thể xử lý các file (dữ liệu Binary) theo ba cách chính:

1. **Tải file lên workflow:** Dùng node `Read Binary File` để đọc một file từ máy tính của bạn, hoặc dùng `HTTP Request` để tải một file từ một URL.
2. **Lưu file từ workflow:** Dùng node `Write Binary File` để lưu một file đang có trong workflow xuống máy tính.
3. **Chuyển tiếp file:** Gửi file như một file đính kèm trong email (ví dụ: `Gmail` node) hoặc gửi qua các ứng dụng chat (ví dụ: `Slack`, `Telegram` node).

> [!warning] Cách n8n "mô tả" dữ liệu Binary
> Đây là một điểm quan trọng cần lưu ý: Khi một file được xử lý, n8n sẽ hiển thị một đối tượng JSON chứa thông tin mô tả (metadata) về file đó, chứ **không hiển thị nội dung thô** của file.
> 
> Thông thường, nội dung file sẽ được mã hóa dưới dạng một chuỗi văn bản dài (Base64) và được đặt vào một trường trong đối tượng JSON đó.

---

## 3. Tổng kết

Hiểu rõ hai định dạng dữ liệu này là điều kiện tiên quyết để làm chủ n8n. Dưới đây là những điểm khác biệt cốt lõi:

| Tiêu chí | JSON | Binary |
| :--- | :--- | :--- |
| **Bản chất** | Văn bản có cấu trúc | Dữ liệu thô của file |
| **Khả năng đọc** | Có thể đọc trực tiếp | Không thể đọc trực tiếp |
| **Cách xử lý** | Dùng Expressions để "đọc" và lấy từng phần thông tin | Dùng các node hành động chuyên dụng (như `Read/Write Binary File`) để xử lý toàn bộ file |

---

> [!nav] Điều hướng
> **Bài trước:** [[08-Core Nodes & Nguyên tắc Dataflow trong n8n]]
> **Bài tiếp theo:** [[10-Data Transformation & Flow Control Nodes trong n8n]]
