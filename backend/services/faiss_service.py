import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()

model=SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text:str,chunk_size:int=500)->list:
    words=text.split()
    chunks=[]
    for i in range(0,len(words),chunk_size):
        chunk=" ".join(words[i:i+chunk_size])
    return chunks

def create_faiss_index(transcript:str):
    chunks=chunk_text(transcript)
    if not chunks:
        chunks=[transcript]
    embeddings=model.encode(chunks)
    embeddings=np.array(embeddings).astype('float32')
    if len(embeddings.shape)==1:
        embeddings=embeddings.reshape(1,-1)
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index,chunks

def search_faiss(question:str,index,chunks:list,top_k:int=3)->str:
    question_embedding=model.encode([question])
    question_embedding=np.array(question_embedding).astype('float32')
    distances,indices=index.search(question_embedding,top_k)
    relevant_chunks=[chunks[i] for i in indices[0]]
    return " ".join(relevant_chunks)