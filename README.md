
# 📘 Offline Medical RAG System

**Local PDF-Based Question Answering using Llama 3, FAISS, FastAPI, and Streamlit**

A fully offline Retrieval-Augmented Generation (RAG) application that allows users to upload medical PDFs and ask natural-language questions about them. Built using local models via **Ollama**, semantic search through **FAISS**, embeddings using **Sentence Transformers**, a **FastAPI** backend, and a clean **Streamlit** web interface.

No cloud APIs, no paid services, and no internet connection required.

---

## ✨ Features

* 📄 **Upload Medical PDFs** and extract text automatically
* 🔍 **Semantic Search with FAISS** for high-accuracy retrieval
* 🧠 **Local Llama 3.2 via Ollama** for fully offline LLM responses
* 🧩 **RAG Pipeline** (retrieve → augment → generate)
* ⚡ **FastAPI Backend** exposing clean REST endpoints
* 🎨 **Streamlit Frontend** for real-time interactive Q&A
* 🔒 **Zero Cloud Dependencies** (completely private & local)
* 🧪 **Extendable & Modular Architecture**

---

## 🏗️ Project Architecture

```
               ┌─────────────────────┐
               │     Streamlit UI     │
               └──────────┬───────────┘
                          ↓
                ┌───────────────────┐
                │    FastAPI API    │
                └───────┬──────────┘
        Upload PDF       │        Ask Question
                          ↓
           ┌──────────────────────────────┐
           │        Ingestion Pipeline     │
           │  (PDF → Text → Chunks → Embed)│
           └───────────┬──────────────────┘
                       ↓
            ┌──────────────────────┐
            │       FAISS DB       │
            └──────────┬───────────┘
                       ↓
               Retrieve Top Chunks
                       ↓
           ┌────────────────────────┐
           │      Llama 3 (Ollama)   │
           └────────────────────────┘
```

---

## 🛠️ Technologies Used

### 🔹 **Core AI/RAG**

* **Sentence Transformers** – Text embeddings
* **FAISS** – Vector similarity search
* **Llama 3.2 (Ollama)** – Local LLM inference
* **Custom Chunking & Retrieval Logic**

### 🔹 **Backend**

* **FastAPI** – REST API
* **Uvicorn** – ASGI server

### 🔹 **Frontend**

* **Streamlit** – Real-time interactive UI

### 🔹 **Utilities**

* **pypdf** – PDF text extraction
* **NumPy** – Vector normalization
* **Requests** – API communication

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/offline-medical-rag.git
cd offline-medical-rag
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Install & Run Ollama Model

Install Ollama: [https://ollama.com](https://ollama.com)
Then pull the model:

```
ollama pull llama3.2
```

### 5️⃣ Start FastAPI Backend

```
uvicorn app.main:app --reload
```

### 6️⃣ Start Streamlit Frontend

Open a second terminal, re-activate venv:

```
venv\Scripts\activate
streamlit run ui/app.py
```

UI will open on **[http://localhost:8501](http://localhost:8501)**

---

## 🚀 Usage

### **Upload Documents**

* Upload one or multiple PDFs
* System ingests → chunks → embeds → stores in FAISS

### **Ask Questions**

Type questions like:

* “Summarize this document.”
* “What symptoms are described?”
* “What medications are mentioned?”

System retrieves best chunks and Llama generates the answer.

---

## 🧠 How RAG Works in This Project

1. PDF uploaded
2. Text extracted using pypdf
3. Text split into semantic chunks
4. Chunks embedded using `all-MiniLM-L6-v2`
5. Stored in FAISS for similarity search
6. User asks a question → embedded
7. FAISS retrieves most relevant chunks
8. Llama 3.2 generates answer using retrieved context

---

## 🗂️ Project Structure

```
offline-medical-rag/
│
├── app/
│   ├── main.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── document_loader.py
│   └── rag_engine.py
│
├── ui/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## 📈 Future Enhancements

* Chat history
* “Show retrieved sources”
* Advanced chunking (semantic splitting)
* Hybrid search (BM25 + vectors)
* PDF page previews
* Persistent FAISS storage

---

## 🤝 Contributing

Pull requests and ideas are welcome!

---
