import pytest
from base import BaseCase
from ui.locators import basic_locators
from ui.testing_data import data
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestExample(BaseCase):

    @pytest.mark.ap1
    def test_cart_clickable(self, wait,to_cart):
        """
        На стартовой странице присутствует кнопка Корзины
        Кнопка корзины кликабельна, при нажатии - переход на страницу корзины
        """
        assert "SHOPPING-CART SUMMARY" in self.text(basic_locators.CART_TITLE)

    @pytest.mark.ap1
    def test_cart_empty_warning(self, wait,to_cart):
        """
        Если корзина пуста, на странице корзины присутствует надпись Your shopping cart is empty.
        """
        assert "Your shopping cart is empty." in self.text(basic_locators.EMPTY_CART_WARNING)

    @pytest.mark.ap
    def test_cart_home_button(self, wait):
        """
        Кнопка домой на странице корзины ведет на домашнюю страницу
        """
        self.find(basic_locators.CART_BUTTON)
        wait.until(ec.presence_of_element_located(basic_locators.CART_TITLE))
        self.find(basic_locators.HOME_BUTTON)
        assert wait.until(ec.url_to_be("http://automationpractice.com/index.php"))

    @pytest.mark.ap
    def test_cart_add_modalwindow(self, wait):
        """
        При добавлениии товара в корзину - модальное окно Product successfully added to your shopping cart
        """
        pass

    @pytest.mark.ap
    def test_cart_has_items(self, wait):
        """
        Если корзина содержит товары, они отображаются на странице корзины
        """
        pass

    @pytest.fixture()
    def wait(self):
        return WebDriverWait(self.driver, timeout=20)

    @pytest.fixture()
    def to_cart(self,wait):
        wait.until(ec.presence_of_element_located(basic_locators.CART_BUTTON))
        self.find(basic_locators.CART_BUTTON)
        wait.until(ec.presence_of_element_located(basic_locators.CART_TITLE))
