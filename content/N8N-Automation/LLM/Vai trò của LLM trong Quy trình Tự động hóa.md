---
publish: false
title: "Vai trò của LLM trong Quy trình Tự động hóa"
tags: []
---

I. Lý thuyết
1.1. LLM là gì?
LLM (Large Language Model - Mô hình Ngôn ngữ Lớn) là một loại mô
hình Trí tuệ Nhân tạo (AI) được huấn luyện trên một khối lượng dữ liệu
văn bản khổng lồ.
● Mục tiêu: Hiểu và tạo ra ngôn ngữ tự nhiên giống như con người.
● Cách học: Về cơ bản, LLM học bằng cách dự đoán từ tiếp theo
trong một câu, dựa trên hàng tỷ ví dụ về ngữ cảnh mà nó đã được
học.
Khi tự động hóa truyền thống gặp AI, LLM trở thành yếu tố then chốt,
mang lại trí tuệ ngôn ngữ và mở rộng khả năng tự động hóa sang các
công việc đòi hỏi chuyên môn cao.
1.2. Vai trò của LLM trong tự động hóa
Hãy xem LLM là "bộ não" trung tâm của một hệ thống tự động hóa thông
minh.
5Trong khi tự động hóa truyền thống là "cơ bắp" thực thi các tác vụ
được lập trình sẵn, LLM cung cấp khả năng tự suy luận và xử lý các dữ
liệu phức tạp, đặc biệt là dữ liệu phi cấu trúc như văn bản, email, hay
phản hồi của khách hàng.
Các vai trò chính của LLM bao gồm:
● Hiểu dữ liệu phi cấu trúc: Đọc và hiểu ý nghĩa của email, bình luận,
văn bản.
● Sáng tạo nội dung tự động: Tự động viết email, báo cáo, tóm tắt
nội dung.
● Ra quyết định theo ngữ cảnh: Phân loại thông tin và quyết định
hành động tiếp theo dựa trên nội dung.
● Tự động hóa tác vụ chuyên môn: Hỗ trợ các công việc đòi hỏi kiến
thức chuyên ngành như phân tích dữ liệu hay viết mã.
II. Hướng Dẫn Workflow: Tự Động Phân Tích Phản Hồi Khách Hàng

Chúng ta sẽ xây dựng một workflow thực tế để tự động đọc phản hồi từ
Google Forms, dùng AI (Gemini) để phân loại cảm xúc, sau đó thực hiện
các hành động tương ứng.
2.1. Mục tiêu Workflow
Khi người dùng gửi một phản hồi qua Google Forms, workflow sẽ tự
động:
1. Đọc nội dung phản hồi.
2. Dùng LLM (Text Classifier) để phân loại phản hồi là "Tích cực" hay
"Tiêu cực".
3. Phân luồng:
○ Nếu là "Tích cực", tự động gửi một email cảm ơn đến khách
hàng.
○ Nếu là "Tiêu cực", lưu thông tin vào một file Google Sheets
riêng để đội ngũ có thể xem xét và xử lý.

2.2. Chuẩn bị
● Google Form: Một biểu mẫu để thu thập phản hồi với các trường:
Tên, Email, Sản phẩm, Ý kiến.
● Google Sheet (Đầu vào): Một trang tính được liên kết với Google
Form để nhận các câu trả lời.
● Google Sheet (Đầu ra): Một trang tính khác (hoặc một sheet khác
trong cùng file) để lưu các phản hồi tiêu cực.
● Credentials trong n8n: Đảm bảo bạn đã kết nối tài khoản Google
Sheets và Gmail.
● Gemini API Key: Cần có API Key từ Google AI Studio và đã tạo
credential cho Google Gemini trong n8n.
2.3. Xây dựng Workflow từng bước
Bước 1: Trigger - Bắt đầu khi có phản hồi mới
● Node: Google Sheets Trigger
● Mục đích: Kích hoạt workflow mỗi khi có một dòng mới được thêm
vào trang tính nhận phản hồi từ Google Form.

● Thực hiện:
1. Chọn tài khoản Google Sheets của bạn.
2. Trong trường Document, chọn file Google Sheet được liên kết
với Google Form.
3. Trong trường Sheet, chọn đúng sheet chứa các câu trả lời.
4. Mục Event để là Row Added.

Bước 2: "Bộ não" - Phân loại cảm xúc với LLM
● Node: Text Classifier và Google Gemini Chat Model
● Mục đích: Đọc trường "Ý kiến" và phân loại nó.
● Thực hiện:
1. Thêm node Text Classifier.
2. Kéo điểm nối Model của nó ra và chọn Google Gemini Chat
Model. Trong node Gemini, hãy chắc chắn bạn đã chọn đúng
credential chứa API Key của mình.
3. Quay lại node Text Classifier:
■ Input Text: Sử dụng expression để lấy dữ liệu từ trường
"Ý kiến": ={{ $json['Ý kiến'] }}.
■ Categories: Nhấn Add Category và tạo hai danh mục:
Tích cực và Tiêu cực.

Bước 3: Logic - Phân luồng xử lý
● Node: Switch
● Mục đích: Tạo ra các nhánh xử lý khác nhau dựa trên kết quả phân
loại của LLM.
● Thực hiện:
1. Thêm node Switch sau node Text Classifier.
2. Value to Switch On: Sử dụng expression để lấy kết quả phân
loại: ={{ $json.category }}.
3. Trong mục Routing Rules, tạo 2 quy tắc:
■ Rule 0: Operation is equal to, Value 2 là Tích cực.
■ Rule 1: Operation is equal to, Value 2 là Tiêu cực.

Bước 4: Hành động - Nhánh "Tích cực"
● Node: Gmail (Send a message)
● Mục đích: Tự động gửi email cảm ơn.
● Thực hiện:
1. Nối đầu ra của quy tắc "Tích cực" (output 0) từ node Switch
vào node Gmail.
2. Send To: Dùng expression để lấy email của người gửi: ={{
$json.Email }}.
3. Subject: Đặt tiêu đề, ví dụ: Cảm ơn bạn đã đóng góp ý kiến!.
4. Message: Soạn nội dung email cảm ơn.

Bước 5: Hành động - Nhánh "Tiêu cực"
● Node: Google Sheets (Append or update row)
● Mục đích: Lưu lại các phản hồi tiêu cực để theo dõi.
● Thực hiện:
1. Nối đầu ra của quy tắc "Tiêu cực" (output 1) từ node Switch
vào node Google Sheets.
2. Document và Sheet: Chọn đúng file và sheet bạn đã chuẩn bị
để lưu các phản hồi tiêu cực.
3. Trong mục Columns, ánh xạ các cột tương ứng:
■ Tên: ={{ $json['Tên'] }}
■ Sản phẩm: ={{ $json['Sản phẩm'] }}
■ Phản hồi: ={{ $json['Ý kiến'] }}

Sau khi hoàn tất, hãy lưu và kích hoạt (Active) workflow của bạn. Giờ đây,
mọi phản hồi từ khách hàng sẽ được xử lý một cách thông minh và tự
động.

---
**Bài trước:** [[Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary]]
**Quay lại:** [[N8N 101 - Mục lục]]