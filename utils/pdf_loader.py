import os
from unstract.llmwhisperer import LLMWhispererClientV2
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

PDF_DIR = "pdfs"

def extract_text_from_pdf(file_path: str) -> str:
    client = LLMWhispererClientV2()
    try:
        result = client.whisper(
            file_path=file_path,
            wait_for_completion=True,
            wait_timeout=200
        )
        return result["extraction"]["result_text"]
    except Exception as e:
        print(f"❌ Error extracting {file_path}: {e}")
        return ""

def load_and_split_pdfs():
    all_docs = []

    if not os.path.isdir(PDF_DIR):
        print(f"⚠️ Folder '{PDF_DIR}' not found.")
        return all_docs

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDFs found.")
        return all_docs

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    for file in pdf_files:
        path = os.path.join(PDF_DIR, file)
        print(f"📄 Extracting: {file}")
        text = extract_text_from_pdf(path)
        if text.strip():
            doc = Document(page_content=text, metadata={"source": file})
            split_docs = splitter.split_documents([doc])
            all_docs.extend(split_docs)

    return all_docs
