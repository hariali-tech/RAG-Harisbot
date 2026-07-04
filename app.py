import streamlit as st
from rag_chain import get_rag_chain
from config import CHATBOT_NAME

st.set_page_config(page_title=f"{CHATBOT_NAME} Chat", page_icon="")
st.title(f" {CHATBOT_NAME} – Your Personal RAG Assistant")

# ================= Sidebar =================
with st.sidebar:
    st.title(" HarisBot")

    st.markdown("###  About")
    st.write(
        "Ask questions about your uploaded PDF and TXT documents using AI."
    )

    st.markdown("###  Features")
    st.write("- PDF Support")
    st.write("- TXT Support")
    st.write("- Semantic Search")
    st.write("- FAISS Vector Database")
    st.write("- Hugging Face LLM")
    st.write("- LangChain RAG")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Built by Haris Ali")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = get_rag_chain()

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me anything about your documents..."):

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build conversation history (last 6 messages)
    history = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in st.session_state.messages[-6:]
        ]
    )

    # Combine history with current question
    query = f"""
Conversation History:
{history}

Current Question:
{prompt}
"""

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.rag_chain.invoke(query)

        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

st.markdown("---")
st.caption("Built by Haris Ali | LangChain • FAISS • Hugging Face • Streamlit")