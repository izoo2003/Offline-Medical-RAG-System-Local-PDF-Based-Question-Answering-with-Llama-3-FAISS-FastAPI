from fastapi import FastAPI, UploadFile, File
import os
from .ingest import ingest_pdf
from .retriever import Retriever
from .embeddings import Embedder

app = FastAPI(title="Offline Medical RAG Assistant")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(os.path.join(DATA_DIR, "uploads"), exist_ok=True)

retriever = Retriever()
embedder = Embedder()   # load once at startup

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload_document")
async def upload_document(file: UploadFile = File(...)):
    save_path = os.path.join(DATA_DIR, "uploads", file.filename)
    with open(save_path, "wb") as f:
        f.write(await file.read())

    num_chunks = ingest_pdf(save_path, retriever, embedder)
    return {"status": "ok", "chunks": num_chunks}

@app.post("/ask")
async def ask(payload: dict):
    question = payload.get("question", None)
    if not question:
        return {"error": "Missing question"}

    answer = retriever.ask(question, embedder)
    return {"answer": answer}
