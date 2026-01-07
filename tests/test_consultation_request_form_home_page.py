import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePage import HomePage
from utilities.logger import logger


@pytest.fixture(scope="function")
def browser():
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def homepage(browser):
    page = HomePage(browser)
    page.open()  # Автоматически откроем страницу перед каждым тестом
    return page


class TestConsultationRequestForm:
    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка успешной отправки формы с валидными значениями.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Отправка формы с валидными значениями и проверка содержания аллерта.")
    def test_field_name_successful(self, homepage):
        name = "Tester"
        email = "1111@mail.ru"
        messages = "Test"
        logger.info(f"Test Execution 'test_field_name_successful' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()
        expected_message = "Сообщение отправлено!"
        try:
            assert alert_text == expected_message, f"The alert message differs in content: {expected_message}"
        except AssertionError as e:
            logger.info(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_field_name_successful' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы с невалидным значением в поле 'Имя'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы с пустым полем 'имя' и проверка содержания аллерта.")
    def test_empty_field_name(self, homepage):
        name = ""
        email = "1111@mail.ru"
        messages = "Test"
        logger.info(f"Test Execution 'test_field_name_successful' with values name: 'пустое значение',"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()
        expected_message = 'Поле "Введите своё имя" не заполнено.'

        try:
            assert alert_text == expected_message, f"Сообщение в Alert не соответствует ожиданию {alert_text}"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_empty_field_name' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы с невалидным значением в поле 'Имя'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы с одним символом в поле 'имя' и проверка содержания аллерта.")
    def test_one_character_field_name(self, homepage):
        name = "T"
        email = "1111@mail.ru"
        messages = "Test"
        logger.info(f"Test Execution 'test_field_name_successful' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()
        expected_message = "Имя должно содержать от 2 до 30 символов."

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_one_character_field_name' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы с невалидным значением в поле 'Имя'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы с значением более 30 символов в поле 'имя' и проверка содержания аллерта.")
    def test_long_value_field_name(self, homepage):
        name = "testertestertestertestertestertestertestertestertestertestertester"
        email = "1111@mail.ru"
        messages = "Test"
        logger.info(f"Test Execution 'test_long_value_field_name' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()
        expected_message = "Имя должно содержать от 2 до 30 символов."

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_long_value_field_name' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы с невалидным значением в поле 'Email'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы с пустым полем 'Email' и проверка содержания аллерта.")
    def test_empty_field_email(self, homepage):
        name = "Tester"
        email = ""
        messages = "Test"
        logger.info(f"Test Execution 'test_empty_field_email' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()


        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()
        expected_message = 'Поле "Введите адрес электронной почты" не заполнено.'

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_empty_field_email' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы с невалидным значением в поле 'Email'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы с невалидным значением в поле 'Email' и проверка содержания аллерта.")
    def test_invalid_value_field_email(self, homepage):
        name = "Tester"
        email = "ingcmail.ru"
        messages = "Test"
        expected_message = 'Адрес электронной почты указан неверно.'
        logger.info(f"Test Execution 'test_invalid_value_field_email' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_invalid_value_field_email' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы без подтверждения согласия на обработку данных.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы без подтверждения согласия на обработку данных и проверка содержания аллерта.")
    def test_lack_consent(self, homepage):
        name = "Tester"
        email = "1111@mail.ru"
        messages = "Test"
        expected_message = 'Необходимо согласиться с условиями конфиденциальности.'
        logger.info(f"Test Execution 'test_lack_consent' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        homepage.fill_form_and_submit(name, email, messages)
        homepage.button_click()

        alert = homepage.wait_for_alert()
        alert_text = alert.text.strip()

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test 'test_lack_consent' failed with error: {e}")
            raise

        alert.accept()
        logger.info("Test 'test_lack_consent' was successful!")

    @allure.feature("Тестирование формы 'Заявка на консультацию'")
    @allure.story("Проверка блокировки отправки формы при попытке повторной отправки после успешной отпрваки формы.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Отправка формы сразу после успешной отправки формы 'Заявка на консультацию'.")
    def test_limitation_re_sending(self, homepage):
        name = "Tester"
        email = "1111@mail.ru"
        messages = "Test"
        expected_message = 'Повторная отправка доступна через 1 минуту.'
        logger.info(f"Test Execution 'test_limitation_re_sending' with values name: {name},"
                    f" email: {email}, messages: {messages}")

        logger.info("Первая успешная отправка формы.")
        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        first_alert = homepage.wait_for_alert()
        first_alert.accept()

        logger.info("Попытка повторной отправки формы сразу после успешной первой попытки.")
        homepage.fill_form_and_submit(name, email, messages)
        homepage.installing_checkbox()
        homepage.button_click()

        second_alert = homepage.wait_for_alert()
        alert_text = second_alert.text.strip()

        try:
            assert alert_text == expected_message, f"Сообщение в alert отличается по содержанию: {expected_message}"
        except AssertionError as e:
            logger.error(f"Test 'test_limitation_re_sending' failed with error: {e}")
            raise

        second_alert.accept()
        logger.info("Test 'test_limitation_re_sending' was successful!")






























