import time
import os
import selenium.webdriver as webdriver
import selenium.webdriver.chrome.service as chrome_service
import selenium.webdriver.chrome.options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager

# target URL
url = "https://example.com"

# configure Brave browser
options = chrome_options.Options()
options.binary_location = "/usr/bin/brave-browser"

# create a dedicated Selenium profile so it doesn’t clash with your normal Brave profile
selenium_profile = "/home/dextermnesh/.config/BraveSoftware/Brave-Browser-Selenium"
os.makedirs(selenium_profile, exist_ok=True)

options.add_argument(f"--user-data-dir={selenium_profile}")
options.add_argument("--profile-directory=Default")

# start the browser
driver = webdriver.Chrome(
    service=chrome_service.Service(ChromeDriverManager().install()),
    options=options
)

driver.get(url)

# keep refreshing every 60s with performance stats
refresh_count = 0

while True:
    time.sleep(60)
    start = time.time()
    driver.refresh()
    end = time.time()

    refresh_count += 1
    page_source = driver.page_source
    page_size = len(page_source.encode("utf-8"))

    print(f"\n=== Refresh #{refresh_count} ===")
    print(f"Load Time: {end - start:.2f}s")
    print(f"Page Size: {page_size} bytes")
