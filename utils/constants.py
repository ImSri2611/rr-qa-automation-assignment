from selenium.webdriver.common.by import By

class WebPageTitles:
    CHAINSAW_MAN_TITLE = "Chainsaw Man - The Movie: Reze Arc"
    THE_SMASHING_MAN = "The Smashing Machine"
    AFTERBURN = "Afterburn"
    THE_SHAWSHANK = "The Shawshank Redemption"
    INVALID_TITLE = "sgagsfdgahf"
class Selectors:
    SEARCH_INPUT_BOX = (By.CSS_SELECTOR, "input[placeholder='SEARCH']")
    MOVIE_CARD_TITLE = "//div[contains(@class,'movie-card')]//p"
    PAGE_TITLE = (By.XPATH, '//*[@id="root"]/div/div/header/a/p')
    NO_RESULTS_MESSAGE = (By.XPATH, "//div[contains(text(), 'No results found.')]")
    TREND_TAB = (By.LINK_TEXT, "Trend")
    NEWEST_TAB = (By.LINK_TEXT, "Newest")
    TOP_RATED_TAB = (By.LINK_TEXT, "Top rated")
    MOVIE_TITLES = (By.CSS_SELECTOR, "p.text-blue-500.font-bold.py-1")


class Urls:
    BASE_URL = "https://tmdb-discover.surge.sh/"

class BrowserPlatform:
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"

