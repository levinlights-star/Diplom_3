**Описание**
Проект содержит Автотесты для UI приложения Stellar Burgers.

**Структура проекта**
├── allure_results                   # для Allure-отчётов
│
├── data/
│   └── config.py                    # URL сайта
│   └── user_data.py                 # Функции для пользователя
│ 
├── locators/
│   └── feed_page_locators.py        # Локаторы для страницы Лента заказов
│   └── login_page_locators.py       # Локаторы для страницы авторизации
│   └── main_page_locators.py        # Локаторы для главной страницы 
│   └── register_page_locators.py    # Локаторы для страницы регистрации
│ 
├── pages/
│   └── base_page.py                 # page object основные
│   └── feed_page.py                 # page object страницы ленты заказов
│   └── login_page.py                # page object страницы авторизации
│   └── main_page.py                 # page object главной страницы
│   └── register_page.py             # page object страницы регистрации
│ 
├── tests/
│   └── test_feed_page.py            # Тесты на странице ленты заказов
│   └── test_main_page.py            # Тесты на главной странице
│ 
├── conftest.py                      # Фикстуры
├── pytest.ini                       # Файл конфигурации pytest
├── .gitignore                       # Файл для игнорирования файлов в Git
├── README.md                        # Описание проекта
└── requirements.txt                 # Список внешних зависимостей


**Технологии**
Python 3.14+
pytest — фреймворк для тестирования
allure-pytest — генерация отчётов Allure

**Установка и запуск**
1. Клонируйте репозиторий
2. Установите зависимости: pip3 install -r requirements.txt (или pip install -r requirements.txt)
3. Запустите тесты: pytest
4. Для генерации отчёта Allure: pytest --alluredir=allure_results и allure serve allure_results


Пример выполнения тестов:
tests/test_feed_page.py::TestFeedPage::test_today_orders_counter_increases[firefox] 
------------------------------------------------------------------------------------------- live log setup -------------------------------------------------------------------------------------------
INFO     conftest:conftest.py:46 Сгенерированный данные: {'email': 'bolrscvgtp@mail.ru', 'password': 'zlafrfmkdy', 'name': 'hsucfqauwi'}
------------------------------------------------------------------------------------------- live log call --------------------------------------------------------------------------------------------
INFO     test_feed_page:test_feed_page.py:54 Выполнено за сегодня до моего заказа: 165
INFO     pages.main_page:main_page.py:113 Номер моего заказа: 379860
INFO     test_feed_page:test_feed_page.py:64 Выполнено за сегодня после моего заказа: 166
PASSED                                                                                          