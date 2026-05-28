import pandas as pd

# Create sample sector data
data = {
    "Symbol": ["ABB", "APLAPOLLO", "AUBANK", "ADANIENSOL"],
    "Sector": [
        "Capital Goods",
        "Capital Goods",
        "Financial Services",
        "Power"
    ],
    "Momentum": [0.12, 0.08, 0.15, -0.03]
}

df = pd.DataFrame(data)

# Rank inside each sector
df["Sector_Rank"] = df.groupby("Sector")["Momentum"].rank(
    ascending=False
)

# Show result
print(df)
