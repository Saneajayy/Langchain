from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever

# Sample documents
docs = [
    Document(page_content="LangChain is a framework for building LLM applications."),
    Document(page_content="Vector databases store embeddings for semantic search."),
    Document(page_content="RAG stands for Retrieval Augmented Generation."),
    Document(page_content="Retrievers fetch relevant information from vector databases.")
]

embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)


llm = ChatOpenAI()

# Create MultiQuery Retriever
retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)

query = "What is LangChain?"

results = retriever.invoke(query)

for doc in results:
    print(doc.page_content)