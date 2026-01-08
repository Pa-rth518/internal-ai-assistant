from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma

def ingest_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if not documents or all(not d.page_content.strip() for d in documents):
        raise ValueError(
            "PDF has no extractable text. Please upload a text-based PDF."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    texts = [doc.page_content for doc in chunks if doc.page_content.strip()]

    embeddings = FastEmbedEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    vectordb = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        persist_directory="db"
    )

    vectordb.persist()
