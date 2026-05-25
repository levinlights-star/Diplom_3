import logging
import allure

from pages.base_page import BasePage

from locators.register_page_locators import RegisterPageLocators
from data.config import REGISTRATION_URL

logger = logging.getLogger(__name__)


class RegisterPage(BasePage):

    @allure.step("Открыть страницу регистрации")
    def open_register_page(self):
        self.open(REGISTRATION_URL)
        return self

    @allure.step("Зарегистрировать пользователя {email}")
    def register(self, name, email, password):
        self.input_text(RegisterPageLocators.NAME, name)
        self.input_text(RegisterPageLocators.EMAIL, email)
        self.input_text(RegisterPageLocators.PASSWORD, password)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)
        return self
