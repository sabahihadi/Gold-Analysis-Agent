import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


def get_gold_price():

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "XAUUSD",
        "apikey": API_KEY
    }

    response = requests.get(url, params=params, timeout=20)

    data = response.json()

    series = data["Time Series (Daily)"]

    dates = list(series.keys())[:7]

    prices = [
        float(series[d]["4. close"])
        for d in dates
    ]

    current_price = prices[0]

    weekly_change = (
        (prices[0] - prices[-1]) / prices[-1]
    ) * 100

    return {
        "current_price": current_price,
        "weekly_prices": prices,
        "weekly_change_percent": round(weekly_change, 2)
    }