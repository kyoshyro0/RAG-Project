# RAG Project

The RAG project is a web app that helps answer academic questions queried from a source of scientific articles.

## Note:
The model used is vi-gemma-2b-RAG which requires a GPU with more than 8G of memory to run.

Link Model: https://drive.google.com/drive/folders/18664QHHWV0GLp8KZm_D1f-rNuLMtC0bD?usp=sharing

## Setting
Follow these steps to setup the environment and run the project.

### System Requirements
- Python 3.10 or later
- pip

### Installation instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/kyoshyro0/RAG-Project.git
2. Move to the project folder:
   ```bash
   cd RAG-Project
3. Create and activate virtual environments:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate    # On Windows
4. Install frameworks:
   ```bash
   pip install -r requirements.txt
5. Run code
   ```bash
   uvicorn src.app:app --host "0.0.0.0" --port 5000 --reload

