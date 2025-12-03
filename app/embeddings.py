from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        print("[Embedder] Loading embedding model...")
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        """
        Accepts a list of texts (strings) and returns a normalized numpy matrix.
        """
        vectors = self.model.encode(texts, convert_to_numpy=True)
        # Normalize all vectors
        norms = np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-10
        return vectors / norms
