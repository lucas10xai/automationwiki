---
title: "🚀 n8n Automation Wiki Toàn Tập"
tags: [n8n, automation, wiki, ai, index, toc, roadmap]
publish: true
---

> [!info] 🌟 Chào mừng đến với **n8n Automation Wiki**!
> Đây là nơi tổng hợp tất cả kiến thức về n8n từ cơ bản đến nâng cao. Wiki này được thiết kế để giúp bạn làm chủ tự động hóa, kết nối các ứng dụng và tích hợp sức mạnh của AI vào quy trình làm việc. Mỗi bài viết đều đi kèm hướng dẫn chi tiết, sơ đồ minh hoạ và ví dụ thực tế.

![n8n banner](https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a?w=1200&q=80)

---

## 🟢 Phần 1: Tư duy & Nhập môn
Các khái niệm cơ bản nhất giúp bạn định hình tư duy về Automation và làm quen với n8n.

- 🔰 [[01-AI & Automation - Tổng quan và ứng dụng|Tổng quan về AI & Automation]]
- 🔰 [[02-Giới thiệu n8n và triết lý low-code|Giới thiệu n8n và triết lý low-code]]

---

## 🛠️ Phần 2: Cài đặt & Triển khai (Deployment)
Hướng dẫn chi tiết từng bước để tự host n8n trên các nền tảng khác nhau.

- 🐳 [[03-Cài đặt n8n Self-host qua Docker|Cài đặt n8n qua Docker (Khuyên dùng)]]
- ☁️ [[04-Cài đặt n8n trên Instance EC2 Amazon Web Service|Deploy trên AWS EC2]]
- 🍓 [[05-Cài đặt n8n trên Instance Raspberry Pi|Deploy trên Raspberry Pi]]
- 🔐 [[25-Cấu hình HTTPS Reverse Proxy Nginx và Cloudflare Tunnel|Cấu hình HTTPS, Reverse Proxy (Nginx) & Cloudflare Tunnel]]
- 🔄 [[26-Backup và Restore dữ liệu n8n|Backup & Restore dữ liệu n8n]]

---

## ⚙️ Phần 3: Kỹ năng n8n Cốt lõi
Nắm vững các khái niệm nền tảng để xây dựng bất kỳ workflow nào.

- 🔀 [[06-Phân biệt Trigger Node và Action Node|Hiểu về Trigger Node và Action Node]]
- 🧩 [[07-Trigger Nodes & Action trong App Nodes|Cách sử dụng Trigger và Action trong App Nodes]]
- 🌊 [[08-Core Nodes & Nguyên tắc Dataflow trong n8n|Nguyên tắc Dataflow (Luồng dữ liệu) trong n8n]]
- 🗃️ [[09-Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary|Xử lý dữ liệu JSON và Binary]]
- 🔀 [[10-Data Transformation & Flow Control Nodes trong n8n|Các Node điều hướng (Flow Control) & Biến đổi dữ liệu]]
- 🔑 [[11-Quản lí Credential (Thông tin xác thực)|Quản lý Credentials và bảo mật API Key]]

---

## 🔥 Phần 4: Kỹ năng Nâng cao (Advanced & Pro)
Đưa kỹ năng của bạn lên một tầm cao mới với việc xử lý logic phức tạp.

- 💻 [[14-Sử dụng Expressions và Formulas trong n8n|Sử dụng Expressions & Formulas trong n8n]]
- 🌐 [[15-Node HTTP Request - Gọi bất kỳ API nào|Node HTTP Request - Gọi bất kỳ API nào]]
- 🧑‍💻 [[16-Node Code - Viết code tùy chỉnh JavaScript Python|Node Code (JavaScript/Python) - Viết code tùy chỉnh]]
- 🛡️ [[17-Error Handling - Bắt lỗi và xử lý ngoại lệ|Error Handling - Bắt lỗi và xử lý ngoại lệ]]
- 🔁 [[18-Execute Workflow Node - Thiết kế Sub-workflows|Execute Workflow Node - Thiết kế Sub-workflows]]
- 🎣 [[19-Webhooks - Nhận dữ liệu thời gian thực|Webhooks - Nhận dữ liệu thời gian thực]]
- 📦 [[20-Xử lý mảng Arrays Batching và Phân trang Pagination|Xử lý mảng (Arrays), Batching và Phân trang (Pagination)]]

---

## 🤖 Phần 5: Tích hợp AI & LLM (AI Agents)
Tận dụng tính năng Advanced AI của n8n để biến workflow thành một AI Agent tự hành.

- 🧠 [[12-Vai trò của LLM trong Quy trình Tự động hóa|Vai trò của LLM trong Automation]]
- 💬 [[21-Kết nối OpenAI và Anthropic Claude vào n8n|Kết nối OpenAI (ChatGPT) / Anthropic (Claude) vào n8n]]
- 🕵️ [[22-Xây dựng AI Agent với các Tools tùy chỉnh|Xây dựng AI Agent với các Tools tùy chỉnh]]
- 📚 [[23-Ứng dụng RAG và Vector Store trong n8n|Ứng dụng RAG (Retrieval-Augmented Generation) & Vector Store]]
- 🧠 [[24-Cấp phát Memory cho AI Agent|Cấp phát Memory cho AI Agent]]

---

## 🚀 Phần 6: Dự án thực hành
Thực chiến với các bài toán Automation ứng dụng thực tế.

- 🔗 [[13-Dự án - Kết nối Lark với Obsidian qua n8n|Dự án: Kết nối Lark với Obsidian qua n8n]]
- 📱 *[Sắp ra mắt] Tự động lập lịch & đăng bài Social Media (Facebook, LinkedIn)*
- 🤖 *[Sắp ra mắt] Tạo Telegram Bot / Slack Bot phản hồi tự động bằng AI*
- 📊 *[Sắp ra mắt] Đồng bộ Lead từ Landing Page sang CRM (HubSpot/Lark) và Google Sheets*
- 📧 *[Sắp ra mắt] Đọc email tự động, phân tích bằng AI và lưu file đính kèm*
- 📝 *[Sắp ra mắt] Auto-Blogging: Tự động thu thập tin tức và viết lại bài đăng lên WordPress*

---

## 📚 Phần 7: Tài nguyên & Best Practices
- 🏆 *[Sắp ra mắt] Best Practices: Cách tổ chức một workflow gọn gàng, dễ bảo trì*
- 🌍 *[Sắp ra mắt] Tổng hợp các nguồn học n8n và Cộng đồng*
- 💡 *[Sắp ra mắt] Các Node cộng đồng (Community Nodes) hữu ích nhất*

---

> [!tip] Mẹo sử dụng Wiki
> - Sử dụng thanh tìm kiếm 🔍 (Search) của Quartz để tìm nhanh các khái niệm (vd: "HTTP Request", "Docker").
> - Các bài viết có nhãn *[Sắp ra mắt]* đang trong quá trình biên soạn và sẽ sớm được cập nhật!
> - Mỗi bài học có nút điều hướng **← Bài trước / Bài tiếp theo →** để đọc tuần tự theo lộ trình.
