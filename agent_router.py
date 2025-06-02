from utils.classifier import classify_query
from tools.factual_tools import search_web, scrape_url
from tools.calculator_tool import calculator_tool
from tools.comparison_tool import comparison_tool
from tools.definition_tool import definition_tool
from config.llm_config import llm
from langchain.agents import initialize_agent, AgentType

def run_agent(query: str) -> str:
    query_type = classify_query(query)
    print(f"\n🔍 Detected query type: {query_type.upper()}")

    tools = []
    prompt = query

    if query_type == "factual":
        tools = [search_web, scrape_url]
        prompt = f'Search the web for: "{query}".\nScrape the top 2 results. Summarize with proper citations like [1], [2].'

    elif query_type == "analytical":
        tools = [calculator_tool]
        prompt = f"Compute and explain step by step: {query}"

    elif query_type == "comparison":
        tools = [comparison_tool]

    elif query_type == "definition":
        tools = [definition_tool]

    else:
        return "❗ Could not classify the query. Please rephrase."

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent.run(prompt)
