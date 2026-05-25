import pytest
import allure
import logging
from selenium import webdriver

from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data.user_data import generate_user_data
from data.config import BASE_URL

logger = logging.getLogger(__name__)

"""Фикстура: Для открытия и закрытия тестов в Chrome и в Firefox"""
@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


# # Для открытия и закрытия тестов  в Firefox
# @pytest.fixture(scope="function")
# def driver(request):

#     driver = webdriver.Firefox()
#     yield driver
#     driver.quit()

"""Фикстура: Открыть страницу {BASE_URL}"""
@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    return page


"""Фикстура: регистрация + авторизация через UI"""
@pytest.fixture
def auth_main_page(driver):
    with allure.step("Генерируем данные для нового пользователя"):
        user_data = generate_user_data()
    logger.info(f"Сгенерированный данные: {user_data}")

    with allure.step("Регистрируем нового пользователя"):
        register_page = RegisterPage(driver)
    register_page.open_register_page()
    register_page.register(
        user_data["name"],
        user_data["email"],
        user_data["password"]
    )

    with allure.step("Авторизация под новым пользователем"):
        login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(user_data["email"], user_data["password"])

    return MainPage(driver).wait_until_loaded_after_login()