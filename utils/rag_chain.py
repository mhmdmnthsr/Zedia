from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

VECTOR_DIR = "vector_store"

def get_rag_chain():
    vector_store = Chroma(
        persist_directory=VECTOR_DIR,
        embedding_function=OpenAIEmbeddings()
        )


    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model="gpt-4")

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return rag_chain

