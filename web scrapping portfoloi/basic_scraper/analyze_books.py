import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("books_data.csv")

print("First 5 rows:")
print(df.head())

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)


# Convert rating text to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Basic Analysis
avg_price = df["Price"].mean()
max_price = df["Price"].max()
min_price = df["Price"].min()

print("Average Price:", avg_price)
print("Max Price:", max_price)
print("Min Price:", min_price)

# Top expensive books
top = df.sort_values("Price", ascending=False).head(10)

# Plot
plt.figure()
plt.barh(top["Title"], top["Price"])
plt.xlabel("Price (£)")
plt.title("Top 10 Most Expensive Books")
plt.tight_layout()
plt.show()
