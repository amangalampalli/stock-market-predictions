import yfinance as yf

data = yf.download('MSFT', '2012-03-01', '2022-02-08')

data.to_csv('data/MSFT/MSFT.csv')