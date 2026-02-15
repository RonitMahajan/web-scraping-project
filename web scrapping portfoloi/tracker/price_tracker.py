from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time
import os

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://webscraper.io/test-sites/e-commerce/allinone"
driver.get(url)

time.sleep(5)

data = []

today = datetime.date.today().strftime("%Y-%m-%d")

items = driver.find_elements(By.CLASS_NAME, "thumbnail")

for item in items:

    name = item.find_element(By.CLASS_NAME, "title").text
    price = item.find_element(By.CLASS_NAME, "price").text

    # Clean price
    price = float(price.replace("$", "").strip())

    data.append([today, name, price])


driver.quit()

# Save daily file
filename = f"prices_{today}.csv"
df = pd.DataFrame(data, columns=["Date", "Product", "Price"])

df.to_csv(filename, index=False)

print(f"✅ Data saved: {filename}")


# Combine with old data
all_files = [f for f in os.listdir() if f.startswith("prices_")]

all_data = []

for file in all_files:
    temp = pd.read_csv(file)
    all_data.append(temp)

final_df = pd.concat(all_data)

final_df.to_csv("price_history.csv", index=False)

print("✅ Price history updated!")

