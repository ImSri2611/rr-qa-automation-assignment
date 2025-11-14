import pytest
from tests.pages.site_pages import HomePage, Filters

def test_search_functionality(pw_page, base_url):
    home = HomePage(pw_page)
    home.open(base_url)
    home.wait_for_loaded()
    try:
        home.search("Avengers")
    except RuntimeError:
        pytest.skip("Search not available")
    pw_page.wait_for_selector(".card", timeout=8000)
    assert len(home.cards()) > 0

def test_genre_filter_api_response(pw_page, base_url):
    responses = []
    def capture_response(response):
        if "discover" in response.url:
            responses.append(response)
    pw_page.on("response", capture_response)
    home = HomePage(pw_page)
    home.open(base_url)
    home.wait_for_loaded()
    filters = Filters(pw_page)
    filters.select_genre(1)
    pw_page.wait_for_selector(".card", timeout=8000)
    assert any(r.status == 200 for r in responses)
