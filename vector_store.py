from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_or_load_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # ✅ FIX: extract text from dicts
    texts = [chunk["text"] for chunk in chunks]

    vectordb = FAISS.from_texts(texts, embeddings)
    return vectordb
