📘 Internal AI Knowledge Assistant (RAG-based)

An AI-powered internal knowledge assistant built using Retrieval-Augmented Generation (RAG) that allows users to upload documents and ask questions based strictly on the document content.
The system ensures no hallucinations and returns answers only when supported by retrieved context.

🚀 Features

📄 Upload text-based PDF documents

✂️ Automatic text extraction and chunking

🧠 Semantic search using vector embeddings

🔎 Retrieval-Augmented Generation (RAG) pipeline

🤖 Low-latency LLM responses using Groq

🚫 Hallucination control with strict prompt rules

💬 Clean and interactive Streamlit UI

🧩 System Architecture

The application follows a standard RAG (Retrieval-Augmented Generation) workflow:

PDF documents are loaded and processed

Text is split into overlapping chunks

Chunks are converted into vector embeddings

Embeddings are stored in a vector database

User queries retrieve relevant chunks

The LLM generates answers strictly from retrieved context

(Architecture diagram added in the repository)

🛠️ Tech Stack

Python

Streamlit – UI

LangChain – Document processing & RAG orchestration

ChromaDB – Vector database

FastEmbed – Embeddings

Groq API – LLM inference (Llama 3.1)

dotenv – Environment variable management
