import faiss
import numpy as np
from langchain_community.llms import Ollama

class Retriever:
    def __init__(self, dim=384):
        self.dim = dim

        # FAISS IP index (inner product = cosine sim since vectors normalized)
        self.index = faiss.IndexFlatIP(dim)

        # Store docs in Python list
        self.documents = []

        # Load local LLM from Ollama
        try:
            self.llm = Ollama(model="llama3.2")   # you downloaded llama3.2
        except Exception as e:
            print("⚠ Ollama not reachable:", e)
            self.llm = None

    def add_documents(self, chunks, vectors):
        """
        chunks: list of strings
        vectors: numpy array, shape (N, dim)
        """
        for chunk in chunks:
            self.documents.append(chunk)

        # Add embeddings to FAISS
        vectors = vectors.astype("float32")
        self.index.add(vectors)

    def search(self, query_vector, top_k=4):
        """
        Returns top K matching document chunks.
        """
        if len(self.documents) == 0:
            return []

        D, I = self.index.search(np.array([query_vector], dtype="float32"), top_k)

        results = []
        for idx in I[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])
        return results

    def ask(self, question, embedder):
        """
        Main function:
        - embed the question
        - retrieve top contexts
        - build prompt
        - call LLM (Ollama)
        """
        q_vec = embedder.embed([question])[0]  # embed single question

        contexts = self.search(q_vec)
        context_text = "\n\n".join(contexts)

        prompt = f"""
You are a helpful medical assistant.
Use ONLY the context provided below to answer the question.

### CONTEXT:
{context_text}

### QUESTION:
{question}

### ANSWER:
"""

        if self.llm:
            try:
                output = self.llm(prompt)
                return output
            except Exception as e:
                print("LLM error:", e)
                return context_text[:500]
        else:
            return context_text[:500]
