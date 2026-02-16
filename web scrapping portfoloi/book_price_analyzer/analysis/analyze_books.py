import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/books.csv")

df["Price"] = df["Price"].astype(float)

print("Average Price:", round(df["Price"].mean(), 2))

top = df.sort_values("Price", ascending=False).head(10)

print("\nTop 10 Expensive Books:")
print(top[["Title", "Price"]])

plt.figure()
plt.hist(df["Price"], bins=15)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Count")

plt.savefig("../visuals/price_chart.png")
plt.show()

print("Chart saved.")

