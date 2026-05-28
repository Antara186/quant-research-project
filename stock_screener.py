import pandas as pd
import numpy as np

# Load stock universe
df = pd.read_csv("universe/nifty200.csv")

# Keep columns
df = df[["Symbol", "Industry"]]

# Generate sample momentum
np.random.seed(42)

df["Momentum"] = np.random.uniform(
    -0.10,
    0.20,
    len(df)
)

# Rank within sectors
df["Sector_Rank"] = (
    df.groupby("Industry")["Momentum"]
    .rank(ascending=False)
)

# Select top stocks from each sector
top_stocks = df[df["Sector_Rank"] <= 3]

# Sort results
top_stocks = top_stocks.sort_values(
    by=["Industry", "Sector_Rank"]
)

# Show results
print(top_stocks.head(30))