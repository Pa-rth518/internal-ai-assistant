import streamlit as st
from ingest import ingest_pdf
from rag import get_answer

st.set_page_config(page_title="Internal AI Knowledge Assistant")

st.title("📄 Internal AI Knowledge Assistant")

pdf = st.file_uploader("Upload PDF", type=["pdf"])

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())
    st.success("PDF uploaded")

    if st.button("Process Document"):
        ingest_pdf("temp.pdf")
        st.success("Document processed")

query = st.text_input("Ask a question")

if st.button("Get Answer") and query:
    answer = get_answer(query)
    st.write("### Answer")
    st.write(answer)
