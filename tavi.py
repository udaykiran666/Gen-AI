from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain_tavily import TavilySearch


# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     '''
#     Tool that searches over internet 
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     '''
#     print(f"searching for {query}")
#     return tavily.search(query=query)
#     # return "Tokyo weather is sunny"


llm = ChatOllama(model="llama3.2:3b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from main!!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an python developer using langchain in hyderabad, banglore on linkedln and list their details")]})
    print(result)


if __name__ == '__main__':
    main()