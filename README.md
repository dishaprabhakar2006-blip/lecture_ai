# 🎓 Lecture AI — AI-Powered YouTube Learning Assistant

Turn any YouTube lecture into a complete study kit in minutes.

## 🚀 Live Demo
Coming soon after deployment

## 📌 What It Does
Paste a YouTube lecture URL and get:
- 📝 Structured Notes — organized with headings and bullet points
- 📋 Summary — concise 150-200 word overview
- ❓ MCQs — 10 multiple choice questions with answers
- 🃏 Flashcards — 10 front/back flashcards for revision
- 💬 AI Chatbot — ask any question about the lecture

## 🛠️ Tech Stack
- Frontend: React.js, Axios, ReactMarkdown
- Backend: FastAPI, Python
- Speech-to-Text: OpenAI Whisper (runs locally, free)
- LLM: Mistral API (free tier)
- Vector Search: FAISS + SentenceTransformer
- Database: MongoDB Atlas (free tier)
- Audio Extraction: yt-dlp + FFmpeg

## 💡 Key Features
- Zero cloud cost — Whisper runs locally, free APIs only
- MongoDB caching — same video never processed twice
- RAG-based chatbot — answers grounded in lecture content
- Falls back to general knowledge when topic not in lecture

## ⚙️ Setup

### Backend
```
cd backend
pip install fastapi uvicorn yt-dlp openai-whisper mistralai pymongo python-dotenv faiss-cpu sentence-transformers
```

Create backend/.env file:
```
MISTRAL_API_KEY=your_key_here
MONGODB_URI=your_mongodb_uri_here
```

Run backend:
```
uvicorn main:app --reload
```

### Frontend
```
cd frontend
npm install
npm start
```

## 📁 Project Structure
```
lecture-ai/
├── backend/
│ ├── main.py
│ ├── database/
│ │ └── mongo.py
│ ├── services/
│ │ ├── whisper_service.py
│ │ ├── mistral_service.py
│ │ └── faiss_service.py
│ └── routes/
│ ├── transcribe.py
│ └── chat.py
└── frontend/
└── src/
├── App.js
└── App.css
```

## 🔌 API Endpoints
- POST /transcribe — takes YouTube URL, returns notes, MCQs, summary, flashcards
- POST /chat — takes question and video URL, returns RAG-based answer

## 🧠 How RAG Works

Transcript split into 500-word chunks
Each chunk converted to embeddings using SentenceTransformer
Stored in FAISS vector index
User question converted to embedding
FAISS finds 3 most relevant chunks
Chunks and question sent to Mistral API
Answer returned grounded in lecture content

## 👩‍💻 Author
Disha P
GitHub: https://github.com/dishaprabhakar2006-blip
LinkedIn: https://www.linkedin.com/in/disha-p-46668232b/
