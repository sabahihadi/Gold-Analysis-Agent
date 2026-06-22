import yfinance as yf

gold = yf.Ticker("GC=F")

data = gold.history(period="1d")

print(data.tail())