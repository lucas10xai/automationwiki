---
publish: false
title: "Data Transformation & Flow Control Nodes trong n8n"
tags: []
---

I. Giới thiệu
Trong bài học này, chúng ta sẽ khám phá hai nhóm node cốt lõi và mạnh
mẽ nhất trong n8n: Data Transformation Nodes (Node Biến đổi Dữ liệu)
và Flow Control Nodes (Node Điều khiển Luồng). Nắm vững các node
này sẽ cho phép bạn xử lý mọi loại dữ liệu đầu vào và xây dựng các quy
trình tự động hóa phức tạp, thông minh và hiệu quả.

II. Data Transformation Nodes - Node Biến Đổi Dữ Liệu
Data Transformation Nodes là nhóm các công cụ cho phép bạn làm
sạch, sửa đổi, và tái cấu trúc dữ liệu để nó sẵn sàng cho các bước xử lý
tiếp theo trong workflow.
2.1. Set Node
● Mục đích: Set Node là công cụ cơ bản và mạnh mẽ nhất để thao
tác dữ liệu ở cấp độ từng item (từng mục dữ liệu). Hãy nghĩ về nó
như một con dao đa năng: bạn có thể dùng nó để thêm một
trường dữ liệu mới, sửa một trường có sẵn, hoặc xóa những
trường không cần thiết.
● Chức năng chính:
○ Add Field (Thêm trường): Dùng khi bạn muốn gán thêm một
"nhãn" hay một "thông tin" mới cho dữ liệu.
○ Set Value (Thiết lập giá trị): Khi thông tin có sẵn bị sai hoặc
cần định dạng lại. Đây là lúc bạn sẽ dùng đến các "công
thức" đặc biệt gọi là Expressions.
○ Rename Keys (Đổi tên trường): Sử dụng khi tên trường dữ
liệu từ nguồn vào không khớp với tên trường mà hệ thống
đích yêu cầu.
○ Keep Only Set (Chỉ giữ lại các trường đã chọn): Khi được
bật, node sẽ chỉ giữ lại những trường bạn đã định nghĩa
trong Set Node và xóa tất cả các trường còn lại.

● Ví dụ thực tế:
Bạn có dữ liệu khách hàng với các trường "Họ tên", "Số điện thoại".
Bạn muốn chuẩn hóa lại dữ liệu này bằng Set Node:

○ Đổi tên trường "Họ tên" thành "Customer Name".
○ Thêm trường "Ngày tạo" với giá trị là ngày hiện tại.

2.2. Function Node
● Mục đích: Khi các thao tác đơn giản của Set Node là không đủ,
Function Node cho phép bạn viết mã JavaScript tùy chỉnh để thực
hiện các logic biến đổi dữ liệu phức tạp.
● Chức năng chính:
○ Xử lý mảng và object lồng nhau: Dùng để "bóc tách" và truy
cập dữ liệu bị giấu sâu trong các cấu trúc phức tạp.
○ Tính toán phức tạp: Thực hiện các phép tính trên toàn bộ
danh sách dữ liệu cùng lúc, thay vì xử lý từng cái một.
○ Validation dữ liệu với nhiều điều kiện: Tạo ra các bộ lọc
"thông minh" để kiểm tra dữ liệu với nhiều quy tắc lồng vào
nhau.
○ Xử lý chuỗi và định dạng phức tạp: Giúp bạn "nhào nặn" và
biến đổi văn bản theo bất kỳ cách nào bạn muốn.

● Ví dụ thực tế: Xử lý một danh sách đơn hàng, Function Node có
thể được dùng để:
○ Tính tổng tiền (total_amount) từ các thành phần con.
○ Gán độ ưu tiên (priority) là 'high' nếu tổng tiền > 100.
○ Làm sạch và chuẩn hóa tên khách hàng (customer_name).

2.3. Split In Batches Node
● Mục đích: Dùng để chia một tập dữ liệu lớn thành nhiều "lô" (batch)
nhỏ hơn để xử lý tuần tự.
● Khi nào sử dụng:
○ Xử lý dữ liệu lớn: Khi có hàng ngàn mục cần xử lý, việc chia
nhỏ giúp workflow chạy ổn định, không bị chậm hoặc treo. Ví
dụ: Gửi 1.000 email bằng cách chia thành các lô 50 email để
không bị đánh dấu là spam.
○ Làm việc với API: Hầu hết các dịch vụ đều giới hạn số lượng
yêu cầu bạn có thể gửi trong một phút. Chia lô giúp bạn tuân

thủ giới hạn này và không bị chặn truy cập. Ví dụ: Lấy thông
tin 500 sản phẩm bằng cách chia thành các lô 10 sản phẩm.

