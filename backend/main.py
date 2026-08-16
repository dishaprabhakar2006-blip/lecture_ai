from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()
from routes.transcribe import router as transcribe_router

app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )
app.include_router(transcribe_router)
@app.get("/")
def read_root():
    return {"message":"Lecture AI backend is running"}

from routes.chat import router as chat_router
app.include_router(chat_router)