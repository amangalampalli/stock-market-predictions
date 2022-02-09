import yfinance as yf

data = yf.download('RBLX', '2021-03-01', '2022-02-08')

data.filter(['Date', 'Open']).to_csv('data/RBLX.csv')