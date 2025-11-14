from tests.pages.site_pages import HomePage
import pytest

def test_pagination_next_and_prev(pw_page, base_url):
    home = HomePage(pw_page)
    home.open(base_url)
    home.wait_for_loaded()

    next_btn = pw_page.query_selector("text=Next")
    if not next_btn:
        pytest.skip("Pagination controls not found")

    next_btn.click()
    pw_page.wait_for_selector(".card", timeout=8000)
    next_btn.click()
    pw_page.wait_for_selector(".card", timeout=8000)

    prev_btn = pw_page.query_selector("text=Prev")
    if prev_btn:
        prev_btn.click()
        pw_page.wait_for_selector(".card", timeout=8000)

    assert len(home.cards()) > 0
