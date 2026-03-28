"""
RAG Retriever — FAISS + Ollama Embeddings
Drop any .txt or .pdf medical docs into the /docs folder
"""

import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader

DOCS_DIR   = os.path.join(os.path.dirname(__file__), "docs")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "faiss_index")

embeddings = OllamaEmbeddings(model="llama3.2")


def build_index():
    """Build FAISS index from docs/ folder. Run once."""
    os.makedirs(DOCS_DIR, exist_ok=True)

    # Load all .txt and .pdf files
    docs = []
    for fname in os.listdir(DOCS_DIR):
        fpath = os.path.join(DOCS_DIR, fname)
        if fname.endswith(".pdf"):
            docs.extend(PyPDFLoader(fpath).load())
        elif fname.endswith(".txt"):
            docs.extend(TextLoader(fpath).load())

    if not docs:
        print("⚠️  No docs found in rag/docs/ — add .txt or .pdf files to enable RAG.")
        return None

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(INDEX_PATH)
    print(f"✅ FAISS index built with {len(chunks)} chunks from {len(docs)} documents.")
    return db


def load_index():
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return build_index()


def retrieve_context(query: str, k: int = 4) -> str:
    """Retrieve top-k relevant chunks for a given query."""
    db = load_index()
    if db is None:
        return "No medical knowledge base found. Using LLM knowledge only."
    docs = db.similarity_search(query, k=k)
    return "\n\n".join([d.page_content for d in docs])


if __name__ == "__main__":
    print("Building index...")
    build_index()
    print("\nTest retrieval:")
    print(retrieve_context("fever headache rash dengue"))
