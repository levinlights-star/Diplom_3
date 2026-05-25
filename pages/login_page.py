import allure

from pages.base_page import BasePage

from locators.login_page_locators import LoginPageLocators
from data.config import LOGIN_URL


class LoginPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open(LOGIN_URL)
        return self

    @allure.step("Авторизоваться под {email}")
    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL, email)
        self.input_text(LoginPageLocators.PASSWORD, password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)
        return self
