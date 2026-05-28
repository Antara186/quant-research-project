import pandas as pd
import numpy as np

# Load NSE universe
df = pd.read_csv("universe/nifty200.csv")

# Keep useful columns
df = df[["Symbol", "Industry"]]

# Create random momentum values
np.random.seed(42)

df["Momentum"] = np.random.uniform(
    -0.10,
    0.20,
    len(df)
)

# Rank stocks INSIDE each sector
df["Sector_Rank"] = (
    df.groupby("Industry")["Momentum"]
    .rank(ascending=False)
)

# Show first 20 rows
print(df.head(20))