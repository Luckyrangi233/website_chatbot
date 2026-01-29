import streamlit as st
from crawler import crawl_website
from chunking import chunk_text
from vector_store import create_or_load_vectorstore
from qa import create_qa_chain, ask_question

# Function to block unsupported URLs
def is_supported_url(url):
    unsupported_patterns = [
        "youtube.com",
        "youtu.be",
        "facebook.com",
        "instagram.com",
        "twitter.com",
        "linkedin.com"
    ]
    return not any(p in url.lower() for p in unsupported_patterns)

st.set_page_config(page_title="Website Chatbot")
st.title("Website-Based AI Chatbot")

url = st.text_input("Enter Website URL")

if st.button("Index Website"):
    if not url:
        st.error("Please enter a website URL.")
    elif not is_supported_url(url):
        st.error("This website is not supported. Please provide a static HTML website.")
    else:
        with st.spinner("Indexing website..."):
            docs = crawl_website(url)
            if not docs:
                st.error("No readable content found on this website.")
            else:
                chunks = chunk_text(docs)
                vectordb = create_or_load_vectorstore(chunks)
                st.session_state.qa_chain = create_qa_chain(vectordb)
                st.success("Website indexed successfully!")

if "qa_chain" in st.session_state:
    query = st.chat_input("Ask a question")
    if query:
        st.chat_message("user").write(query)
        answer = ask_question(st.session_state.qa_chain, query)
        st.chat_message("assistant").write(answer)