III. Flow Control Nodes - Node Điều Khiển Luồng Dữ Liệu
Flow Control Nodes là nhóm các công cụ giúp bạn điều khiển luồng đi
của dữ liệu trong workflow, cho phép bạn tạo ra các nhánh xử lý khác
nhau và quyết định dữ liệu nào được đi tiếp.
3.1. If Node
● Mục đích: Hoạt động như một câu lệnh "Nếu... thì...", cho phép bạn
kiểm tra một điều kiện đơn giản và phân luồng dữ liệu thành hai
hướng: Đúng (true) hoặc Sai (false).
● Khi nào sử dụng:
○ Khi cần kiểm tra một điều kiện đơn giản (ví dụ: số lượng >
10, trạng thái = "completed").
○ Khi muốn phân chia luồng xử lý thành hai hướng riêng biệt.
○ Khi cần kiểm tra (validate) dữ liệu trước khi xử lý bước tiếp
theo.

● Ví dụ: Phân loại đơn hàng VIP. Nếu Đơn hàng > 1 triệu (Đúng) ->
Gửi quà tặng. Nếu (Sai) -> Xử lý bình thường.
3.2. Switch Node
● Mục đích: Là phiên bản nâng cao của If Node, cho phép bạn phân
loại và định tuyến dữ liệu vào nhiều hơn hai nhánh dựa trên giá trị
của một trường dữ liệu.
● Khi nào sử dụng:
○ Khi cần phân loại dữ liệu thành nhiều nhóm (hơn hai nhóm).
○ Khi mỗi loại dữ liệu cần một quy trình xử lý khác nhau.
○ Để thay thế cho việc phải nối nhiều If Node phức tạp.
● Ví dụ: Xử lý đơn hàng dựa trên trạng thái của chúng:
○ Nếu trạng thái là "Pending" -> Nhánh 1: Gửi email xác nhận.
○ Nếu trạng thái là "Shipped" -> Nhánh 2: Gửi mã vận đơn.
○ Nếu trạng thái là "Cancelled" -> Nhánh 3: Hủy đơn trong hệ
thống.

3.3. Merge Node
● Mục đích: Dùng để gộp (hợp nhất) dữ liệu từ các nhánh xử lý riêng
biệt trở lại thành một luồng duy nhất.
● Chế độ hoạt động:
○ Append: Nối dữ liệu từ các nhánh lại với nhau thành một
danh sách dài.
○ Combine: Ghép dữ liệu của các item liên quan từ các nhánh
khác nhau dựa trên một trường chung (ví dụ: ID đơn hàng).
○ Choose Branch: Chỉ ưu tiên lấy dữ liệu từ một nhánh nhất
định nếu có.

● Ví dụ: Gộp báo cáo doanh thu từ 3 nhánh (Website, Cửa hàng,
App) thành một danh sách tổng hợp duy nhất để phân tích.
IV. Workflow Thực Tế: Xử Lý Đơn Hàng Tự Động
● Mục tiêu: Xây dựng một quy trình tự động nhận dữ liệu đơn hàng,
tính toán, làm sạch, phân loại theo trạng thái, và chuẩn hóa dữ liệu
để chuẩn bị cho các bước xử lý cuối cùng.
● Phân tích Workflow:
○ Data Transformation Nodes:
■ Code Node: Dùng để tính toán tổng tiền cho mỗi đơn
hàng và gán độ ưu tiên (priority) dựa trên giá trị đơn
hàng.
■ Set Node (Edit Fields): Dùng để bổ sung các "chỉ dẫn"
xử lý cho từng loại đơn hàng sau khi được phân loại.

○ Flow Control Nodes:
■ Switch Node: Phân luồng các đơn hàng dựa trên trạng
thái của chúng (ví dụ: pending, shipped).
■ Merge Node: Sau khi mỗi luồng được xử lý riêng,
Merge Node sẽ hợp nhất tất cả các đơn hàng lại thành
một luồng dữ liệu duy nhất.

V. Tổng Kết & Lưu Ý
5.1. Khi nào dùng Node nào?

● Đổi tên trường, thêm/sửa dữ liệu đơn giản: Dùng Set Node.
● Xử lý logic phức tạp, tính toán, làm sạch sâu: Dùng Code Node.
● Xử lý một danh sách dữ liệu lớn hoặc làm việc với API: Dùng
SplitInBatch Node.
● Kiểm tra điều kiện Đúng/Sai (2 nhánh): Dùng If Node.
● Phân loại dữ liệu ra nhiều nhánh: Dùng Switch Node.
● Gộp dữ liệu từ nhiều nhánh lại: Dùng Merge Node.
5.2. Lưu ý quan trọng
● Bắt đầu từ nhỏ: Luôn thử nghiệm workflow với một lượng dữ liệu
nhỏ trước khi chạy với dữ liệu thật.
● Kiểm tra từng bước: Sau mỗi node, hãy kiểm tra cấu trúc dữ liệu
đầu ra (output) để đảm bảo nó đúng như bạn mong đợi.
● Kiểm tra cú pháp: Luôn đảm bảo các biểu thức (expressions) và
mã JavaScript được viết đúng cú pháp.
● Đặt tên rõ ràng: Đặt tên cho từng node một cách có ý nghĩa (ví dụ:
"Tính Tổng Tiền", "Lọc Đơn VIP") để dễ dàng đọc hiểu lại sau này.
---
**Bài tiếp theo:** [[Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary]]
