from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    documents = [Document(page_content=chunk) for chunk in chunks]
    return documents
