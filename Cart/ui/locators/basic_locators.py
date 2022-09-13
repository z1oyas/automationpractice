from selenium.webdriver.common.by import By

CART_BUTTON = (By.XPATH, "//div [@class= 'shopping_cart']/a")
CART_TITLE = (By.ID, "cart_title")
EMPTY_CART_WARNING = (By.XPATH,"//div /p[@class= 'alert alert-warning']")
HOME_BUTTON = (By.XPATH, "//div/a[@class= 'home']")

