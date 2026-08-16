from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from services.whisper_service import process_youtube_url
from services.mistral_service import generate_summary,generate_notes,generate_mcqs,generate_flashcards
from database.mongo import videos_collection

router=APIRouter()

class VideoRequest(BaseModel):
    url:str
@router.post("/transcribe")
async def transcribe_video(request:VideoRequest):
    url=request.url
    existing=videos_collection.find_one({"url":url})
    if existing:
        existing["_id"]=str(existing["_id"])
        return existing
    transcript=process_youtube_url(url)

    summary= generate_summary(transcript)
    notes=generate_notes(transcript)
    mcqs=generate_mcqs(transcript)
    flashcards=generate_flashcards(transcript)

    video_data={
        "url":url,
        "transcript":transcript,
        "summary":summary,
        "notes":notes,
        "mcqs":mcqs,
        "flashcards":flashcards

    }
    videos_collection.insert_one(video_data)
    video_data["_id"]=str(video_data["_id"])
    return video_data
