import logging
import allure

from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators

from data.config import ORDER_FEED_URL

logger = logging.getLogger(__name__)


class MainPage(BasePage):

    @allure.step("Нажать на 'Конструктор'")
    def click_сonstructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Открыть страницу ленты заказов")
    def open_order_feed(self):
        self.driver.get(ORDER_FEED_URL)
        return self

    @allure.step("Проверить, что открыта страница конструктора")
    def is_constructor_page_opened(self):
        return self.is_element_visible(MainPageLocators.H1_BURGERS)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Нажать на 'Лента заказов'")
    def click_feed(self):
        self.click_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Проверить, что открыта страница лента заказов")
    def is_feed_page_opened(self):
        try:
            self.find_element(FeedPageLocators.H1_FEED)
            return True
        except:
            return False

    @allure.step("Нажать на ингредиент")
    def click_ingridient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверить, что модальное окно ингредиента отображается")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_TITLE)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.wait_for_invisible(MainPageLocators.MODAL_TITLE)
        return self

    @allure.step("Проверить, что модальное окно ингредиента невидимо")
    def is_modal_invisible(self):
        return not self.is_element_visible(MainPageLocators.MODAL_TITLE)

    @allure.step("Добавить ингредиент булка в конструктор через drag-and-drop")
    def add_ingredient_to_constructor(self):
        self.drag_and_drop_element(
            MainPageLocators.INGREDIENT, MainPageLocators.BASKET)

    @allure.step("Получить значения счётчика ингредиента")
    def get_ingredient_counter(self):
        counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER)
        total = 0
        for counter in counters:
            text = counter.text
            if text.isdigit():
                total += int(text)
        return total

    @allure.step("Дожидаемся появления кнопки 'Оформить заказ' на главной после авторизации")
    def wait_until_loaded_after_login(self):
        self.find_element(MainPageLocators.ORDER_BUTTON)
        return self

    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def place_order(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
        return self

    @allure.step("Создать заказ из булки")
    def create_order(self):
        self.add_ingredient_to_constructor(MainPageLocators.INGREDIENT)
        self.place_order()
        return self

    @allure.step("Получить номер заказа в модальном окне")
    def get_order_number_from_modal(self):
        self.wait(10).until(lambda driver: driver.find_element(
            *MainPageLocators.ORDER_NUMBER).text != "9999")
        element = self.find_element(MainPageLocators.ORDER_NUMBER)
        return element.text

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)
        self.wait_for_invisible(MainPageLocators.MODAL_TITLE)
        return self

    @allure.step("Создать заказ и получить его номер")
    def create_order_get_number(self):
        self.click_сonstructor()
        self.add_ingredient_to_constructor()
        self.place_order()
        order_number = self.get_order_number_from_modal()
        logger.info(f"Номер моего заказа: {order_number}")
        self.close_order_modal()
        return order_number
