import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator, timeout=10):
        element = self.wait(timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator, timeout=10):
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ожидать невидимость элемента {locator}")
    def wait_for_invisible(self, locator, timeout=10):
        return self.wait(timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Проверить, виден ли элемент {locator}")
    def is_element_visible(self, locator, timeout=0):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Выполнить JavaScript: {script}")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step('Перетаскивание элемента из {locator_from} в {locator_to}')
    def drag_and_drop_element(self, locator_from, locator_to, timeout=10):
        element_from = self.find_element(locator_from)
        element_to = self.find_element(locator_to)
        self.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    @allure.step("Внести текст в {locator}")
    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
