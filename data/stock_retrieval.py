import yfinance as yf

data = yf.download('XOM', '2012-03-01', '2022-02-08')

data.to_csv('data/XOM/XOM.csv')