# 🧠 AI Text/Story/Script Generator

Generate compelling AI-written content like stories, scripts, podcast episodes, and blogs based on your title, genre, tone, and target audience — all from a web interface!

## ✨ Features

- 📜 Generate stories, scripts, podcasts, and more with Hugging Face LLMs (Falcon-7B, GPT-Neo, FLAN-T5)
- 🎭 Customize genre, tone/style, and audience
- 🖼️ Clean multi-page frontend (Generate | History | About)
- ⏳ Shows loading state while generating content
- 📋 Copy or ⬇️ Download content as `.txt`
- 🔊 (Optional) Convert content to speech using TTS like Coqui/Bark
- 🐳 Dockerized for easy deployment

## 🚀 Live Demo
[🔗 Railway App Link](https://your-live-url.railway.app)

## 📦 Tech Stack

- **Backend**: Flask, Hugging Face Transformers
- **Frontend**: HTML, CSS
- **Model APIs**: Falcon-7B-Instruct, GPT-Neo, FLAN-T5
- **Deployment**: Docker + Railway
- **Version Control**: Git, GitHub

## 🛠️ How to Run Locally

```bash
git clone https://github.com/yourusername/ai-content-generator.git
cd ai-content-generator
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py

🐳 Docker Usage

docker build -t ai-content-generator .
docker run -p 5000:5000 ai-content-generator

📁 Project Structure

ai-content-generator/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── models/
│   └── generate_text.py
├── requirements.txt
├── Dockerfile
├── run.py
├── .gitignore
└── README.md