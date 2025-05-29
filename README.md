# 🎤 Voice-Based Finance Assistant

A Streamlit-powered voice-enabled finance assistant that takes voice queries, retrieves relevant financial context, summarizes it using a language model, and speaks the summary aloud.

## 🚀 Features

- 🎙 Voice input using microphone
- 🔍 FAISS-powered semantic search on financial documents
- 🧠 Text summarization using `distilbart-cnn-12-6`
- 🔊 Text-to-speech summary
- 🧩 Modular agent-based design (`voice_agent`, `retriever_agent`, `language_agent`)
- 📚 Powered by HuggingFace Transformers, LangChain, FAISS, and Streamlit

## 🛠 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- LangChain + FAISS
- SpeechRecognition + pyttsx3
- SentenceTransformers

## 📦 Installation

```bash
git clone https://github.com/cseazeem/voice-finance-agent.git
cd finance-assistant
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
