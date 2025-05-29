import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Base directory and vectorstore path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VECTORSTORE_PATH = os.path.join(BASE_DIR, "vectorstore")

# Embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Build FAISS index from a single file
def build_faiss_index(file_path: str):
    loader = TextLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTORSTORE_PATH)
    print("✅ FAISS index created & saved at", VECTORSTORE_PATH)

# Query from the index
def query_index(query: str, k=3):
    faiss_file = os.path.join(VECTORSTORE_PATH, "index.faiss")
    if not os.path.exists(faiss_file):
        raise FileNotFoundError(f"❌ FAISS index not found at {faiss_file}. Please run build_faiss_index() first.")
    
    db = FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=k)
    return [r.page_content for r in results]
