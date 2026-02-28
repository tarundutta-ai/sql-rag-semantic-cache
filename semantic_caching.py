import os
import faiss
import numpy as np
import pickle
from openai import OpenAI
from config import settings

class SemanticSQLCache:
    def __init__(self, index_path = settings.VECTOR_CACHE_PATH, metadata_path = settings.METADATA_PKL, dimension = settings.VECTOR_DIMENSION):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.index = self._load_or_create_index()
        self.metadata = self._load_metadata()
        self.dimension = dimension


    def _load_or_create_index(self):
        if os.path.exists(self.index_path):
            return faiss.read_index(self.index_path)
        return faiss.IndexFlatIP(1536)
    
    
    def _load_metadata(self):
        if os.path.exists(self.metadata_path):
            with open(self.metadata_path,"rb") as f:
                return pickle.load(f)
            
        return []
            
    def _save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def _embed(self, text):
        response = self.client.embeddings.create(
            model = settings.EMBEDDING_MODEL,
            input = text
        )

        embedding = np.array(response.data[0].embedding).astype("float32")
        faiss.normalize_L2(embedding.reshape(1,-1))
        return embedding
    
    def search(self, question):
        if self.index.ntotal == 0:
            return None
        query_vector = self._embed(question)
        query_vector = query_vector.reshape(1,-1)
        scores, indices = self.index.search(query_vector, 1)
        score = scores[0][0]
        idx = indices[0][0]
        if score>=settings.CACHE_SEMATIC_MATCHING:
            return self.metadata[idx]
        
        return None
    
    def add(self, question, sql_query):
        vector = self._embed(question)
        vector = vector.reshape(1,-1)

        self.index.add(vector)
        self.metadata.append({

            "question": question,
            "sql":sql_query
        })

        self._save()





    



