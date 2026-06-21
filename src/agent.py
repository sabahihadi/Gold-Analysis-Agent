from src.market_data import get_gold_price
from src.news_fetcher import get_gold_news
from src.llm_engine import generate_response


class GoldAnalysisAgent:

    def ask(self, user_question):

        market_data = get_gold_price()

        news = get_gold_news()

        answer = generate_response(
            user_question,
            market_data,
            news
        )

        return answer