import allure

from pages.base_page import BasePage

from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    @allure.step("Получить количество выполненных заказов за всё время")
    def get_total_orders_count(self):
        text = self.get_text(FeedPageLocators.TOTAL_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        text = self.get_text(FeedPageLocators.DAILY_COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Получить список номеров заказов")
    def get_order_numbers(self):
        elements = self.find_elements(FeedPageLocators.ORDER_NUMBER)
        return [el.text for el in elements]
