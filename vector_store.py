
from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()


    # ✅ FIX: extract text from dicts
    texts = [chunk["text"] for chunk in chunks]

    vectordb = FAISS.from_texts(texts, embeddings)
    return vectordb
