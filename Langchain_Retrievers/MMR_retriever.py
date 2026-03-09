from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Example documents
docs = [
    Document(page_content="LangChain is a framework for building LLM applications."),
    Document(page_content="Vector databases store embeddings for semantic search."),
    Document(page_content="Retrievers help fetch relevant documents."),
    Document(page_content="LangChain supports RAG pipelines.")
]


embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5}
)

query = "What is LangChain?"

results = retriever.invoke(query)


for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print(doc.page_content)