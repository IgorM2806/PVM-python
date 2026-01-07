import pytest
import allure

from pages.HomePage import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.ElementPosition import ElementPosition
from utilities.logger import logger

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

class TestMainMenu:
    @allure.feature("Тестирование меню Главной страницы 'HomePage'")
    @allure.story("Проверка заголовка страницы")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход на страницу 'Обо мне' и проверка заголовка страницы.")
    def test_main_menu_about_me(self, homepage):
        logger.info("Running the test 'test_main_menu_about_me'")

        homepage.checking_element_about_me()

        try:
            assert "About me" in homepage.get_title(), f"Переход не на ту страницу!"
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

        logger.info("Test 'test_main_menu_about_me' was successful!")

    @allure.feature("Тестирование меню Главной страницы 'HomePage'")
    @allure.story("Проверка главного Меню - пункт 'Образование'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход на страницу 'Образование' и проверка заголовка страницы.")
    def test_main_menu_education(self, homepage):
        logger.info("Running the test 'test_main_menu_education'")

        homepage.checking_element_menu_education()

        try:
            assert "Education" in homepage.get_title(), f"Переход не на ту страницу!"
        except AssertionError as e:
            logger.error(f"Test 'test_main_menu_education'  failed with error: {e}")

        logger.info("Test 'test_main_menu_education' was successful!")

    @allure.feature("Тестирование меню Главной страницы 'HomePage'")
    @allure.story("Проверка главного Меню - пункт 'Публикации'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход на страницу 'Публикации' и проверка заголовка страницы.")
    def test_main_menu_publications(self, homepage):
        logger.info("Running the test 'test_main_menu_publications'")

        homepage.checking_element_menu_publications()

        try:
            assert "Все публикации" in homepage.get_title(), f"Переход не на ту страницу!"
        except AssertionError as e:
            logger.error(f"Test 'test_main_menu_publications' failed with error: {e}")
            raise

        logger.info("Test 'test_main_menu_publications' was successful!")

    @allure.feature("Тестирование меню Главной страницы 'HomePage'")
    @allure.story("Проверка главного Меню - пункт 'Контакты'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Переход к разделу 'Контакты' и проверка отображения заголовка раздела.")
    def test_main_menu_contacts(self, homepage):
        logger.info("Running the test 'test_main_menu_contacts'")

        try:
            homepage.checking_element_menu_contacts()

            element_control = (WebDriverWait(homepage.driver, 3, 3)
                               .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text8"))))

            if not ElementPosition.is_element_visible_in_viewport(homepage.driver, element_control):
                raise AssertionError("Элемент - #wb_Text8 не виден на экране!")

            logger.info("Test 'test_main_menu_contacts' was successful!")

        except AssertionError as e:
            logger.error(f"Element '#wb_Text8' is missing or not visible: {e}")

    @allure.feature("Тестирование меню Главной страницы 'HomePage'")
    @allure.story("Проверка главного Меню - пункт 'Оставить заявку'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода к разделу 'Заявка на консультацию' и проверка отображения названия раздела.")
    def test_main_menu_application(self, homepage):
        logger.info("Running the test 'test_main_menu_application'")

        try:
            homepage.checking_element_menu_application()

            element_control = (WebDriverWait(homepage.driver, 3).
                                until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#wb_Text8"))))

            if not ElementPosition.is_element_visible_in_viewport(homepage.driver, element_control):
                raise AssertionError("Элемент - #wb_Text8 не виден на экране!")

            logger.info("Test 'test_main_menu_application' was successful!")
        except AssertionError as e:
            logger.error(f"Element '#wb_Text8' is missing or not visible: {e}")
