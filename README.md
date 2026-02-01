# 🎥 Chat with YouTube (LLM-powered Q&A App)

Chat with any YouTube video using AI.  
This app extracts a video transcript, converts it into embeddings, stores it in a vector database, and lets users ask natural-language questions about the video content — even if the video is **not in English**.

---

## 🚀 Features

- 🔗 Accepts **YouTube video URLs**
- 📝 Automatically fetches video transcripts
- 🌐 Supports **multiple languages** (English, Hindi, Marathi, Tamil)
- 🔁 Translates non-English transcripts to English using LLM
- 🧠 Uses **vector embeddings + semantic search**
- 💬 Chat-style Q&A interface
- ⚡ Fast and lightweight with **Streamlit**

---

## 🏗️ Architecture Overview

YouTube Video
↓
Transcript Extraction
↓
(Optional Translation → English)
↓
Text Chunking
↓
Embeddings (OpenAI)
↓
FAISS Vector Store
↓
Semantic Retrieval
↓
LLM Answer Generation


---

## 🛠️ Tech Stack

**Frontend**
- Streamlit

**Backend / AI**
- LangChain
- OpenAI (Embeddings + Chat Model)
- FAISS (Vector Store)
- YouTube Transcript API

---

## 📂 Project Structure

├── main.py # Backend logic (transcript, embeddings, LLM, translation)
├── frontend.py # Streamlit UI
├── requirements.txt
└── README.md


---

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

App extracts the video ID

Transcript is fetched using YouTube Transcript API

If video language ≠ English:

Transcript is translated to English using LLM

Transcript is split into chunks

Chunks are converted into embeddings

Embeddings are stored in FAISS

User asks a question

Relevant transcript chunks are retrieved

LLM answers using only retrieved context

🌍 Supported Languages
Language	Code
English	en
Hindi	hi
Marathi	mr
Tamil	ta
🔐 Limitations
Only works for videos with available transcripts

Translation quality depends on LLM

API usage depends on OpenAI rate limits

Not optimized for extremely long videos

🧠 Future Improvements
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
