from time import sleep

import pytest
from utils.constants import WebPageTitles
from utils.logger import get_logger
class TestSearch:
    def test_search_valid_title(self, home_page):
        home_page.search(WebPageTitles.CHAINSAW_MAN_TITLE)
        sleep(5)
        assert WebPageTitles.CHAINSAW_MAN_TITLE in home_page.get_visible_movie_titles(), \
            f"'{WebPageTitles.CHAINSAW_MAN_TITLE}' not found in Trend tab"

    def test_search_invalid_title(self, home_page):
        home_page.search(WebPageTitles.INVALID_TITLE)
        sleep(5)
        assert home_page.is_no_results_displayed(), "No 'No results found.' message was shown."
