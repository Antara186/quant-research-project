import pandas as pd

# Load stock data
df = pd.read_csv("data/ABB.csv")

# Check column names
print(df.columns)

# Convert Close column to numeric
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Calculate returns
df["Return"] = df["Close"].pct_change()

# Show result
print(df[["Close", "Return"]].head())

# Save file
df.to_csv("data/ABB_returns.csv", index=False)

print("Returns calculated successfully")
