import numpy as np
from app.retriever import Retriever

def test_add_and_search():
    r = Retriever(dim=384)
    docs = ["This is a test document about diabetes.", "Another doc about hypertension."]
    vectors = [np.random.rand(384).astype('float32') for _ in docs]
    r.add_documents(docs, vectors)
    res = r._search(vectors[0], top_k=1)
    assert len(res) >= 1
