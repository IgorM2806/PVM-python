import pytest
import allure

from utilities.logger import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.PublicationsPage import PublicationsPage
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
def publications_page(browser):
    publications_page = PublicationsPage(browser)
    publications_page.open()
    return publications_page
class TestPublicationsPage:
    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка открытия страницы 'Публикации' и содержания заголовка.")
    def test_publications_page_title(self, publications_page):
        logger.info("Running the test 'test_publications_page_title'")
        expected_title = "Все публикации"

        actual_title = publications_page.get_title()

        try:
            assert expected_title in actual_title, \
                f"Значение  'actual_title': {actual_title} не соответствует ожиданию 'expected_title': {expected_title}"
            logger.info(f"The page title value: '{actual_title}' is valid.")
        except AssertionError as e:
            logger.error(f"Test 'test_publications_page_title' failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка главного Меню - пункт 'Главная'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Главная' основного меню с проверкой заголовка целевой страницы.")
    def test_publications_menu_main(self, publications_page):
        logger.info("Running the test 'test_publications_menu_main'")
        expected_title = "psycholog-vam"

        publications_page.checking_element_menu_main()
        actual_page_title = publications_page.get_title()

        try:
            assert expected_title in actual_page_title,(f"Checking whether the value matches 'expected_title':"
                                                        f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_publications_menu_main' failed with error: {e}")
            raise

        logger.info("The Test 'test_publications_menu_main' was successful!")

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка главного Меню - пункт 'Обо мне'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Обо мне'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_publications_menu_about_me(self, publications_page):
        logger.info("Running the test 'test_publications_menu_about_me'")
        expected_title = "About me"

        publications_page.checking_element_menu_about_me()
        actual_page_title = publications_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_publications_menu_about_me' failed with error: {e}")
            raise

        logger.info("The Test 'test_publications_menu_about_me' was successful!")

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка главного Меню - пункт 'Образование'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Образование'"
                        " основного меню с проверкой заголовка целевой страницы.")
    def test_publications_menu_education(self, publications_page):
        logger.info("Running the test 'test_publications_menu_education'")
        expected_title = "Education"

        publications_page.checking_element_menu_education()
        actual_page_title = publications_page.get_title()

        try:
            assert expected_title in actual_page_title, (f"Checking whether the value matches 'expected_title':"
                                                         f" {expected_title} and 'actual_title': {actual_page_title}")
        except AssertionError as e:
            logger.error(f"The test 'test_publications_menu_education' failed with error: {e}")
            raise

        logger.info("The Test 'test_publications_menu_education' was successful!")

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка главного Меню - пункт 'Контакты'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Контакты'"
                        " основного меню с проверкой заголовка раздела.")
    def test_publications_menu_contacts(self, publications_page):
        logger.info("Running the test 'test_publications_menu_contacts'")
        expected_text = "Контакты"

        publications_page.checking_element_menu_contacts()
        actual_text = (WebDriverWait(publications_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text8"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                  f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_publications_menu_contacts' failed with error: {e}")
            raise

        logger.info("The Test 'test_publications_menu_contacts' was successful!")

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка главного Меню - пункт 'Оставить заявку'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по пункту 'Оставить заявку'"
                        " основного меню с проверкой заголовка раздела.")
    def test_publications_menu_submit_application(self, publications_page):
        logger.info("Running the test 'test_publications_menu_submit_application'")
        expected_text = "Заявка на консультацию"

        publications_page.checking_element_menu_submit_application()
        actual_text = (WebDriverWait(publications_page.driver, 5)
                       .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text6"))).text)

        try:
            assert expected_text in actual_text, (f"Checking whether the value matches 'expected_text':"
                                                  f" {expected_text} and 'actual_text': {actual_text}")
        except AssertionError as e:
            logger.error(f"The test 'test_publications_menu_submit_application' failed with error: {e}")
            raise

        logger.info("The Test 'test_publications_menu_submit_application' was successful!")

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка отображения списка публикаций.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения выпадающего списка публикаций.")
    def test_displaying_list_publications(self, publications_page):
        logger.info("Running the test 'test_displaying_list_publications'")

        result = publications_page.element_visibility_list_publications()
        try:
            assert result is True, "Выпадающий Список публикаций не отображается на странице!"
            logger.info("The Test 'test_displaying_list_publications' was successful!")
        except AssertionError as e:
            logger.error(f"The test 'test_displaying_list_publications' failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка открытия  списка публикаций.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения выпадающего списка публикаций.")
    def test_list_publications_open(self, publications_page):
        logger.info("Running the test 'test_list_publications_open'")
        expected_teg_value = "true"

        publications_page.opening_list_articles()
        attribute_value = publications_page.checking_tag_value()

        try:
            assert attribute_value in expected_teg_value, \
                f"Значение атрибута 'attribute_value': {attribute_value} - список статей не открылся!"
            logger.info("The Test 'test_list_publications_open' was successful!")
        except AssertionError as e:
            logger.error(f"The test 'test_list_publications_open' failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Публикации'")
    @allure.story("Проверка перехода по элементу списка публикаций.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по последнему элементу списка публикаций.")
    def test_clicking_last_item_list(self, publications_page):
        logger.info("Running the test 'test_clicking_last_item_list'")
        expected_title = "Publication_general"

        publications_page.opening_list_articles()
        publications_page.clicking_last_item_list()
        actual_title = publications_page.get_title()

        try:
            assert expected_title in actual_title,\
                f"Checking whether the value matches 'expected_title': {expected_title} and 'actual_title': {actual_title}"
            logger.info("The Test 'test_clicking_last_item_list' was successful!")
        except AssertionError as e:
            logger.error(f"The test 'test_clicking_last_item_list' failed with error: {e}")
            raise


