import random
import string
import allure


@allure.step("Генерирует строку из букв нижнего регистра, в качестве параметра передаём длину строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


DOMAINS = ['mail.ru', 'yandex.ru', 'gmail.com']


@allure.step("Функция для генерации email")
def generate_email():
    domain = random.choice(DOMAINS)
    return f"{generate_random_string(10)}@{domain}"


@allure.step("Генерирует email, пароль и имя пользователя")
def generate_user_data():
    return {
        "email": generate_email(),
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }
