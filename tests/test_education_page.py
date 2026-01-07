import pytest
import allure

from utilities.logger import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.EducationPage import EducationPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    ChromeDriverManager().install()  # Устанавливаем драйвер
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def education_page(browser):
    education_page = EducationPage(browser)
    education_page.open()
    return education_page
class TestEducationPage:

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка открытия страницы 'Образование' и содержания заголовка.")
    def test_education_page_title(self, education_page):
        expected_title = "Education"
        logger.info("Running the test 'test_education_page_title'")

        actual_title = education_page.get_title()

        try:
            assert expected_title in actual_title, \
                f"Значение  'actual_title': {actual_title} не соответствует ожиданию 'expected_title': {expected_title}"
            logger.info(f"The page title value: '{actual_title}' is valid.")
        except AssertionError as e:
            logger.error(f"Test 'test_education_page_title' failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка главного Меню - пункт 'Главная'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Главная' основного меню с проверкой заголовка целевой страницы.")
    def test_education_menu_main(self, education_page):
        logger.info("Running the test 'test_education_menu_main'")
        expected_title = "psycholog-vam"

        education_page.checking_element_menu_main()
        actual_page_title = education_page.get_title()

        try:
            assert expected_title in actual_page_title,(f"Checking whether the value matches 'expected_title':"
                                                        f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_education_menu_main' failed with error: {e}")
            raise

        logger.info("The Test 'test_education_menu_main' was successful!")

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка главного Меню - пункт 'Обо мне'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Обо мне'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_education_menu_about_me(self, education_page):
        logger.info("Running the test 'test_education_menu_about_me'")
        expected_title = "About me"

        education_page.checking_element_menu_about_me()
        actual_page_title = education_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_education_menu_about_me' failed with error: {e}")
            raise

        logger.info("The Test 'test_education_menu_about_me' was successful!")

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка главного Меню - пункт 'Публикации'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Публикации'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_education_menu_publications(self, education_page):
        logger.info("Running the test 'test_education_menu_publications'")
        expected_title = "Все публикации"

        education_page.checking_element_menu_publications()
        actual_page_title = education_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_education_menu_publications' failed with error: {e}")
            raise

        logger.info("The Test 'test_education_menu_publications' was successful!")

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка главного Меню - пункт 'Контакты'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Контакты'"
                        " основного меню с проверкой заголовка раздела.")
    def test_education_menu_contacts(self, education_page):
        logger.info("Running the test 'test_education_menu_contacts'")
        expected_text = "Контакты"

        education_page.checking_element_menu_contacts()
        actual_text = (WebDriverWait(education_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text8"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                  f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_education_menu_contacts' failed with error: {e}")
            raise

        logger.info("The Test 'test_education_menu_contacts' was successful!")

    @allure.feature("Тестирование страницы 'Образование'")
    @allure.story("Проверка главного Меню - пункт 'Оставить заявку'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Оставить заявку'"
                        " основного меню с проверкой заголовка раздела.")
    def test_education_menu_submit_application(self, education_page):
        logger.info("Running the test 'test_education_menu_submit_application'")
        expected_text = "Заявка на консультацию"

        education_page.checking_element_menu_submit_application()
        actual_text = (WebDriverWait(education_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text6"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                  f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_education_menu_submit_application' failed with error: {e}")
            raise

        logger.info("The Test 'test_education_menu_submit_application' was successful!")
