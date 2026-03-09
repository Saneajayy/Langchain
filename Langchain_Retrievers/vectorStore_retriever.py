from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="Python is a programming language."),
    Document(page_content="Cricket is a very popular sport in India."),
    Document(page_content="Space exploration studies planets and galaxies.")
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

query = "Tell me about sports"

results = vector_store.similarity_search(query, k=1)


for doc in results:
    print(doc.page_content)