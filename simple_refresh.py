
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# enter your url here
url = "https://example.com"

options = Options()
options.binary_location = "/usr/bin/brave-browser"

# use a separate Selenium profile folder
selenium_profile = "/home/dextermnesh/.config/BraveSoftware/Brave-Browser-Selenium"
os.makedirs(selenium_profile, exist_ok=True)

options.add_argument(f"--user-data-dir={selenium_profile}")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

refresh_count = 0

while True:
    time.sleep(60)  # refresh every 60s
    start = time.time()
    driver.refresh()
    end = time.time()

    refresh_count += 1
    print(f"Refresh #{refresh_count} took {end - start:.2f}s")
