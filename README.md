# RAG Project

The RAG project is a web app that helps answer academic questions queried from a source of scientific articles.

## Note:
The model used is Vicuna which requires a GPU with more than 8G of memory to run.

Link Model: https://huggingface.co/lmsys/vicuna-7b-v1.5

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
5. Clone model:
   ```bash
   cd src/base/lmsys
   ```
   
   Make sure you have git-lfs installed
   ```bash
   git lfs install
   ```

   Clone model
   ```bash
   git clone https://huggingface.co/lmsys/vicuna-7b-v1.5
   ```
6. Run code
   ```bash
   cd RAG-Project
   ```
   ```bash
   uvicorn src.app:app --host "0.0.0.0" --port 5000 --reload

