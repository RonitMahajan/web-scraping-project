from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://unsplash.com")

time.sleep(5)

# Scroll down slowly
for i in range(5):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

time.sleep(5)
driver.quit()
