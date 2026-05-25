from selenium.webdriver.common.by import By
# Локаторы страницы {BASE_URL}/register


class RegisterPageLocators:

    NAME = [By.XPATH, '//label[text()="Имя"]/following::input']
    EMAIL = [By.XPATH, '//label[text()="Email"]/following::input']
    PASSWORD = [
        By.XPATH, '//label[contains(text(),"Пароль")]/following::input']
    REGISTER_BUTTON = [By.XPATH, '//button[text()="Зарегистрироваться"]']
