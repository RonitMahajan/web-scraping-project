import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

# Add headers (act like a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()   # Check if request succeeded

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        availability = book.find("p", class_="instock availability").text.strip()

        data.append([title, price, rating, availability])

    df = pd.DataFrame(
        data,
        columns=["Title", "Price", "Rating", "Availability"]
    )

    df.to_csv("books_data.csv", index=False)

    print("✅ Scraping successful! Data saved.")

except requests.exceptions.Timeout:
    print("❌ Connection timed out. Website not responding.")

except requests.exceptions.ConnectionError:
    print("❌ Network problem. Check internet or firewall.")

except Exception as e:
    print("❌ Error:", e)
