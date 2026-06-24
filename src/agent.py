from src.market_data import get_gold_price
from src.news_fetcher import get_gold_news
from src.llm_engine import generate_response
from src.language import detect_language

class GoldAnalysisAgent:

    def ask(self, question: str):

        market_data = get_gold_price()

        if "error" in market_data:

            return (
                f"Unable to retrieve market data.\n\n"
                f"Error: {market_data['error']}"
            )

        news = get_gold_news()

        lang = detect_language(question)
       
        return generate_response(
            question,
            market_data,
            news,
            lang
        )