import yfinance as yf

def get_markets():
    tickers = {
        "SP500": "^GSPC",
        "NASDAQ": "^IXIC",
        "DAX": "^GDAXI",
        "NIKKEI": "^N225"
    }

    result = {}

    for name, ticker in tickers.items():
        data = yf.Ticker(ticker).history(period="5d")
        if len(data) >= 2:
            last = data["Close"].iloc[-1]
            prev = data["Close"].iloc[-2]
            result[name] = round(((last - prev) / prev) * 100, 2)

    return result
