from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """Finds a single element using a locator tuple"""
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            raise Exception(f"Error finding element {locator}: {e}")

    def find_all(self, locator):
        """Finds multiple elements using a locator tuple"""
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            raise Exception(f"Error finding elements {locator}: {e}")

    def click(self, locator):
        """Clicks on the element specified by the locator"""
        element = self.find(locator)
        element.click()

    def input_text(self, locator, text, clear_first=True):
        """Sends keys to an input field"""
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Returns text content of a web element"""
        element = self.find(locator)
        return element.text

    def wait_for_visibility(self, locator):
        """Waits until the element is visible on the page"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        """Waits until the element is present in DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))
