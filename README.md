# RAG Project

Dự án RAG là một công cụ giúp trả lời các câu hỏi học thuật được truy vấn từ nguồn tài liệu là các bài báo khoa học.

## Note:
Model được sử dụng vi-gemma-2b-RAG cần có GPU có bộ nhớ lớn hơn 8G để chạy(khuyến khích 24G)

Link Model: https://drive.google.com/drive/folders/18664QHHWV0GLp8KZm_D1f-rNuLMtC0bD?usp=sharing

## Cài đặt
Làm theo các bước sau để cài đặt môi trường và chạy project.

### Yêu cầu hệ thống
- Python 3.10 hoặc mới hơn
- pip

### Hướng dẫn cài đặt
1. Clone kho lưu trữ này:
   ```bash
   git clone https://github.com/kyoshyro0/RAG-Project.git
2. Chuyển vào thư mục dự án:
   ```bash
   cd RAG-Project
3. Tạo và kích hoạt môi trường ảo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Trên macOS/Linux
   .\venv\Scripts\activate    # Trên Windows
4. Cài đặt các thư viện:
   ```bash
   pip install -r requirements.txt
5. Run code
   ```bash
   uvicorn src.app:app --host "0.0.0.0" --post 5000 --reload

