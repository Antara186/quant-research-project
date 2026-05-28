import pandas as pd

# Load data
df = pd.read_csv("data/ABB.csv")

# Convert Close to numeric
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Calculate 20-day momentum
df["Momentum_20"] = (
    df["Close"] / df["Close"].shift(20)
) - 1

# Show output
print(df[["Close", "Momentum_20"]].tail())

# Save file
df.to_csv("data/ABB_momentum.csv", index=False)

print("Momentum factor calculated")
