import streamlit as st
import requests
import json

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Offline Medical RAG", layout="wide")

st.title("📚 Offline Medical RAG System")
st.subheader("Ask questions from your uploaded medical PDFs")

# --- Upload Section ---
st.header("Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Upload"):
    if not uploaded_files:
        st.warning("Please upload at least one PDF.")
    else:
        for file in uploaded_files:
            files = {"file": (file.name, file.getvalue(), "application/pdf")}
            response = requests.post(f"{FASTAPI_URL}/upload_document", files=files)

        st.success("All documents uploaded successfully!")


# --- Ask Question ---
st.header("Ask a Question")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Enter a question.")
    else:
        payload = {"question": question}

        response = requests.post(
            f"{FASTAPI_URL}/ask",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            st.success("Answer:")
            st.write(response.json()["answer"])
        else:
            st.error("Error occurred while processing request.")


# --- Health Check ---
with st.sidebar:
    st.header("System Status")
    health = requests.get(f"{FASTAPI_URL}/health")
    if health.status_code == 200:
        st.success("Backend Online")
    else:
        st.error("Backend Offline ❌")
