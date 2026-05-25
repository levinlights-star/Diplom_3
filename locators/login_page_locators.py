from selenium.webdriver.common.by import By
# Локаторы страницы {BASE_URL}/login

class LoginPageLocators:

    EMAIL = [By.XPATH, '//label[text()="Email"]/following::input']
    PASSWORD = [By.XPATH, '//label[contains(text(),"Пароль")]/following::input']
    ENTER_BUTTON = [By.XPATH, '//button[text()="Войти"]']