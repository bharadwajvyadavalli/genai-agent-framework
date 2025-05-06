import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FaissMemory:
    def __init__(self, dim=384, index_path='faiss.index'):
        self.dim = dim
        self.index_path = index_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self.entries = np.load('entries.npy', allow_pickle=True).tolist()
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.entries = []

    def add(self, key: str, value: str):
        text = f"{key}: {value}"
        emb = self.model.encode(text, convert_to_numpy=True)
        self.index.add(emb.reshape(1, -1))
        self.entries.append(text)
        faiss.write_index(self.index, self.index_path)
        np.save('entries.npy', np.array(self.entries, dtype=object))

    def query(self, query: str, k: int = 3):
        emb = self.model.encode(query, convert_to_numpy=True)
        D, I = self.index.search(emb.reshape(1, -1), k)
        results = []
        for idx in I[0]:
            if idx < len(self.entries):
                results.append(self.entries[idx])
        return results
