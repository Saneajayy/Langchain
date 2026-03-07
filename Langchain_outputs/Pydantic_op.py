# instead of schema , we send pydantic object, helps in validation.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

#define the model 
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description='Name of the Person')
    age:int = Field(gt=18, description='Age of the person')
    city:str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and the city of a fictional {place} person \n {format_instruction}',
    input_variables=['place']
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'Place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

# chain = template | model | parser
# final_result = chain.invoke({'Place':'British'})

print(final_result)

