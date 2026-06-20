import yfinance as yf


def get_gold_price():
    gold = yf.Ticker("GC=F")

    data = gold.history(period="30d")

    current_price = data["Close"].iloc[-1]
    previous_price = data["Close"].iloc[-2]

    change = current_price - previous_price
    change_percent = (change / previous_price) * 100

    return {
        "price": round(current_price, 2),
        "change": round(change, 2),
        "change_percent": round(change_percent, 2)
    }