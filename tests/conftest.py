import os
import pytest
import logging
from playwright.sync_api import sync_playwright

BASE_URL = "https://tmdb-discover.surge.sh/"

# Create report directories
os.makedirs("reports/html", exist_ok=True)
os.makedirs("reports/screenshots", exist_ok=True)
os.makedirs("reports/logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename="reports/logs/test_run.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def pw_page(pw, request):
    """Launches a Playwright browser page and yields it (fixture named pw_page to avoid conflicts)."""
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    console_errors = []

    def on_console(msg):
        if msg.type == "error":
            console_errors.append(f"[console:{msg.type}] {msg.text}")

    page.on("console", on_console)
    page.on("pageerror", lambda e: console_errors.append(f"[pageerror] {e}"))

    yield page

    # Screenshot on failure
    rep = getattr(request.node, "rep_call", None)
    if rep is None or rep.failed:
        try:
            page.screenshot(path=f"reports/screenshots/{request.node.name}.png", full_page=True)
        except Exception:
            pass

    # Write any console errors
    if console_errors:
        log_path = f"reports/logs/{request.node.name}_console.log"
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("\n".join(console_errors))
        logging.error("Console errors for %s: %s", request.node.name, console_errors)

    context.close()
    browser.close()

# Correct hook: use hookwrapper
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
