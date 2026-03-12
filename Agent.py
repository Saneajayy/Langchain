from langchain_openai import ChatOpenAI
from langchain_community.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
import requests
import os
os.environ['OPEN_API_KEY'] = 'Ajhjd53qedbusvd73u78e568279_du32ygduqwdvyqtwd_3evecjjhdffgf'

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke('top news in india today')

llm = ChatOpenAI()

prompt = hub.pull("hwchase17/react") #pulls the standard React agent prompt

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=tool
)

response = agent_executor.invoke({"input": "3 ways to reach goa from delhi"})
print(response)

response['output']
