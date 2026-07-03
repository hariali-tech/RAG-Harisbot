from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import FAISS_INDEX_PATH
from data_loader import load_documents, split_documents
import os
import shutil


def create_or_load_vectorstore():
    # Use FREE Hugging Face embeddings
    print(" Loading Hugging Face embeddings (free)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5",
        model_kwargs={"device": "cpu"},
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    # Check if index exists
    index_exists = os.path.exists(FAISS_INDEX_PATH) and \
                   os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.faiss"))

    if index_exists:
        print("📂 Loading existing FAISS index...")
        return FAISS.load_local(
            FAISS_INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        print("🆕 Creating new FAISS index from documents...")

        # Delete old index if corrupted
        if os.path.exists(FAISS_INDEX_PATH):
            shutil.rmtree(FAISS_INDEX_PATH)

        docs = load_documents()
        if not docs:
            raise ValueError("❌ No documents found in 'data/' folder!")

        chunks = split_documents(docs)
        if not chunks:
            raise ValueError("❌ No chunks created!")

        print(f"📄 Creating embeddings for {len(chunks)} chunks...")
        vectorstore = FAISS.from_documents(chunks, embeddings)

        os.makedirs(FAISS_INDEX_PATH, exist_ok=True)
        vectorstore.save_local(FAISS_INDEX_PATH)
        print(f"✅ Index saved to {FAISS_INDEX_PATH}")

        return vectorstore