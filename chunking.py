from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []
    for doc in documents:
        split_texts = splitter.split_text(doc["content"])
        for text in split_texts:
            chunks.append({
                "text": text,
                "metadata": {
                    "source": doc["source"],
                    "title": doc["title"]
                }
            })
    return chunks
