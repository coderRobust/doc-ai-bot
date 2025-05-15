import streamlit as st
import requests

st.title("📄 Ask your Document")
file = st.file_uploader("Upload your PDF")
if file:
    response = requests.post(
        "http://localhost:8000/upload", files={"file": file})
    st.success("File uploaded")

query = st.text_input("Ask a question")
if query:
    answer = requests.get("http://localhost:8000/query",
                          params={"q": query}).json()
    st.write("Answer:", answer["answer"])
