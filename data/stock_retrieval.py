import yfinance as yf

data = yf.download('RBLX', '2021-03-01', '2022-02-08')

data.to_csv('data/Roblox/RBLX.csv')