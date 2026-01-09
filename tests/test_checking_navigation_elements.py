import pytest
import allure

from pages.HomePage import HomePage
from utilities.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    ChromeDriverManager().install()  # Устанавливаем драйвер
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def homepage(browser):
    page = HomePage(browser)
    page.open()  # Автоматически откроем страницу перед каждым тестом
    return page

class TestNavigationElements:
    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка кнопки 'Узнать больше' первого раздела.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по кнопке 'Узнать больше' и проверка заголовка целевой страницы.")
    def test_checking_button_learn_more_main_section(self, homepage):
        logger.info("Running the test 'test_checking_button_learn_more_main_section")
        element_intro_button = (By.CSS_SELECTOR, "#introButton")
        expected_title = "About me"

        homepage.click_element_intro_button(element_intro_button)
        control_title = homepage.get_title()

        try:
            assert expected_title in control_title,\
                f"Значение title открытой страницы: {control_title} не соответствует ожидаемому: {expected_title}"
            logger.info("Test 'test_checking_button_learn_more_main_section' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_button_learn_more_main_section' failed with error: {e}")
            raise

    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка кнопки 'Узнать больше' раздела 'Психологическое консультирование'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по кнопке 'Узнать больше'"
                        " и проверка заголовка целевой страницы 'Психологическое консультирование'.")
    def test_checking_button_learn_more_psychological_counseling(self, homepage):
        logger.info("Running the test 'test_checking_button_learn_more_psychological_counseling'.")
        element_intro_button = (By.CSS_SELECTOR, "#whyButton")
        expected_title = "Psychological counseling"

        homepage.click_element_intro_button(element_intro_button)
        control_title = homepage.get_title()

        try:
            assert expected_title in control_title, \
                f"Значение title открытой страницы: {control_title} не соответствует ожидаемому: {expected_title}"
            logger.info("Test 'test_checking_button_learn_more_psychological_counseling' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_button_learn_more_psychological_counseling' failed with error: {e}")
            raise

    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка кнопки 'Узнать больше' раздела 'Карьерное консультирование и профориентация'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по кнопке 'Узнать больше'"
                        " и проверка заголовка целевой страницы 'Карьерное консультирование и профориентация'.")
    def test_checking_button_learn_more_career_counseling(self, homepage):
        logger.info("Running the test 'test_checking_button_learn_more_career_counseling'.")
        element_intro_button = (By.CSS_SELECTOR, "#Button2")
        expected_title = "KKP"

        homepage.click_element_intro_button(element_intro_button)
        control_title = homepage.get_title()

        try:
            assert expected_title in control_title, \
                f"Значение title открытой страницы: {control_title} не соответствует ожидаемому: {expected_title}"
            logger.info("Test 'test_checking_button_learn_more_career_counseling' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_button_learn_more_career_counseling' failed with error: {e}")
            raise

    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка кнопки 'Узнать больше' раздела 'Коучинг'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по кнопке 'Узнать больше'"
                        " и проверка заголовка целевой страницы 'Коучинг'.")
    def test_checking_button_learn_more_coaching(self, homepage):
        logger.info("Running the test 'test_checking_button_learn_more_coaching'.")
        element_intro_button = (By.CSS_SELECTOR, "#howButton")
        expected_title = "Coaching"

        homepage.click_element_intro_button(element_intro_button)
        control_title = homepage.get_title()

        try:
            assert expected_title in control_title, \
                f"Значение title открытой страницы: {control_title} не соответствует ожидаемому: {expected_title}"
            logger.info("Test 'test_checking_button_learn_more_coaching' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_button_learn_more_coaching' failed with error: {e}")
            raise

    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка ссылки 'Подробнее...' раздела 'Публикации'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по ссылке 'Подробнее...'"
                        " и проверка заголовка целевой страницы 'Publication_general'.")
    def test_checking_link_more_information_publication_section(self, homepage):
        logger.info("Running the test 'test_checking_link_more_information_publication_section'.")
        element_intro_button = (By.CSS_SELECTOR, ".blogtext a")
        expected_title = "Publication_general"

        homepage.click_element_intro_button(element_intro_button)
        control_title = homepage.get_title()

        try:
            assert expected_title in control_title, \
                f"Значение title открытой страницы: {control_title} не соответствует ожидаемому: {expected_title}"
            logger.info("Test 'test_checking_link_more_information_publication_section' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_link_more_information_publication_section' failed with error: {e}")
            raise

    @allure.feature("Тестирование элементов навигации Главной страницы 'HomePage'")
    @allure.story("Проверка кнопки 'Вверх' в футере страницы.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход по кнопке 'Вверх'"
                        " и проверка отображения логотипа.")
    def test_checking_button_up_futter(self, homepage):
        logger.info("Running the test 'test_checking_button_up_futter'.")
        element_intro_button = (By.CSS_SELECTOR, "#Button1")

        homepage.click_element_intro_button(element_intro_button)
        control_element = (WebDriverWait(homepage.driver, 5)
                           .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#RollOver1"))))
        result = control_element.is_displayed()
        try:
            assert result is True, \
                f"Элемент логотип: {control_element} не отображается в видимой части страницы."
            logger.info("Test 'test_checking_button_up_futter' was successful!")
        except AssertionError as e:
            logger.error(f"Test 'test_checking_button_up_futter' failed with error: {e}")
            raise