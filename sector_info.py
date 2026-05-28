import pandas as pd

# Load NSE universe
df = pd.read_csv("universe/nifty200.csv")

# Show only Symbol and Industry
print(df[["Symbol", "Industry"]].head(10))