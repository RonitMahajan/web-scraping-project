import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("price_history.csv")

df["Date"] = pd.to_datetime(df["Date"])

product = df["Product"].iloc[0]

product_data = df[df["Product"] == product]

plt.figure()
plt.plot(product_data["Date"], product_data["Price"], marker="o")

plt.title(f"Price Trend: {product}")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid()

plt.show()

