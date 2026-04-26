---
publish: false
title: "Trigger Nodes & Action trong App Nodes"
tags: []
---

I. Giới thiệu: Nền tảng của mọi Workflow
Trong n8n, mọi quy trình tự động hóa đều được xây dựng dựa trên hai
loại node nền tảng:
Trigger Nodes và Action in App Nodes. Việc hiểu rõ vai trò và cách hoạt
động của chúng là vô cùng quan trọng vì:
● Trigger Node là điểm khởi đầu, không có nó, workflow không thể
tự động kích hoạt.
● Action in App Node là các node thực thi, không có chúng,
workflow không thể thực hiện bất kỳ hành động nào như gửi email,
lưu dữ liệu hay thông báo.
Về cơ bản, một workflow là một chuỗi bắt đầu bằng một Trigger (Khi
điều kiện A xảy ra) và theo sau bởi một hoặc nhiều Actions (thì thực hiện
hành động B, C, D...).

II. Trigger Nodes - Node Khởi Đầu Workflow
Trigger Node luôn được đặt ở đầu một workflow, có nhiệm vụ xác định
sự kiện nào sẽ kích hoạt toàn bộ quy trình.
● Ví dụ: Khi có một đơn hàng mới được tạo trên website (đây là
Trigger), workflow sẽ được kích hoạt để tự động gửi email xác
nhận và lưu thông tin đơn hàng vào Google Sheets.
Dưới đây là các loại Trigger Node phổ biến nhất.
2.1. Webhook Trigger
● Định nghĩa: Kích hoạt workflow khi nhận được dữ liệu từ một hệ
thống bên ngoài gửi đến. Node này sẽ tạo ra một URL duy nhất để
các ứng dụng khác như website, form đăng ký, hoặc app di động
có thể gửi thông tin vào.
● Ví dụ: Một khách hàng điền form đăng ký trên website, thông tin
của họ sẽ được gửi đến URL của Webhook, từ đó kích hoạt

workflow để tự động lưu dữ liệu vào Google Sheets và gửi mail
cảm ơn.
2.2. Cron Trigger
● Định nghĩa: Kích hoạt workflow theo một lịch trình được định sẵn
một cách chính xác (theo giờ, ngày, tuần, tháng).
● Ví dụ:
○ Tự động gửi báo cáo doanh thu của ngày hôm trước vào lúc
8 giờ mỗi sáng.
○ Tự động chạy quy trình dọn dẹp và sao lưu dữ liệu vào 10 giờ
tối Chủ Nhật hàng tuần.

2.3. RSS Feed Reader Trigger
● Định nghĩa: Tự động theo dõi nội dung mới từ một trang web hoặc
blog thông qua RSS feed. Workflow sẽ được kích hoạt mỗi khi có
một bài viết mới được xuất bản.
● Ví dụ: Khi một blog tin tức ra bài mới, workflow sẽ tự động lấy link
bài viết và gửi thông báo vào một nhóm chat Telegram.
2.4. Interval Trigger
● Định nghĩa: Kích hoạt workflow để kiểm tra một dịch vụ bên ngoài
một cách định kỳ theo một khoảng thời gian nhất định (ví dụ: mỗi
5 phút, mỗi 1 giờ). Điểm khác biệt với Cron là nó không chạy vào
một thời điểm chính xác mà lặp lại sau mỗi khoảng thời gian.
● Ví dụ: Cứ mỗi 5 phút, workflow sẽ kiểm tra API của một đơn vị vận
chuyển để xem trạng thái đơn hàng đã được cập nhật hay chưa.

III. Action in App Nodes - Node Thực Thi Hành Động
Sau khi Trigger được kích hoạt, workflow cần thực hiện các hành động
cụ thể. Các hành động này được thực hiện bởi các
Action in App Nodes.
● Đặc điểm:

○ Làm việc và tương tác với các ứng dụng bên ngoài như
Google, Telegram, Notion, Slack, v.v.
○ Thường yêu cầu kết nối tài khoản (xác thực) để có quyền
truy cập.
○ Một workflow có thể có nhiều Action Node nối tiếp nhau sau
một Trigger.

Dưới đây là một số Action Node phổ biến và các thao tác chính của
chúng.
3.1. Google Sheets Node
● Mục đích: Đọc, ghi và cập nhật dữ liệu trong Google Sheets.
● Thao tác chính:
○ Read: Đọc dữ liệu từ một sheet.
○ Append: Thêm một hoặc nhiều dòng mới vào cuối sheet.
○ Update: Tìm một dòng dựa trên điều kiện và cập nhật lại dữ
liệu cho dòng đó.

● Ví dụ:
○ Ghi thông tin khách hàng mới từ form đăng ký vào Google
Sheets.
○ Cập nhật trạng thái đơn hàng từ "Đang xử lý" thành "Đã giao"
trong bảng theo dõi.

3.2. Telegram Node
● Mục đích: Gửi tin nhắn đến một người dùng, một nhóm, hoặc một
kênh trên Telegram.
● Yêu cầu: Cần có Bot Token và Chat ID để hoạt động.
● Ví dụ:
○ Gửi thông báo khẩn cấp cho đội ngũ kỹ thuật khi hệ thống
phát hiện lỗi.
○ Gửi cập nhật tiến độ công việc hàng ngày cho nhóm dự án.

3.3. Gmail Node
● Mục đích: Tự động hóa việc gửi email.

● Ví dụ: Khi một khách hàng hoàn tất mua hàng, hệ thống tự động
gửi một email cảm ơn kèm theo hóa đơn chi tiết.
3.4. Notion Node
● Mục đích: Tương tác với cơ sở dữ liệu (database) trong Notion để
quản lý công việc, ghi chú, lưu trữ thông tin.
● Thao tác chính:
○ Create Record: Tạo một trang (dòng) mới trong database.
○ Update Record: Chỉnh sửa một trang đã có.
○ Search Record: Tìm kiếm các trang dựa trên điều kiện lọc.
● Ví dụ:
○ Tự động thêm một học viên mới vào database quản lý danh
sách lớp học.
○ Tự động tạo một task mới trong bảng quản lý công việc khi
có email yêu cầu từ khách hàng.

3.5. ChatGPT Node
● Mục đích: Tích hợp trí tuệ nhân tạo (AI) vào workflow để sinh nội
dung, tóm tắt văn bản, phân loại dữ liệu, hoặc trả lời câu hỏi.
● Thao tác chính:
○ Chat: Gửi một prompt (câu lệnh) và nhận lại phản hồi.
○ Completion: Yêu cầu AI tạo ra một đoạn nội dung dài hơn.
○ Moderation: Kiểm tra xem nội dung có vi phạm các quy tắc
an toàn hay không.

● Ví dụ:
○ Tự động tạo nội dung email phản hồi cho khách hàng dựa
trên thông tin họ cung cấp trong form liên hệ.
○ Tự động tóm tắt nội dung một bài báo dài và gửi bản tóm tắt
qua email.
---
**Bài tiếp theo:** [[Core Nodes & Nguyên tắc Dataflow trong n8n]]




