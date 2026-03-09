from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Sample documents
docs = [
    Document(page_content="LangChain is a framework used for building LLM applications."),
    Document(page_content="Vector databases are used to store embeddings for semantic search."),
    Document(page_content="RAG stands for Retrieval Augmented Generation.")
]

# Create embeddings
embedding = OpenAIEmbeddings()

# Create vector store
vectorstore = FAISS.from_documents(docs, embedding)

# Base retriever
retriever = vectorstore.as_retriever()

# LLM
llm = ChatOpenAI()

# Compressor
compressor = LLMChainExtractor.from_llm(llm)

# Contextual Compression Retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=retriever,
    base_compressor=compressor
)

# Query
query = "What is LangChain?"

results = compression_retriever.invoke(query)

for doc in results:
    print(doc.page_content)