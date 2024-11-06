from chromadb.api.fastapi import FastAPI
from chromadb.config import Settings, System

settings = Settings(
    chroma_server_host="localhost",  
    chroma_server_http_port=8000,    
    chroma_api_impl="chromadb.api.fastapi.FastAPI"
)

system = System(settings=settings)
client = FastAPI(system)
collection = client.get_or_create_collection("document_collection")

def add_document(text, embedding):
    collection.add(documents=[text], embeddings=[embedding])

def query_documents(embedding, top_k=5):
    return collection.query(embedding=embedding, top_k=top_k)