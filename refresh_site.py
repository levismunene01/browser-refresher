from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# your target site
url = "https://www.forexfactory.com/trades"

options = Options()
options.binary_location = "/usr/bin/brave-browser"  # change path if needed

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

# keep refreshing every 1 minute
while True:
    time.sleep(60)
    driver.refresh()
