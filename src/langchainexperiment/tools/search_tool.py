from langchain.tools import tool
from tavily import TavilyClient
from langchainexperiment.util.get_env_var import get_env_var


@tool
def search_tool(query:str) -> dict:
    """
    Search the internet for information related to the user's query.
    
    Args:
        query: Search terms to look for
    """
    tavily_client = TavilyClient(api_key= get_env_var("TAVILY_API_KEY"))
    response = tavily_client.search(query, search_depth= "basic", max_results = 3)
    return response


