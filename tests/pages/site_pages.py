# tests/pages/site_pages.py
class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, base_url):
        # open base url (the app also navigates to /popular by default sometimes)
        self.page.goto(base_url)

    def wait_for_loaded(self, timeout=15000):
        """
        Wait for the main grid that contains movie tiles.
        """
        # grid grid-cols-3 is the container visible on the site
        self.page.wait_for_selector(".grid.grid-cols-3", timeout=timeout)

    def cards(self):
        """
        Return all card nodes. Selector chosen from observed DOM:
        - .grid.grid-cols-3 .flex.flex-col.items-center
        """
        return self.page.query_selector_all(".grid.grid-cols-3 .flex.flex-col.items-center")

    def click_category(self, name, timeout=10000):
        """
        Click a category tab (Popular / Trend / Newest / Top rated).
        Use nav scope to avoid accidental matches.
        """
        # Use nav scope and visible text
        self.page.click(f"nav >> text={name}", timeout=timeout)

    def search(self, query, timeout=10000):
        """
        Fill the search box. The site uses <input name='search' placeholder='SEARCH'>.
        """
        selector = "input[name='search'], input[placeholder='SEARCH'], input[placeholder*='Search']"
        element = self.page.query_selector(selector)
        if not element:
            raise RuntimeError("Search input not found on page")
        element.fill(query)
        # Press Enter to trigger search; add small wait after
        element.press("Enter")
        self.page.wait_for_timeout(800)


class Filters:
    def __init__(self, page):
        self.page = page

    def select_genre(self, index=1, timeout=10000):
        """
        The UI uses react-select styled components; there may not be a plain <select>.
        This will try the common select patterns and fall back to clickable genre buttons.
        """
        selector = "select#genre, select[name='genre'], select"
        dropdown = self.page.query_selector(selector)
        if dropdown:
            options = dropdown.query_selector_all("option")
            if len(options) > index:
                value = options[index].get_attribute("value")
                dropdown.select_option(value, timeout=timeout)
                return

        # fallback: genre buttons or items with .genre-item or .genre
        buttons = self.page.query_selector_all("button.genre, .genre-item, .genre")
        if buttons and len(buttons) > index:
            buttons[index].click()
            self.page.wait_for_timeout(500)
            return

        # last resort: click the genre input and pick first option if visible
        try:
            self.page.click("div[role='combobox']", timeout=2000)
            self.page.wait_for_timeout(300)
        except Exception:
            pass
