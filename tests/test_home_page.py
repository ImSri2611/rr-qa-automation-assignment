from time import sleep

import pytest
from pages.home_page import HomePage


class TestHomePage:
    def test_home_page_loads(self):
        page = HomePage(self.driver)
        sleep(5)
        assert page.is_page_loaded(), "Home page did not load correctly."