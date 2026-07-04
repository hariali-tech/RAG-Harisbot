import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# First try Streamlit Secrets, then fall back to .env
HUGGINGFACEHUB_API_TOKEN = st.secrets.get(
    "HUGGINGFACEHUB_API_TOKEN",
    os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

CHATBOT_NAME = st.secrets.get(
    "CHATBOT_NAME",
    os.getenv("CHATBOT_NAME", "HarisBot")
)

DATA_PATH = "data/"
FAISS_INDEX_PATH = "faiss_index/"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

TOP_K = 8

MAX_NEW_TOKENS = 512
