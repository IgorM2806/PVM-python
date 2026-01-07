import pytest
import allure

from utilities.logger import logger
from pages.AboutMePage import AboutMePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    ChromeDriverManager().install()  # Устанавливаем драйвер
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def about_me_page(browser):
    about_me_page = AboutMePage(browser)
    about_me_page.open()
    return about_me_page

class TestAboutMePage:
    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка открытия страницы 'Обо мне' и заголовка.")
    def test_about_me_page_title(self, about_me_page):
        expected_title = "About me"
        logger.info("Running the test 'test_about_me_page_title'")

        actual_title = about_me_page.get_title()

        try:
            assert expected_title in actual_title, \
                f"Значение  'actual_title': {actual_title} не соответствует ожиданию 'expected_title': {expected_title}"
            logger.info(f"The page title value: '{actual_title}' is valid.")
        except AssertionError as e:
            logger.error(f"Test 'test_about_me_page_title' failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка главного Меню - пункт 'Главная'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Главная' основного меню с проверкой заголовка целевой страницы.")
    def test_about_me_menu_main(self, about_me_page):
        logger.info("Running the test 'test_about_me_menu_main'")
        expected_title = "psycholog-vam"

        about_me_page.checking_element_menu_main()
        actual_page_title = about_me_page.get_title()

        try:
            assert expected_title in actual_page_title,(f"Checking whether the value matches 'expected_title':"
                                                        f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_about_me_menu_main' failed with error: {e}")
            raise

        logger.info("The Test 'test_about_me_menu_main' was successful!")

    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка главного Меню - пункт 'Образование'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Образование'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_about_me_menu_education(self, about_me_page):
        logger.info("Running the test 'test_about_me_menu_education'")
        expected_title = "Education"

        about_me_page.checking_element_menu_education()
        actual_page_title = about_me_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_about_me_menu_education' failed with error: {e}")
            raise

        logger.info("The Test 'test_about_me_menu_education' was successful!")

    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка главного Меню - пункт 'Публикации'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Публикации'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_about_me_menu_publications(self, about_me_page):
        logger.info("Running the test 'test_about_me_menu_publications'")
        expected_title = "Все публикации"

        about_me_page.checking_element_menu_publications()
        actual_page_title = about_me_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_about_me_menu_publications' failed with error: {e}")
            raise

        logger.info("The Test 'test_about_me_menu_publications' was successful!")

    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка главного Меню - пункт 'Контакты'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Контакты'"
                        " основного меню с проверкой заголовка раздела.")
    def test_about_me_menu_contacts(self, about_me_page):
        logger.info("Running the test 'test_about_me_menu_contacts'")
        expected_text = "Контакты"

        about_me_page.checking_element_menu_contacts()
        actual_text = (WebDriverWait(about_me_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text8"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                         f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_about_me_menu_contacts' failed with error: {e}")
            raise

        logger.info("The Test 'test_about_me_menu_contacts' was successful!")

    @allure.feature("Тестирование страницы 'Обо мне'")
    @allure.story("Проверка главного Меню - пункт 'Оставить заявку'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Оставить заявку'"
                        " основного меню с проверкой заголовка раздела.")
    def test_about_me_menu_submit_application(self, about_me_page):
        logger.info("Running the test 'test_about_me_menu_submit_application'")
        expected_text = "Заявка на консультацию"

        about_me_page.checking_element_menu_submit_application()
        actual_text = (WebDriverWait(about_me_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text6"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                  f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_about_me_menu_submit_application' failed with error: {e}")
            raise

        logger.info("The Test 'test_about_me_menu_submit_application' was successful!")





