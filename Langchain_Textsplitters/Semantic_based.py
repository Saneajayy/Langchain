from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample_text = """Space missions are helping scientists search for life on Mars. Cricket fans were excited after the team won the last over thriller yesterday. Farmers across many regions depend heavily on monsoon rains for their crops. Smartphones have become an essential tool for communication and work. Mountains attract thousands of travelers who enjoy trekking and adventure.

Artificial intelligence is rapidly changing how software is developed. Street food vendors often serve some of the most flavorful dishes in cities. Football is one of the most popular sports watched around the world. Many students prefer studying late at night when it is quiet. Electric cars are becoming more common as countries focus on cleaner energy."""

docs = text_splitter.create_documents([sample_text])
print(len(docs))
print(docs)