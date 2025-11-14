# debug_get_dom.py
from playwright.sync_api import sync_playwright
import os, time

os.makedirs("reports/debug", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headed so you can visually inspect
    page = browser.new_page()
    url = "https://tmdb-discover.surge.sh/"
    print("Opening", url)
    page.goto(url, timeout=30000)
    time.sleep(2)  # let content settle
    # Save screenshot and HTML
    ss = "reports/debug/debug_screenshot.png"
    htmlfile = "reports/debug/debug_page.html"
    page.screenshot(path=ss, full_page=True)
    with open(htmlfile, "w", encoding="utf-8") as fh:
        fh.write(page.content())
    print("Saved:", ss)
    print("Saved:", htmlfile)
    # keep browser open for 5s so you can inspect manually if desired
    time.sleep(5)
    browser.close()
