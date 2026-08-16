from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from services.faiss_service import create_faiss_index,search_faiss
from services.mistral_service import answer_question
from database.mongo import videos_collection

router=APIRouter()

class ChatRequest(BaseModel):
    video_url:str
    question:str

@router.post("/chat")
async def chat(request:ChatRequest):
    video=videos_collection.find_one({"url":request.video_url})

    if not video:
        return {"answer":"Video not found.Please transcribe it first."}

    transcript=video["transcript"]

    index,chunks=create_faiss_index(transcript)
    context=search_faiss(request.question,index,chunks)
    answer=answer_question(request.question,context)
    return {"answer":answer}
