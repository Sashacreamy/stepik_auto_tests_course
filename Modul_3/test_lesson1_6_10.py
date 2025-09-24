from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):

    def setUp(self):
        # Настройка перед каждым тестом
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # Завершение после каждого теста
        self.browser.quit()

    def test_registration1(self):
        # Тест для первой страницы (должен проходить)
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Заполняем обязательные поля
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("Smolensk")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки
        time.sleep(4)

        # Проверяем результат
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # def test_registration2(self):
        # Тест для второй страницы (должен падать)
        # link = "http://suninjuly.github.io/registration2.html"
        # self.browser.get(link)

        # Пытаемся заполнить обязательные поля
        # Этот тест должен упасть с NoSuchElementException
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("Smolensk")

        # Отправляем форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки
        time.sleep(4)

        # Проверяем результат
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()