from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.document_processing import extract_text
from utils.embeddings import get_embeddings
from chromadb_file.chroma_client import add_document, query_documents

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        text = await extract_text(file)
        embedding = get_embeddings(text)
        add_document(text, embedding)
        return {"status": "Document uploaded and ingested"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/query")
async def query_document(query: str):
    query_embedding = get_embeddings(query)
    results = query_documents(query_embedding, top_k=5)
    return {"results": results}
