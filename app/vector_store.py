from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import tempfile

embedding = OpenAIEmbeddings()
vector_db = None


def ingest_document(content: bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(content)
        loader = PyPDFLoader(tmp.name)
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        global vector_db
        vector_db = FAISS.from_documents(chunks, embedding)


def search_similar(query: str):
    return vector_db.similarity_search(query, k=3) if vector_db else []
