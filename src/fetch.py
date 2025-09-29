import yfinance as yf 
# Test fetching basic data for one ticker (revenue, net income).

symbols = {"Apple" : 'AAPL' }
apple_symbol = 'AAPL'
ticker = yf.Ticker(apple_symbol)

hist_data = ticker.history(period = '1d')
# print(f"Data: {hist_data}")
print(ticker.calendar )
