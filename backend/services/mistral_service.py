from dotenv import load_dotenv
load_dotenv()
import os
from mistralai import Mistral

client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

def ask_mistral(prompt:str)->str:
    response=client.chat.complete(model="mistral-small-latest",
                                  messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content
def generate_summary(transcript:str)->str:
    prompt=f"""You are a helpful study assistant. 
    Given the following lecture transcript,generate a concise summary.
    Transcript:
    {transcript}
    Provide a clear,concise summary in 150-200 words."""
    return ask_mistral(prompt)

def generate_notes(transcript:str)->str:
    prompt=f"""You are a helpful study assistant. 
    Given the following lecture transcript,generate structure study notes.
    Transcript:
    {transcript}
    Format the notes with:
    -Main topics as headings
    -Key points as bullet points
    -Important definitions clearly marked"""
    return ask_mistral(prompt)

def generate_mcqs(transcript:str)->str:
    prompt=f"""You are a helpful study assistant.
Given the following lecture transcript, generate 10 multiple choice questions.

Transcript:
{transcript}
Format each question as:
**Q1.** Question here
A) option
B) option
C) option
D) option
**Answer:** X"""
    return ask_mistral(prompt)

def generate_flashcards(transcript:str)->str:
    prompt=f"""You are a helpful study assistant.
Given the following lecture transcript, generate 10 flashcards.

Transcript:
{transcript}
Format each flashcard as:
FRONT:concept or question
BACK:definition or answer"""
    return ask_mistral(prompt)

def answer_question(question:str,context:str)->str:
    prompt=f"""You are a helpful study assistant.
Use the following lecture content to answer the question.
If the answer is in the context, use it.
If not, answer from general knowledge but mention it wasn't in the lecture.

Lecture context:
{context}

Question:{question}"""
    return ask_mistral(prompt)
