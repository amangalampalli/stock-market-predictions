import yfinance as yf
import threading

Forex = [
    "AUDCAD",
    "AUDJPY",
    "AUDNZD",
    "AUDCHF",
    "AUDUSD",
    "CADJPY",
    "CADCHF",
    "EURAUD",
    "EURCAD",
    "EURGBP",
    "EURJPY",
    "EURNZD",
    "EURCHF",
    "EURUSD",
    "GBPAUD",
    "GBPCAD",
    "GBPJPY",
    "GBPNZD",
    "GBPCHF",
    "GBPUSD",
    "NZDCAD",
    "NZDJPY",
    "NZDCHF",
    "NZDUSD",
    "CHFJPY",
    "USDCAD",
    "USDJPY",
    "USDCHF",
]

Commodities = [
    "BRENT",
    "ARABICA",
    "ROBUSTA",
    "COPPER",
    "COTTON",
    "GOLD",
    "ORANGE.JUICE",
    "PALLADIUM",
    "PLATINUM",
    "SUGAR.RAW",
    "SILVER",
    "COCOA",
    "NGAS",
    "CRUDOIL",
    "WTI",
    "SUGAR.WHITE",
]

Indicies = [
    "ASX200",
    "CAC40",
    "Canada60",
    "DAX40",
    "DJI30",
    "STOXX50",
    "FTSE100",
    "MDAX50",
    "TECDAX30",
    "IBEX35",
    "NQ100",
    "AEX25",
    "JP225",
    "SP500",
    "SMI20",
]

# Merge all the lists together into one big list
All_Tickers = Forex + Commodities + Indicies

# Use threading to download 15 minute intervals from each ticker in All_Tickers
# This will take a while


def download_data(ticker):
    try:
        data = yf.download(ticker, period="1d", interval="15m")
        data.to_csv(f"data/{ticker}.csv")
    except:
        print(f"{ticker} failed to download")


# Run the download function for each ticker in All_Tickers using threading
threads = []
for ticker in All_Tickers:
    t = threading.Thread(target=download_data, args=(ticker,))
    threads.append(t)
    t.start()

# Close all threads that are done downloading
for t in threads:
    t.join()
