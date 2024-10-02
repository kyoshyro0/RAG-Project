from typing import Union
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModel
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import torch

tokenizer = AutoTokenizer.from_pretrained('vinai/phobert-base')
model = AutoModel.from_pretrained('vinai/phobert-base')

def encode_text(texts):
    inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
    
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

class PhoEmbeddings(HuggingFaceBgeEmbeddings):
    def embed_documents(self, texts):
        return [encode_text(text) for text in texts]
    
    def embed_query(self, text: str):
        return encode_text(text)

class VectorDB:
    def __init__(self,
                 documents = None,
                 vector_db: Union[Chroma, FAISS] = Chroma,
                 embedding = PhoEmbeddings(),
                 ) -> None:
        self.vector_db = vector_db
        self.embedding = embedding
        self.db = self._build_db(documents)
    
    def _build_db(self, documents):
        db = self.vector_db.from_documents(documents=documents,
                                           embedding=self.embedding)
        return db
    
    def get_retriever(self,
                      search_type: str = "similarity",
                      search_kwargs: dict = {"k": 10}):
        retriever = self.db.as_retriever(search_type=search_type,
                                         search_kwargs=search_kwargs)
        return retriever
