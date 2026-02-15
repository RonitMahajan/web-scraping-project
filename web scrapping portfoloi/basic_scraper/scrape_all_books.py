import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_data = []

for page in range(1, 51):   # 1 to 50

    print(f"Scraping page {page}...")

    url = base_url.format(page)

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            all_data.append(
                [title, price, rating, availability, page]
            )

        # Be polite to server
        time.sleep(1)

    except Exception as e:
        print("Error on page", page, ":", e)


# Create DataFrame
df = pd.DataFrame(
    all_data,
    columns=["Title", "Price", "Rating", "Availability", "Page"]
)

# Save
df.to_csv("all_books_data.csv", index=False)

print("✅ All pages scraped successfully!")
