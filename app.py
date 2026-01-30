# rebuild trigger

import streamlit as st

from crawler import crawl_website
from chunking import chunk_text
from vector_store import create_or_load_vectorstore
from qa import create_qa_chain, ask_question

st.set_page_config(page_title="Website Chatbot", layout="wide")

st.title("🌐 Website-Based Chatbot")

url = st.text_input("Enter Website URL")

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if st.button("Index Website"):
    if not url:
        st.error("Please enter a valid URL")
    else:
        with st.spinner("Crawling website..."):
            docs = crawl_website(url)

        with st.spinner("Processing content..."):
           full_text = "\n".join(docs)
           chunks = chunk_text(full_text)


        with st.spinner("Creating embeddings..."):
            vectordb = create_or_load_vectorstore(chunks)
            st.session_state.qa_chain = create_qa_chain(vectordb)

        st.success("Website indexed successfully!")

query = st.chat_input("Ask a question about the website")

if query and st.session_state.qa_chain:
    answer = ask_question(st.session_state.qa_chain, query)
    st.chat_message("assistant").write(answer)
