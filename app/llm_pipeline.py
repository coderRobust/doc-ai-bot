from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from vector_store import search_similar

llm = OpenAI(temperature=0)
chain = load_qa_chain(llm, chain_type="stuff")


def query_answer(query: str):
    docs = search_similar(query)
    return chain.run(input_documents=docs, question=query)
