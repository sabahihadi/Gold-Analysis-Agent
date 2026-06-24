import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


def get_gold_history(days=30):
    """
    Returns historical gold prices for charting.
    """

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "XAUUSD",
        "apikey": API_KEY
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(
            f"Alpha Vantage Error: {data}"
        )

    series = data["Time Series (Daily)"]

    dates = list(series.keys())[:days]

    dates.reverse()

    prices = [
        float(series[d]["4. close"])
        for d in dates
    ]

    return {
        "dates": dates,
        "prices": prices
    }


def get_gold_price():
    """
    Returns summary data for LLM analysis.
    """

    history = get_gold_history(days=7)

    prices = history["prices"]

    current_price = prices[-1]

    weekly_change = (
        (prices[-1] - prices[0])
        / prices[0]
    ) * 100

    return {
        "current_price": round(current_price, 2),
        "weekly_prices": prices,
        "weekly_change_percent": round(
            weekly_change,
            2
        )
    }