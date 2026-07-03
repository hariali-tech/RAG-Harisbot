from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from config import HUGGINGFACEHUB_API_TOKEN, CHATBOT_NAME
from embedding import create_or_load_vectorstore


def format_docs(docs):

    if not docs:
        return ""

    formatted=[]

    for i,doc in enumerate(docs):

        formatted.append(

            f"""
Source {i+1}

{doc.page_content}
"""

        )

    return "\n".join(formatted)


def get_rag_chain():
    vectorstore = create_or_load_vectorstore()
    retriever = vectorstore.as_retriever(

        search_type="similarity_score_threshold",

        search_kwargs={
            "score_threshold": 0.5,
            "k": 8
        }

    )

    print("🤖 Loading Hugging Face LLM (free)...")

    endpoint = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        temperature=0.1,
        max_new_tokens=700,
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    ...

    llm = ChatHuggingFace(llm=endpoint)

    template = """
    You are {bot_name}, an intelligent AI assistant.

    Your task is to answer questions ONLY using the provided context.

    Instructions:
    - Read ALL the context carefully before answering.
    - Combine information from multiple context sections if needed.
    - Give complete, detailed, and well-structured answers.
    - Use bullet points when listing information.
    - Do NOT make up or assume information that is not in the context.
    - If only part of the answer exists, provide all available information.
    - If the answer is not found in the context, reply exactly:

    "I don't have that information in my documents."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = ChatPromptTemplate.from_template(template)

    ...

    # Function to add bot_name
    def add_bot_name(input_dict):
        return {
            "context": input_dict["context"],
            "question": input_dict["question"],
            "bot_name": CHATBOT_NAME
        }

    # Chain with bot_name
    chain = (
            {
                "context": retriever | RunnableLambda(format_docs),
                "question": RunnablePassthrough()
            }
            | RunnableLambda(add_bot_name)
            | prompt
            | llm
            | StrOutputParser()
    )
    return chain