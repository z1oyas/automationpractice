import pytest


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator).click()

    def write_in(self, locator, data):
        return self.driver.find_element(*locator).send_keys(data)

    def get_url(self):
        return self.driver.current_url

    def text(self, locator):
        return self.driver.find_element(*locator).text

    def clear(self, locator):
        return self.driver.find_element(*locator).clear()
