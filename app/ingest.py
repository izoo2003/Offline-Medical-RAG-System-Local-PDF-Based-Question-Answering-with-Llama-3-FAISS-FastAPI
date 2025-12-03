import os
from pypdf import PdfReader
from .embeddings import Embedder

def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def ingest_pdf(path, retriever, embedder=None):
    print(f"[Ingest] Reading: {path}")

    if embedder is None:
        embedder = Embedder()

    # Read PDF
    reader = PdfReader(path)
    pages = []
    for p in reader.pages:
        pages.append(p.extract_text() or "")

    full_text = "\n".join(pages)

    # Chunk text
    chunks = chunk_text(full_text)

    # Embed chunks
    vectors = embedder.embed(chunks)

    # Store in retriever
    retriever.add_documents(chunks, vectors)

    return len(chunks)
