from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

url = "https://www.scrapethissite.com/pages/ajax-javascript/"
driver.get(url)

time.sleep(5)

data = []

# Click "Load More" multiple times
for i in range(5):

    try:
        load_btn = driver.find_element(By.ID, "load-more")
        load_btn.click()
        time.sleep(2)

    except:
        print("No more button found")
        break


items = driver.find_elements(By.CLASS_NAME, "film")

for item in items:

    title = item.find_element(By.CLASS_NAME, "film-title").text
    year = item.find_element(By.CLASS_NAME, "film-year").text
    rating = item.find_element(By.CLASS_NAME, "film-rating").text

    data.append([title, year, rating])


driver.quit()

df = pd.DataFrame(
    data,
    columns=["Title", "Year", "Rating"]
)

df.to_csv("amazon_style_data.csv", index=False)

print("✅ Amazon-style scraping done!")
