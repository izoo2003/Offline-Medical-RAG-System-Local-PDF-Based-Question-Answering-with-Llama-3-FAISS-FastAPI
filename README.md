# Offline Medical RAG Assistant

**Project purpose:** Build a fully offline, open-source RAG-based Medical Q&A assistant that requires **no paid APIs or credit cards**.  
It uses local embeddings, FAISS vector store, LangChain retrieval patterns, a local LLM (via Ollama), and a FastAPI backend. Dockerized for easy deployment.

**Resume reference (your uploaded resume on this machine):** `/mnt/data/Updated_Resume.pdf`

---

## Key components
- FastAPI backend with endpoints: `/upload_document`, `/ask`, `/health`
- Document ingestion: PDF → text chunks → embeddings
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2` (local PyTorch model)
- Vector store: FAISS (local)
- Retriever: LangChain RetrievalQA + local LLM (Ollama)
- UI (optional): Streamlit demo `ui/streamlit_app.py`
- Tests: PyTest test suite in `tests/`
- Dockerized: `Dockerfile` + `docker-compose.yml`

---

## Quick setup (local, no cloud)
1. Create a Python virtualenv and activate it:
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Install Ollama (run locally) — instructions: https://ollama.com (Ollama runs locally and does not require a credit card).
   - Once Ollama is installed, pull a small LLM image (examples): `ollama pull llama3` or `ollama pull phi3`
   - Alternatively, you can configure the app to use an API-compatible local LLM endpoint.

3. Start the API:
```bash
uvicorn app.main:app --reload
```

4. Upload documents via `/upload_document` or place PDFs into `data/uploads/` and run ingestion:
```bash
python -m app.ingest --path data/uploads
```

5. Ask questions:
POST to `/ask` with JSON `{ "question": "What are the patient's symptoms?" }`

---

## Folder layout
```
/mnt/data/offline-medical-rag
├─ app/
│  ├─ main.py
│  ├─ ingest.py
│  ├─ embeddings.py
│  ├─ retriever.py
│  ├─ schemas.py
│  └─ utils.py
├─ ui/
│  └─ streamlit_app.py
├─ tests/
│  ├─ test_api.py
│  └─ test_retrieval.py
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

## Notes
- This project is fully offline if you run a local LLM (Ollama). All other components are open-source and free.
- The included code skeletons are intentionally minimal and annotated so you can implement and iterate quickly.
