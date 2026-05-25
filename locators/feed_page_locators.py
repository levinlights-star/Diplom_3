from selenium.webdriver.common.by import By
# Локаторы страницы {BASE_URL}/feed


class FeedPageLocators:
    # Заголовок страницы
    H1_FEED = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

   # Значение счетчика 'Выполнено за все время'
    TOTAL_COUNTER = (
        By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    
   # Значение счетчика 'Выполнено за сегодня'
    DAILY_COUNTER = (
        By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[1]")

   # Список номеров заказов в разделе 'В работе'
    ORDER_NUMBER = (
        By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
