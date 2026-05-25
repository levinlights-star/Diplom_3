import allure
import logging

from pages.feed_page import FeedPage

logger = logging.getLogger(__name__)


class TestFeedPage:

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, auth_main_page):
        with allure.step("Регистрируем нового пользователя и авторизуемся под ним"):
            page = auth_main_page
        order_feed_page = FeedPage(page.driver)

        with allure.step("Открываем страницу 'Лента заказов'"):
            page.click_feed()

        with allure.step("Получаем и фиксируем значение счетчика 'Выполнено за всё время'"):
            old_total_count = order_feed_page.get_total_orders_count()
        logger.info(
            f"Выполнено за все время до моего заказа: {old_total_count}")

        with allure.step("Создаем заказ"):
            page.create_order_get_number()

        with allure.step("Открываем страницу 'Лента заказов'"):
            page.click_feed()

        with allure.step("Получаем и фиксируем значение счетчика 'Выполнено за всё время'"):
            new_total_count = order_feed_page.get_total_orders_count()

        logger.info(
            f"Выполнено за все время после моего заказа: {new_total_count}")

        with allure.step("Проверяем, что счетчик выполненных заказов увеличился"):
            assert new_total_count == old_total_count + 1, \
                f"Счётчик 'Выполнено за всё время' не увеличился: " \
                f"было {old_total_count}, стало {new_total_count}"

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, auth_main_page):

        with allure.step("Регистрируем нового пользователя и авторизуемся под ним"):
            page = auth_main_page

        order_feed_page = FeedPage(page.driver)
        with allure.step("Открываем страницу 'Лента заказов'"):
            page.click_feed()

        with allure.step("Получаем и фиксируем значение счетчика 'Выполнено за сегодня'"):
            old_day_count = order_feed_page.get_today_orders_count()
        logger.info(f"Выполнено за сегодня до моего заказа: {old_day_count}")

        with allure.step("Создаем заказ"):
            page.create_order_get_number()

        with allure.step("Открываем страницу 'Лента заказов'"):
            page.click_feed()

        with allure.step("Получаем и фиксируем значение счетчика 'Выполнено за сегодня'"):
            new_day_count = order_feed_page.get_today_orders_count()
        logger.info(
            f"Выполнено за сегодня после моего заказа: {new_day_count}")

        with allure.step("Проверяем, что счетчик выполненных заказов за сегодня увеличился"):
            assert new_day_count == old_day_count + 1, \
                f"Счётчик 'Выполнено за сегодня' не увеличился: " \
                f"было {old_day_count}, стало {new_day_count}"

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_appears_in_work_section(self, auth_main_page):
        with allure.step("Регистрируем нового пользователя и авторизуемся под ним"):
            page = auth_main_page
        order_feed_page = FeedPage(page.driver)

        with allure.step("Создаем заказ, получаем его номер"):
            order_number = page.create_order_get_number()

        with allure.step("Открываем Ленту заказов"):
            page.click_feed()

        with allure.step("Получаем список заказов в разделе 'В работе'"):
            work_section_text = order_feed_page.get_order_numbers()

        logger.info(f"Заказы в разделе 'В работе': {work_section_text}")

        with allure.step("Проверяем что наш заказ есть в списке заказов в разделе 'В работе'"):
            assert (
                f'0{order_number}') in work_section_text, f"Номер заказа {order_number} не появился в разделе 'В работе'"
