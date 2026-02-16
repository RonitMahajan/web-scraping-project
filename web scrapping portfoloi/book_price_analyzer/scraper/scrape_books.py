import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

titles = []
prices = []
ratings = []
availability = []

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        titles.append(book.h3.a["title"])
        prices.append(book.find("p", class_="price_color").text[1:])
        ratings.append(book.p["class"][1])
        availability.append(
            book.find("p", class_="instock availability").text.strip()
        )

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})

df.to_csv("../data/books.csv", index=False)

print("Scraping completed!")

