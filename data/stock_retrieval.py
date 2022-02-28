import yfinance as yf

data = yf.download('MSFT', '1940-03-01', '2022-02-27')

data.to_csv('data/MSFT/MSFT.csv')