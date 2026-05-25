from selenium.webdriver.common.by import By
# Локаторы страницы {BASE_URL}


class MainPageLocators:
    """Кнопки в Header"""
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")

    """Заголовок страницы"""
    H1_BURGERS = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    """Ингредиенты"""
    # Флюоресцентная булка
    INGREDIENT = (
        By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')

    """Модальное окно ингредиента"""
    # Заголовок модального окна ингредиента
    MODAL_TITLE = (
        By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # Кнопка закрытия модального окна ингредиента
    CLOSE_MODAL_BUTTON = (
        By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    """Конструктор(корзина) бургера, там где он собирается"""
    # счетчик ингредиента
    INGREDIENT_COUNTER = (
        By.XPATH, "//a[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter__num')]")
    # корзина бургера
    BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

    """Модальное окно заказа"""
    # номер заказа
    ORDER_NUMBER = (
        By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")

    # кнопка "Оформит заказ", доступна только авторизованному пользователю
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
