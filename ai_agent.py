import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()


def create_agent(llm_id, allow_search, system_prompt, provider):
    """Create an AI agent with optional web search tools."""

    if provider == "groq":
        llm = ChatGroq(model=llm_id, api_key=os.getenv("GROQ_API_KEY"))
    else:
        raise ValueError(f"Provider '{provider}' not supported yet.")

    tools = (
        [TavilySearch(max_results=2, api_key=os.getenv("TAVILY_API_KEY"))]
        if allow_search
        else []
    )

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )
    return agent


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    """Helper function to create an agent, run a query, and return response."""

    agent = create_agent(llm_id, allow_search, system_prompt, provider)

    state = {"messages": [HumanMessage(content=query)]}
    response = agent.invoke(state)

    ai_messages = [m.content for m in response["messages"] if isinstance(m, AIMessage)]
    return {"response": ai_messages[-1] if ai_messages else None}
