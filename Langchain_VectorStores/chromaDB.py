from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

# Example documents
docs = [
    Document(page_content="Python is used for machine learning."),
    Document(page_content="Cricket is the most popular sport in India."),
    Document(page_content="Space exploration studies planets and galaxies.")
]

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create Chroma vector store
vector_store = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Query
query = "Tell me about sports"

results = vector_store.similarity_search(query, k=1)

for r in results:
    print(r.page_content)