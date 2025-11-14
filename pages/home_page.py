from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from utils.base import BasePage
from utils.logger import get_logger
from utils.constants import Selectors


class HomePage(BasePage):

    def is_page_loaded(self):
        """Verify page title element is visible."""
        logger = get_logger()
        logger.info("Checking if the Home page is loaded successfully")
        self.wait_for_visibility(Selectors.PAGE_TITLE)
        return self.driver.title != ""

    def search(self, text):
        """Clear the search input and enter a title to search."""
        logger = get_logger()
        logger.info("Locating the search input box")
        self.input_text(Selectors.SEARCH_INPUT_BOX, text)
        logger.info(f"Entered '{text}' into the search box")

    def wait_for_search_result(self, text, timeout=10):
        """Return True if search result containing text is found; else False."""
        logger = get_logger()
        dynamic_xpath = (By.XPATH, f"//*[contains(text(), '{text}')]")
        try:
            self.wait_for_presence(dynamic_xpath)
            logger.info(f"Search result containing '{text}' appeared on the page")
            return True
        except TimeoutException:
            logger.warning(f"No results found matching '{text}' within {timeout} seconds")
            return False

    def is_no_results_displayed(self):
        """Check if the 'No results found' message is displayed."""
        logger = get_logger()
        logger.info("Checking for 'No results found' message")
        return len(self.find_all(Selectors.NO_RESULTS_MESSAGE)) > 0

    def click_tab(self, tab_locator):
        """Clicks on a tab using the given locator."""
        logger = get_logger()
        logger.info(f"Clicking on tab: {tab_locator}")
        self.click(tab_locator)

    def get_visible_movie_titles(self):
        """Returns a list of visible movie titles under the active tab."""
        logger = get_logger()
        logger.info("Fetching visible movie titles under the current tab")

        try:
            self.wait_for_presence(Selectors.MOVIE_TITLES)
            title_elements = self.find_all(Selectors.MOVIE_TITLES)
            titles = [el.text.strip() for el in title_elements]

            logger.info(f"Found {len(titles)} movie title(s): {titles}")
            return titles

        except Exception as e:
            logger.error(f"Error while fetching movie titles: {e}")
            return []

