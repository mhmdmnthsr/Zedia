from utils.pdf_loader import load_and_split_pdfs
from utils.vector_store import save_to_chroma
from utils.rag_chain import get_rag_chain
import click
import json
import os
from dotenv import load_dotenv

load_dotenv()

@click.group()
def cli():
    pass

@cli.command()
def read():

    print("📥 Loading and splitting PDFs...")
    docs = load_and_split_pdfs()

    if not docs:
        print("⚠️ All the PDFs are already read.")
        return
    print(f"✅ Loaded and split {len(docs)} chunks.")

    print("💾 Saving to Chroma vector store...")
    save_to_chroma(docs)
    print("✅ Done!")

@cli.command()
def query():
    rag_chain = get_rag_chain()
    
    print("🤖 What do you want from the PDF (type 'exit' to quit):")

    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break

        result = rag_chain.invoke({"query": q})
        print("\n🧠 Answer:")
        print(result["result"])
        
        print("\n📚 Sources:")
        sources = {doc.metadata.get('source', 'Unknown') for doc in result["source_documents"]}
        for source in sources:
            print(source)

@cli.command()
def list():
    PDF_DIR = "pdfs"

    if not os.path.isdir(PDF_DIR):
        print(f"⚠️ Folder '{PDF_DIR}' not found.")
        return

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDFs found in the folder.")
        return

    print("📚 PDFs in folder:")
    for file in pdf_files:
        print(f"  - {file}")



if __name__ == "__main__":
    cli()
