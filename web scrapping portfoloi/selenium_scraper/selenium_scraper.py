from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Setup driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open website
url = "https://books.toscrape.com"
driver.get(url)

time.sleep(5)

print("✅ Browser opened successfully!")

# Close browser
driver.quit()
