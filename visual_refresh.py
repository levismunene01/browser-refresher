from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

url = "https://example.com"

options = Options()
options.binary_location = "/usr/bin/brave-browser"

selenium_profile = "/home/dextermnesh/.config/BraveSoftware/Brave-Browser-Selenium"
os.makedirs(selenium_profile, exist_ok=True)

options.add_argument(f"--user-data-dir={selenium_profile}")
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

times = []

while True:
    time.sleep(60)
    start = time.time()
    driver.refresh()
    end = time.time()

    load_time = end - start
    times.append(load_time)

    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    print(f"Last Load Time: {load_time:.2f}s\nHistory (last 10 refreshes):")
    for t in times[-10:]:
        bar = "#" * int(t * 10)
        print(f"{t:.2f}s | {bar}")
