import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("all_books_data.csv")

print("Dataset shape:", df.shape)
print(df.head())

# Clean Price
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

# Convert Rating to numeric
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Basic statistics
print("\nAverage Price:", df["Price"].mean())
print("Max Price:", df["Price"].max())
print("Min Price:", df["Price"].min())

# Most expensive books
top_expensive = df.sort_values("Price", ascending=False).head(10)
print("\nTop 10 Expensive Books:")
print(top_expensive[["Title", "Price"]])

# Rating distribution
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure()
rating_counts.plot(kind="bar")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()
