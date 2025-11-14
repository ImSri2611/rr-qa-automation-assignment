from time import sleep

import pytest
from utils.constants import Selectors, WebPageTitles


class TestTabs:

    def test_trend_tab_movies(self, home_page):
        home_page.click_tab(Selectors.TREND_TAB)
        sleep(5)
        assert WebPageTitles.THE_SMASHING_MAN in home_page.get_visible_movie_titles(), \
            f"'{WebPageTitles.THE_SMASHING_MAN}' not found in Trend tab"

    def test_newest_tab_movies(self, home_page):
        home_page.click_tab(Selectors.NEWEST_TAB)
        sleep(5)
        assert WebPageTitles.AFTERBURN in home_page.get_visible_movie_titles(), \
            f"'{WebPageTitles.AFTERBURN}' not found in Newest tab"

    def test_toprated_tab_movies(self, home_page):
        home_page.click_tab(Selectors.TOP_RATED_TAB)
        sleep(5)
        assert WebPageTitles.THE_SHAWSHANK in home_page.get_visible_movie_titles(), \
            f"'{WebPageTitles.THE_SHAWSHANK}' not found in Top Rated tab"
