from tavily import TavilyClient
import os


client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def get_gold_news():

    query = """
    Gold price today, Federal Reserve interest rates,
    inflation data, DXY index, geopolitical tensions
    """

    results = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return results["results"]