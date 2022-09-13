import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as dc


@pytest.fixture()
def driver():
    caps = dc.CHROME
    caps["pageLoadStrategy"] = "eager"
    url = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
