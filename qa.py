from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def create_qa_chain(vectordb):
    llm_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=512
    )

    llm = HuggingFacePipeline(pipeline=llm_pipeline)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(),
        memory=memory
    )

def ask_question(chain, question):
    result = chain({"question": question})
    answer = result["answer"]

    if not answer.strip():
        return "The answer is not available on the provided website."

    return answer
