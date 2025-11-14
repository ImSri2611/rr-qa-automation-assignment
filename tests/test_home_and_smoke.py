from tests.pages.site_pages import HomePage

def test_home_page_loads(pw_page, base_url):
    home = HomePage(pw_page)
    home.open(base_url)
    home.wait_for_loaded()
    cards = home.cards()
    assert len(cards) > 0

def test_switch_category_popular(pw_page, base_url):
    home = HomePage(pw_page)
    home.open(base_url)
    home.wait_for_loaded()
    home.click_category("Popular")
    pw_page.wait_for_selector(".card", timeout=8000)
    assert len(home.cards()) > 0
