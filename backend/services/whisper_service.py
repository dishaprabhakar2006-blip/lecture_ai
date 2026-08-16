from dotenv import load_dotenv
load_dotenv()
import os
import yt_dlp
import glob
from groq import Groq

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def download_audio(youtube_url: str) -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        },
        'cookiesfrombrowser': ('chrome',),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    files = glob.glob("audio.*")
    return files[0] if files else "audio.mp3"


def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcription = groq_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=audio_file,
        )
    return transcription.text


def process_youtube_url(youtube_url: str) -> str:
    audio_path = download_audio(youtube_url)
    transcript = transcribe_audio(audio_path)
    os.remove(audio_path)
    return transcript