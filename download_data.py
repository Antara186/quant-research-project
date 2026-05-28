import pandas as pd
import yfinance as yf

# Load stock universe
df = pd.read_csv("universe/nifty200.csv")

# First 5 stocks
symbols = df["Symbol"].head(5)

# Download data
for stock in symbols:

    ticker = stock + ".NS"

    print(f"Downloading {ticker}...")

    data = yf.download(
        ticker,
        start="2024-01-01"
    )

    # Save data
    data.to_csv(f"data/{stock}.csv")

print("Download completed")
