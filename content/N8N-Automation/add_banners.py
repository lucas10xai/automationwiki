import os

DIR = "/Users/nghia/Downloads/my-digital-garden/content/N8N-Automation"

image_map = {
    "00-N8N 101 - Mục lục.md": "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=1200&q=80",
    "01-AI & Automation - Tổng quan và ứng dụng.md": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&q=80",
    "02-Giới thiệu n8n và triết lý low-code.md": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80",
    "03-Cài đặt n8n Self-host qua Docker.md": "https://images.unsplash.com/photo-1605745341112-85968b19335b?w=1200&q=80",
    "04-Cài đặt n8n trên Instance EC2 Amazon Web Service.md": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80",
    "05-Cài đặt n8n trên Instance Raspberry Pi.md": "https://images.unsplash.com/photo-1555661530-68c8e98db4e6?w=1200&q=80",
    "06-Phân biệt Trigger Node và Action Node.md": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&q=80",
    "07-Trigger Nodes & Action trong App Nodes.md": "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=1200&q=80",
    "08-Core Nodes & Nguyên tắc Dataflow trong n8n.md": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    "09-Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary.md": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&q=80",
    "10-Data Transformation & Flow Control Nodes trong n8n.md": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&q=80",
    "11-Quản lí Credential (Thông tin xác thực).md": "https://images.unsplash.com/photo-1614064641913-6b7140414c71?w=1200&q=80",
    "LLM/12-Vai trò của LLM trong Quy trình Tự động hóa.md": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&q=80"
}

import re

for rel_path, img_url in image_map.items():
    filepath = os.path.join(DIR, rel_path)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if image is already added to prevent duplicates
    if "images.unsplash.com" in content:
        continue
        
    # We want to insert the image right after the first `> [!nav]` block.
    # The block looks like:
    # > [!nav] Điều hướng
    # > **Tới trang chủ:** ...
    # > **Bài trước:** ...
    # > **Bài tiếp theo:** ...
    # \n
    
    # We can use regex to find the end of the first nav block
    # It starts with `> [!nav]` and ends with the first line that doesn't start with `>`
    
    lines = content.split('\n')
    new_lines = []
    nav_found = False
    nav_ended = False
    inserted = False
    
    for line in lines:
        new_lines.append(line)
        if not inserted:
            if line.startswith("> [!nav]"):
                nav_found = True
            elif nav_found and not nav_ended:
                if not line.startswith(">"):
                    # Nav block ended
                    nav_ended = True
                    # Insert the image
                    img_markdown = f"\n![Cover Image]({img_url})\n"
                    new_lines.append(img_markdown)
                    inserted = True
                    
    # Fallback if nav block wasn't found or wasn't formatted as expected
    if not inserted:
        # Just insert after frontmatter
        if content.startswith("---"):
            # find second "---"
            parts = content.split("---", 2)
            if len(parts) >= 3:
                new_content = "---" + parts[1] + "---\n\n" + f"![Cover Image]({img_url})\n" + parts[2]
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                continue
                
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
    print(f"Added banner to {rel_path}")

