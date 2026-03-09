from langchain_community.retrievers import WikipediaRetriever

# Initialize retriever
retriever = WikipediaRetriever(
    top_k_results=2,   # number of articles to fetch
    lang="en"
)

query = "history of India and Pakistan"


docs = retriever.invoke(query)


for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print("Title:", doc.metadata.get("title"))
    print("Content:", doc.page_content[:500])  # print first 500 chars