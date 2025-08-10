# 📄 ZEDIA (PDF RAG Chatbot)

A CLI-based Retrieval-Augmented Generation (RAG) system that lets you **upload PDFs**, extract & chunk their text, embed into a **Chroma vector store**, and query them using **OPEN AI**.

---

## 🚀 Features
- 📥 **Extract text from PDFs** using [Unstract LLM Whisperer](https://docs.unstract.com/).
- ✂️ **Split documents into chunks** with LangChain’s `RecursiveCharacterTextSplitter`.
- 🧠 **Embed text** using `OpenAIEmbeddings` and store in ChromaDB.
- 🤖 **Query PDFs** interactively with GPT-4.
- 🗄 **Persist embeddings** for fast retrieval across sessions.
- 💻 **CLI commands** for reading, querying, and managing PDFs.

---

## 📦 Project Structure

```
.
├── main.py                     # CLI entry point
├── utils/
│   ├── pdf_loader.py           # Extracts & splits PDF text
│   ├── vector_store.py         # Saves/loads Chroma vector store
│   ├── rag_chain.py            # Creates RetrievalQA chain
├── pdfs/                       # Folder containing PDFs to read
├── vector_store/               # ChromaDB storage
├── requirements.txt            # Python dependencies
└── .env                        # API keys & environment variables
```

---

## ⚙️ Installation

1️⃣ **Clone the repo**
```bash
git clone https://github.com/mhmdmnthsr/Zedia.git
cd Zedia
```

2️⃣ **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

4️⃣ **Set up environment variables**

Create a `.env` file:
```ini
OPENAI_API_KEY=your_openai_api_key
LLM_WHISPERER_API_KEY=your_llmwhisperer_api_key
```

---

## 📜 Usage

### **1. Add PDFs**
Place all PDFs you want to query inside the `pdfs/` folder.

### **2. Read & Embed PDFs**
```bash
python main.py read
```
- Extracts text from all PDFs in `pdfs/`
- Splits text into chunks
- Saves chunks into ChromaDB

### **3. Query PDFs**
```bash
python main.py query
```
Example:
```
🤖 What do you want from the PDF (type 'exit' to quit):
You: What is the main conclusion of the report?
🧠 Answer:
The report concludes that...
📚 Sources:
report.pdf
```

---

## 🛠 Commands

| Command | Description |
|---------|-------------|
| `python main.py read` | Extracts & embeds all PDFs from the `pdfs/` folder |
| `python main.py query` | Starts interactive chat to query embedded PDFs |
| `python main.py list` | Lists all PDFs that have been embedded |

---

## 🧩 Tech Stack
- **[LangChain](https://www.langchain.com/)** — Text splitting, document handling, and RAG chain
- **[ChromaDB](https://www.trychroma.com/)** — Vector database for embeddings
- **[OpenAI GPT-4](https://platform.openai.com/)** — Answer generation
- **[Unstract LLM Whisperer](https://docs.unstract.com/)** — PDF text extraction

---

## 📌 Notes
- All PDFs are processed fresh every time 
- ChromaDB persists embeddings in `vector_store/` for faster queries.
- Adjust `chunk_size` and `chunk_overlap` in `pdf_loader.py` for different document sizes.
