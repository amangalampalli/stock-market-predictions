import yfinance as yf

data = yf.download('WFC', '2012-03-01', '2022-02-08')

data.to_csv('data/WFC/WFC.csv')