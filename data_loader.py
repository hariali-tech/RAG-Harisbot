from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from config import DATA_PATH

def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)
        if file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
        elif file.endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            continue
        docs.extend(loader.load())
    return docs

def split_documents(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )
    return splitter.split_documents(docs)