# RAG Project

The RAG project is a web app that helps answer academic questions queried from a source of scientific articles.

## Note:
The model used is vi-gemma-2b-RAG which requires a GPU with more than 8G of memory to run.

Link Model: https://drive.google.com/drive/folders/18664QHHWV0GLp8KZm_D1f-rNuLMtC0bD?usp=sharing

## Cài đặt
Follow these steps to setup the environment and run the project.

### Yêu cầu hệ thống
- Python 3.10 or later
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
   uvicorn src.app:app --host "0.0.0.0" --port 5000 --reload

