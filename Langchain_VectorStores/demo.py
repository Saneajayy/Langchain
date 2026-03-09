from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="Python is a programming language."),
    Document(page_content="Cricket is a popular sport in India."),
    Document(page_content="Space exploration studies planets and galaxies."),
]

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vector_store = FAISS.from_documents(docs, embeddings)

# Query the vector store
query = "Tell me about sports"

results = vector_store.similarity_search(query, k=1)

for r in results:
    print(r.page_content)

# Cricket is a popular sport in India. ----- this will be the result 