# 🧠 Personal RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that answers questions based on your own documents. This project uses LangChain, FAISS, Hugging Face models, and Streamlit to provide accurate, context-aware responses from uploaded PDF and text files.

---

## 🚀 Features

- 📄 Supports PDF and TXT documents
- 🔍 Semantic document retrieval using FAISS
- 🤖 Hugging Face LLM integration
- 💬 Interactive chat interface with Streamlit
- 🧠 Context-aware document question answering
- ⚡ Fast local vector search
- 📚 Automatic document chunking
- 🔄 Persistent FAISS vector database
- 🎯 Retrieval-Augmented Generation (RAG) pipeline

---

## 🏗️ Project Structure

```
Personal-RAG-Assistant/
│
├── app.py                 # Streamlit application
├── rag_chain.py           # LangChain RAG pipeline
├── embedding.py           # FAISS vector database
├── data_loader.py         # Document loading & chunking
├── config.py              # Configuration settings
├── requirements.txt
│
├── data/                  # PDF & TXT documents
├── faiss_index/           # Generated FAISS index
│
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Hugging Face
- FAISS
- Sentence Transformers
- PyPDF
- Transformers
- Torch

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Personal-RAG-Assistant.git
```

Go into the project

```bash
cd Personal-RAG-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
HUGGINGFACEHUB_API_TOKEN=YOUR_API_KEY
CHATBOT_NAME=HarisBot
```

Run the application

```bash
streamlit run app.py
```

---

## 📂 Supported Documents

- PDF
- TXT

Simply place your documents inside the `data/` folder.

---

## 🔄 Workflow

```
Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Hugging Face LLM
      │
      ▼
Answer
```

---

## 📸 Screenshots

(Add screenshots of your chatbot here.)

---

## 👨‍💻 Author

**Haris Ali**

Software Engineering Student

Interested in AI • NLP • Machine Learning • Python

---

## 📄 License

This project is licensed under the MIT License.