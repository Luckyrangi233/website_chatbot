# qa.py
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

def create_qa_chain(vectordb):
    """
    Create a conversation-based retrieval chain with short-term memory.
    """
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
        memory=memory
    )

    return qa_chain


def ask_question(chain, question):
    """
    Ask a question via the chain.
    Returns fallback sentence if answer is missing.
    """
    result = chain({"question": question})
    answer = result["answer"].strip()

    if not answer or len(answer) < 5:
        return "The answer is not available on the provided website."
    return answer
