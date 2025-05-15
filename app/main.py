from fastapi import FastAPI, UploadFile
from llm_pipeline import query_answer
from vector_store import ingest_document

app = FastAPI()


@app.post("/upload")
async def upload_pdf(file: UploadFile):
    content = await file.read()
    ingest_document(content)
    return {"status": "Document ingested."}


@app.get("/query")
def query(q: str):
    return {"answer": query_answer(q)}
