import time
import yfinance as yf


def get_gold_price(retries=3, delay=5):

    for attempt in range(retries):

        try:
            gold = yf.Ticker("GC=F")

            data = gold.history(period="5d")

            if data.empty:
                raise ValueError("No data returned.")

            current_price = float(data["Close"].iloc[-1])
            previous_price = float(data["Close"].iloc[-2])

            change = current_price - previous_price
            change_percent = (change / previous_price) * 100

            return {
                "price": round(current_price, 2),
                "change": round(change, 2),
                "change_percent": round(change_percent, 2)
            }

        except Exception as e:

            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return {
                    "error": str(e)
                }