import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
from utils.constants import Urls
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.home_page import HomePage
from utils.constants import BrowserPlatform
from utils.logger import get_logger



def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser option: chrome, firefox, safari"
    )


@pytest.fixture(scope="class", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == BrowserPlatform.CHROME:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == BrowserPlatform.FIREFOX:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == BrowserPlatform.SAFARI:
        driver = SafariDriver()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Urls.BASE_URL)

    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture
def home_page(request):
    logger = get_logger()
    logger.info("Loading the Home page")
    page = HomePage(request.cls.driver)
    assert page.is_page_loaded()
    return page
