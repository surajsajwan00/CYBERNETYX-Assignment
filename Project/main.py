from fastapi import FastAPI
from routers.document_router import router as document_router

app = FastAPI()
app.include_router(document_router.router)

@app.get("/")
async def root():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    return {"message": "Welcome to the RAG API"}
