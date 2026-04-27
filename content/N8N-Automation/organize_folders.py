import os
import shutil
import re

DIR = "/Users/nghia/Downloads/my-digital-garden/content/N8N-Automation"

# Define the target folders
folders = {
    "1-Tư duy và Nhập môn": [
        "01-AI & Automation - Tổng quan và ứng dụng.md",
        "02-Giới thiệu n8n và triết lý low-code.md"
    ],
    "2-Cài đặt hệ thống": [
        "03-Cài đặt n8n Self-host qua Docker.md",
        "04-Cài đặt n8n trên Instance EC2 Amazon Web Service.md",
        "05-Cài đặt n8n trên Instance Raspberry Pi.md"
    ],
    "3-Kỹ năng n8n Cốt lõi": [
        "06-Phân biệt Trigger Node và Action Node.md",
        "07-Trigger Nodes & Action trong App Nodes.md",
        "08-Core Nodes & Nguyên tắc Dataflow trong n8n.md",
        "09-Tìm hiểu các định dạng Dữ liệu trong n8n - JSON và Binary.md",
        "10-Data Transformation & Flow Control Nodes trong n8n.md",
        "11-Quản lí Credential (Thông tin xác thực).md"
    ],
    "4-Nâng cao với AI": [
        "12-Vai trò của LLM trong Quy trình Tự động hóa.md"
    ],
    "5-Dự án thực hành": [
        "13-Dự án - Kết nối Lark với Obsidian qua n8n.md"
    ]
}

# Find all md files recursively in DIR to update links
all_md_files = []
for root, dirs, files in os.walk(DIR):
    for f in files:
        if f.endswith(".md"):
            all_md_files.append(os.path.join(root, f))

# 1. Update links: Strip the folder paths from [[Folder/Filename]] to just [[Filename]]
for filepath in all_md_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace [[LLM/12-Vai trò của LLM...]] with [[12-Vai trò của LLM...]]
    # Also for any other paths if they exist
    # Regex to find [[Path/To/File]] and replace with [[File]]
    # But be careful with aliases [[Path/To/File|Alias]] -> [[File|Alias]]
    
    # Pattern: \[\[ (.*?/) (.*?)(|.*?)? \]\]
    # We can just explicitly replace the known LLM path since we know it's there
    new_content = content.replace("[[LLM/12-Vai trò của LLM trong Quy trình Tự động hóa]]", "[[12-Vai trò của LLM trong Quy trình Tự động hóa]]")
    new_content = new_content.replace("[[LLM/12-Vai trò của LLM trong Quy trình Tự động hóa|", "[[12-Vai trò của LLM trong Quy trình Tự động hóa|")
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

# 2. Move the files
for folder, files in folders.items():
    folder_path = os.path.join(DIR, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    for file in files:
        # Search for the file in DIR and subdirectories
        src_path = None
        for root, _, fs in os.walk(DIR):
            if file in fs:
                src_path = os.path.join(root, file)
                break
                
        if src_path:
            dst_path = os.path.join(folder_path, file)
            if src_path != dst_path:
                shutil.move(src_path, dst_path)
                print(f"Moved {file} -> {folder}/")

# 3. Clean up empty LLM folder if it exists and is empty
llm_dir = os.path.join(DIR, "LLM")
if os.path.exists(llm_dir):
    if not os.listdir(llm_dir):
        os.rmdir(llm_dir)
        print("Removed empty LLM directory")
