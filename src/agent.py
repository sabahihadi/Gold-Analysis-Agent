from src.market_data import get_gold_price
from src.news_fetcher import get_gold_news
from src.llm_engine import generate_response


class GoldAnalysisAgent:

    def ask(self, question: str):

        market_data = get_gold_price()

        if "error" in market_data:

            return (
                f"Unable to retrieve market data.\n\n"
                f"Error: {market_data['error']}"
            )

        news = get_gold_news()

        return generate_response(
            question,
            market_data,
            news
        )