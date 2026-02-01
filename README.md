# 🎥 Chat with YouTube (LLM-powered Q&A App)

Chat with any YouTube video using AI.  
This application extracts the transcript of a YouTube video, converts it into vector embeddings, and allows users to ask context-aware questions about the video content — even if the video is not in English.

---

## 🚀 Features

- Accepts YouTube video URLs
- Automatically fetches video transcripts
- Supports multiple languages (English, Hindi, Marathi, Tamil)
- Translates non-English transcripts to English using LLM
- Semantic search using vector embeddings
- Chat-style question answering interface
- Built with Streamlit for rapid UI development

---

## 🏗️ Architecture Overview

```text
YouTube Video URL
        │
        ▼
Extract Video ID
        │
        ▼
Fetch Transcript (YouTube Transcript API)
        │
        ├── If language ≠ English
        │       ▼
        │   Translate to English (LLM)
        │
        ▼
Text Chunking
(RecursiveCharacterTextSplitter)
        │
        ▼
Generate Embeddings (OpenAI)
        │
        ▼
Store in Vector DB (FAISS)
        │
        ▼
User Question
        │
        ▼
Semantic Search (Top-K Relevant Chunks)
        │
        ▼
Context-Aware Prompt
        │
        ▼
LLM Answer (ChatOpenAI)
        │
        ▼
Response Displayed in Streamlit Chat UI
```

## 📂 Project Structure
```
chat-with-youtube/
│
├── main.py
│   ├── extract_video_id()        # Extracts video ID from URL
│   ├── load_transcript()         # Fetches YouTube transcript
│   ├── create_vector_store()     # Creates FAISS vector DB
│   ├── get_answer()              # Retrieves context + generates answer
│   └── Translate()               # Translates transcript to English
│
├── frontend.py
│   ├── Streamlit UI
│   ├── Language selection
│   ├── Chat interface
│   └── Session state handling
│
├── requirements.txt
│
└── README.md
```

🛠️ Tech Stack

Frontend

Streamlit

Backend / AI

LangChain

OpenAI (Embeddings + Chat Model)

FAISS (Vector Store)

YouTube Transcript API

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/chat-with-youtube.git
cd chat-with-youtube
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set OpenAI API Key
In main.py:

os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
⚠️ Do NOT hardcode the key in production. Use environment variables instead.

▶️ Run the Application
streamlit run frontend.py

🧪 How It Works (Step-by-Step)
User enters a YouTube video URL
            |
App extracts the video ID
            |
Transcript is fetched using YouTube Transcript API
            |
If video language ≠ English:
            |
Transcript is translated to English using LLM
            |
Transcript is split into chunks
            |
Chunks are converted into embeddings
            |
Embeddings are stored in FAISS
            |
User asks a question
            |
Relevant transcript chunks are retrieved
            |
LLM answers using only retrieved context
```

🌍 Supported Languages
Language	Code
English	en
Hindi	hi
Marathi	mr
Tamil	ta


🔐 Limitations :
Only works for videos with available transcripts

Translation quality depends on LLM

API usage depends on OpenAI rate limits

Not optimized for extremely long videos


🧠 Future Improvements :
Add support for more languages

Cache embeddings for repeated videos

Add video summary generation

Support timestamp-based answers

Move API keys to .env

Deploy on cloud (AWS / GCP)


📌 Use Cases
Learning from long educational videos

Interview prep from YouTube tutorials

Research and content analysis

Language-independent video understanding


🧑‍💻 Author
Pruthviraj Pesode
Final-year CSE student | AI & Backend Enthusiast
Building practical LLM-powered applications 🚀

⭐ If You Like This Project
Star the repo.
Fork it.
Break it.
Improve it.
Ship it.

---
