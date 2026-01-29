# Website-Based Chatbot Using Embeddings

<img width="1906" height="917" alt="Screenshot 2026-01-29 235442" src="https://github.com/user-attachments/assets/0b392e4a-4715-4527-98d2-94fd9a05958a" />
<img width="1902" height="960" alt="Screenshot 2026-01-30 005833" src="https://github.com/user-attachments/assets/1afcff30-a93c-4a30-935f-aebf95d8737d" />


## Project Overview

This project is an AI-powered website-based chatbot that allows users to ask questions strictly grounded in the content of a given website. The system crawls and cleans website HTML, generates embeddings from the extracted text, stores them in a persistent vector database, and retrieves relevant context to answer user queries accurately without hallucination.

##Project Folder

website-chatbot/
│
├── app.py
├── crawler.py
├── chunking.py
├── vector_store.py
├── qa.py
├── requirements.txt
├── README.md
│
├── data/                # created automatically
│   └── faiss_index/
│
└── venv/                # optional (DO NOT upload to GitHub)

 
## Architecture Explanation

**Flow:**

```
User URL → Crawl Website → Clean HTML → Chunk Text → Generate Embeddings → Store in Vector DB → Retrieve Relevant Chunks → LLM Answer
```

* **Crawling & Extraction:** Fetches HTML pages and extracts meaningful text while removing headers, footers, navigation menus, and ads.
* **Text Processing:** Normalizes text and splits it into configurable semantic chunks with overlap.
* **Embeddings:** Converts chunks into vector representations.
* **Vector Database:** Stores embeddings persistently for reuse.
* **Retrieval & QA:** Retrieves top-matching chunks and generates answers strictly from retrieved content.

## Frameworks & Libraries Used

* **Streamlit** – Web UI for URL input and chat interface
* **LangChain** – Orchestration for retrieval-based question answering
* **FAISS** – Local vector database for similarity search
* **HuggingFace Transformers / SentenceTransformers** – Embedding generation
* **BeautifulSoup4 & Requests** – Website crawling and HTML parsing

## LLM Model Used & Justification

* **Model:** Open-source instruction-following LLM (e.g., FLAN-T5 family)
* **Reason:** Free to use, lightweight, CPU-friendly, and suitable for retrieval-augmented QA without external API dependency.

## Vector Database Used & Justification

* **FAISS**
* **Reason:** Fast local similarity search, easy persistence, and ideal for small-to-medium datasets without external services.

## Embedding Strategy

* **Model:** HuggingFace sentence-transformers
* **Chunking:** Configurable chunk size with overlap to preserve semantic continuity
* **Metadata:** Each chunk stores source URL and page title (if available)
* **Persistence:** Embeddings are saved to disk and reused across sessions

## Question Answering Logic

* Users can ask natural language questions related to the indexed website.
* The system retrieves the most relevant chunks and generates answers strictly from them.
* **Fallback Rule:** If no relevant information is found, the chatbot responds exactly:

> **“The answer is not available on the provided website.”**

## Short-Term Memory

* Maintains conversational context within the current Streamlit session only.
* Resets automatically when the session ends.

## Setup & Run Instructions

### Prerequisites

* Python 3.10+

### Installation

```bash
git clone <repository-url>
cd website-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## Assumptions

* The website content is primarily HTML-based.
* JavaScript-heavy sites may have limited text extraction.

## Limitations

* Does not support non-HTML formats (PDF, DOCX).
* Performance depends on website size and quality of extracted text.

## Future Improvements

* Add sitemap-based crawling for multi-page websites
* Support additional file formats (PDF)
* Improve ranking with hybrid search (BM25 + vectors)
* Optional cloud deployment

---

**Company:** Humanli.ai


