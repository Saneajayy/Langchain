'''from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):

    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. there are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this""")

print(result)'''

#this code uses hugging face APIs.

from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

# Load Hugging Face model
model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    max_new_tokens=200,
)

# schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
"""The hardware is great, but the software feels bloated. 
there are too many pre-installed apps that I can't remove. 
Also, the UI looks outdated compared to other brands. 
Hoping for a software update to fix this"""
)

print(result)