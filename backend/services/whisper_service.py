import yt_dlp
import whisper
import os

def download_audio(youtube_url:str)->str:
    ydl_opts={
        'format':'bestaudio/best',
        'outtmpl':'audio.%(ext)s',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return "audio.mp3"

def transcribe_audio(file_path:str)->str:
    model=whisper.load_model("base")
    result=model.transcribe(file_path)
    return result["text"]

def process_youtube_url(youtube_url:str)->str:
    audio_path=download_audio(youtube_url)
    transcript=transcribe_audio(audio_path)
    os.remove(audio_path)
    return transcript 