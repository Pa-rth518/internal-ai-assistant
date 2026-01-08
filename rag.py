import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

load_dotenv()


PROMPT_TEMPLATE = """
You are an internal company AI assistant.

Rules:
- Start every answer with: "Listen Parth,"
- Answer in one complete, grammatically correct sentence.
- Do NOT add any extra information beyond what is asked.
- Do NOT rephrase the question.
- Use ONLY the provided context.
- If the answer is not explicitly present in the context, say exactly:
  "I don't have enough information."

Context:
{context}

Question:
{question}
"""



def get_answer(query):
    embeddings = FastEmbedEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    docs = vectordb.similarity_search(query, k=6)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=query
    )

    response = llm.invoke(prompt)
    return response.content
