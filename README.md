# 🦁 Brave Auto Refresh Scripts

This project contains Python scripts that use **Selenium** and **Requests** to automatically refresh a website in the Brave browser and measure site performance.

You can choose between different scripts:
- `refresh_site.py` → Refresh a site in Brave every 1 minute  
- `simple_refresh.py` → Minimal version using `requests` for quick status checks  
- `performance_detailed.py` → Logs status, response time, headers, and content size  
- `visual_refresh.py` → Displays site load times with a simple visual bar chart  

---

## 🚀 Requirements

- **Python 3.x** installed  
- **Brave browser** installed  
- **Pipenv** for dependency management  
- A **Brave profile** (e.g., `Default`, `matwana`)  

---

## 📦 Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/levismunene01/browser-refresher.git
   cd browser-refresher

2. Install dependencies inside a Pipenv virtual environment:
   
   ```pipenv install selenium webdriver-manager requests

3. Activate the virtual environment:

   ``` pipenv shell

⚙️ Brave Browser Configuration (per OS)

You must set the binary location for Brave depending on your OS.

🐧 Linux

Brave is usually installed here:

/usr/bin/brave-browser


Example in Python:

options.binary_location = "/usr/bin/brave-browser"

🍏 macOS

Brave is usually installed here:

/Applications/Brave Browser.app/Contents/MacOS/Brave Browser


Example in Python:

options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

🪟 Windows

Brave is usually installed here:

C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe


Example in Python:

options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

▶️ Running the Scripts
1. Refresh Site in Brave
pipenv run python refresh_site.py

2. Simple Refresh (Requests only)
pipenv run python simple_refresh.py

3. Detailed Performance Logging
pipenv run python performance_detailed.py

4. Visual Refresh (Terminal Bar Chart)
pipenv run python visual_refresh.py



