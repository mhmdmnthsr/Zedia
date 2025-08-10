import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

VECTOR_DIR = "vector_store"

def save_to_chroma(documents):
    embedding_function = OpenAIEmbeddings()
    db = Chroma.from_documents(documents, embedding_function, persist_directory=VECTOR_DIR)
    print(f"✅ Saved {len(documents)} chunks to ChromaDB")

def load_chroma():
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=VECTOR_DIR, embedding_function=embedding_function)
    return db

def get_retriever():
    embedding_function = OpenAIEmbeddings()
    vector_store = Chroma(
        persist_directory=VECTOR_DIR,
        embedding_function=embedding_function
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever