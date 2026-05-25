import allure
import logging

from pages.main_page import MainPage
from data.config import BASE_URL, ORDER_FEED_URL

logger = logging.getLogger(__name__)


class TestMainPage:

    @allure.title("Переход на страницу конструктора по клику на кнопку")
    def test_go_to_constructor_by_click(self, driver):
        page = MainPage(driver)

        with allure.step("Открыть страницу ленты заказов"):
            page.open_order_feed()

        with allure.step("Кликнуть на кнопку 'Конструктор'"):
            page.click_сonstructor()

        with allure.step("Проверить, что URL соответствует странице конструктора"):
            assert BASE_URL == page.get_current_url(), "Не перешли на страницу конструктора!"

        with allure.step("Проверить, что отображается заголовок страницы Конструктор"):
            assert page.is_constructor_page_opened(), \
                "Заголовок страницы конструктора не отображается"

    @allure.title("При клике на кнопку «Лента заказов» пользователь переходит на страницу списка заказов")
    def test_go_to_feed_by_click(self, driver, main_page):
        page = MainPage(driver)

        with allure.step("Открыть страницу ленты заказов"):
            page.click_feed()

        with allure.step("Проверить, что URL страницы ленты заказов"):
            assert ORDER_FEED_URL == page.get_current_url(
            ), "Не перешли на страницу списка заказов!"
        with allure.step("Проверить, что отображается заголовок страницы ленты заказов"):
            assert page.is_feed_page_opened(), "Не перешли на страницу списка заказов!"

    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_сlick_on_ingredient_opens_modal_window(self, driver, main_page):
        page = MainPage(driver)

        with allure.step("Нажать на ингредиент"):
            page.click_ingridient()

        with allure.step("Проверить, что открылось модальное окно ингредиента"):
            assert page.is_modal_visible(), "Не открылось модальное окно ингредиента"

    @allure.title("Модальное окно закрывается кликом по крестику")
    def test_сlick_on_cross_tab_close_modal_window(self, driver, main_page):
        page = MainPage(driver)

        with allure.step("Нажать на ингредиент"):
            page.click_ingridient()

        with allure.step("Закрыть модальное окно ингредиента"):
            page.close_modal()

        with allure.step("Проверить, что модальное окно ингредиента закрылось"):
            assert page.is_modal_invisible(), "Модальное окно не закрылось"

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_counter_increases_when_ingredient_added(self, driver, main_page):
        page = MainPage(driver)

        with allure.step("Получить количество ингредиентов"):
            old_counter = page.get_ingredient_counter()
        logger.info(f"Количество ингредиентов до: {old_counter}")

        with allure.step("Добавить ингредиент булка в конструктор"):
            page.add_ingredient_to_constructor()

        with allure.step("Получить количество ингредиентов"):
            new_counter = page.get_ingredient_counter()
        logger.info(f"Количество ингредиентов после: {new_counter}")

        with allure.step("Проверить, что счетчик ингредиентов увеличился"):
            assert new_counter > old_counter, "Не увеличилось кол-во ингредиентов"
        with allure.step("Проверить, что счетчик ингредиентов стал 2, т.к. это булки"):
            assert new_counter == 2, f"Ожидалось: 2, пришло: {new_counter}"
