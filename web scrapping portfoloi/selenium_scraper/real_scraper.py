from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Setup driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://webscraper.io/test-sites/e-commerce/allinone"
driver.get(url)

time.sleep(5)

products = []

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

items = driver.find_elements(By.CLASS_NAME, "thumbnail")

for item in items:

    name = item.find_element(By.CLASS_NAME, "title").text
    price = item.find_element(By.CLASS_NAME, "price").text
    desc = item.find_element(By.CLASS_NAME, "description").text

    products.append([name, price, desc])


driver.quit()

# Save to CSV
df = pd.DataFrame(
    products,
    columns=["Product Name", "Price", "Description"]
)

df.to_csv("real_products.csv", index=False)

print("✅ Real e-commerce data scraped successfully!")
