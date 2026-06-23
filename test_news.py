from src.news_fetcher import get_gold_news

news = get_gold_news()

for item in news:
    print(item)