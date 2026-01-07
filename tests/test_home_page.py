import time

import pytest
import allure

from utilities.logger import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePage import HomePage

@pytest.fixture(scope="function")
def browser():
    ChromeDriverManager().install()  # Устанавливаем драйвер
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def homepage(browser):
    page = HomePage(browser)
    page.open()
    return page

class TestHomePage:
    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка перехода на страницу.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка перехода на страницу и проверка содержания заголовка страницы.")
    def test_homepage_title(self, homepage):
        expected_title = "psycholog-vam"
        actual_title = homepage.get_title()
        logger.info(f"Checking whether the value matches 'expected_title':"
                    f" {expected_title} and 'actual_title': {actual_title}")

        try:
            assert expected_title in actual_title, \
            f"Значение  'actual_title': {actual_title} не соответствует ожиданию 'expected_title': {expected_title}"
            logger.info("The page title value is valid.")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения логотипа на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения логотипа на странице.")
    def test_homepage_logo(self, homepage):
        logger.info("We check the presence of the logo on the main page.")

        try:
            assert homepage.is_logo_visible(), "The logo is not displayed on the main page!"
            logger.info("The logo is displayed on the main page!")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения фото на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения фото на странице.")
    def test_homepage_foto(self, homepage):
        logger.info("Checking for photos on the page!")

        try:
            assert homepage.is_photo_visible(), f"The photo is not displayed on the main page!"
            logger.info("The photo is displayed on the main page!")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения 1-го раздела на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения 1-го раздела на странице и содержание заголовка раздела.")
    def test_homepage_first_section(self, homepage):
        expected_text = "Психологическое консультирование"
        logger.info(f"Checking the display of the header of the first section!")

        try:
            assert homepage.first_section_has_expected_text(expected_text=expected_text),\
                "The first section does not contain the expected text."
            logger.info("The first section contains the expected text.")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise
    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения 2-го раздела на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения 2-го раздела на странице и содержание заголовка раздела.")
    def test_homepage_two_section(self, homepage):
        expected_text = "Карьерное консультирование и профориентация"
        logger.info(f"Checking the display of the header of the two section!")

        try:
            assert homepage.second_section_has_expected_text(expected_text=expected_text),\
                "The two section does not contain the expected text."
            logger.info("The two section contains the expected text.")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения 3-го раздела на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения 3-го раздела на странице и содержание заголовка раздела.")
    def test_homepage_three_section(self, homepage):
        expected_text = "Коучинг"
        logger.info("Checking the display of the header of the three section!")

        try:
            assert homepage.third_section_has_expected_text(expected_text=expected_text), \
                "The three section does not contain the expected text."
            logger.info("The three section contains the expected text.")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения  раздела 'Публикации' на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения раздела 'Публикации' на странице и содержание заголовка раздела.")
    def test_displaying_publication_block(self, homepage):
        expected_text = "Публикации"
        logger.info("Checking the display of the header of the publication block!")

        try:
            assert homepage.publications_block_is_visible(expected_text=expected_text),\
                "The 'Publications' block does not contain the expected text!"
            logger.info("The 'Publications' block contains the expected text!")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения информации в  разделе 'Публикации'.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения в  разделе 'Публикации' актуальной информации.")
    def test_checking_displaying_information_publications_section(self, homepage):
        logger.info("Running the test 'checking_displaying_information_publications_section'")

        result = homepage.not_displaying_information_publications_section()

        try:
            for item in result:
                assert item != "Loading date...", f"В секции 'Публикации' отображается сообщение '{item}'"
                assert item != "Сервис временно недоступен, извините за неудобства!",\
                    f"В секции 'Публикации' отображается сообщение '{item}'"
            logger.info("The Test 'test_checking_displaying_information_publications_section' was successful!")

        except AssertionError as e:
            logger.error(f"Test 'test_checking_displaying_information_publications_section' failed with error: {e}")
            raise



    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения  раздела 'Контакты' на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения раздела 'Контакты' на странице и содержание заголовка раздела.")
    def test_displaying_contacts_block(self, homepage):
        expected_text = "Контакты"
        logger.info("Checking the display of the header of the contacts block!")

        try:
            assert homepage.contacts_block_is_visible(expected_text=expected_text),\
                "The Contacts block does not contain the expected text!"
            logger.info("The test 'test_displaying_contacts_block' was successful")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise
    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения  раздела 'Контакты' на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения раздела 'Контакты' на странице и содержание блока 'Позвони мне'.")
    def test_displaying_contacts_block_telephone(self, homepage):
        expected_phone_number = "+7 903 344 89 75"
        logger.info("Checking the display of the header of the block telephone!")

        try:
            assert homepage.phone_number_is_visible(), \
                f"The text of the 'phone_element' element does not match {expected_phone_number} or is not displayed!"
            logger.info("The test 'test_displaying_contacts_block_telephone' was successful")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения  раздела 'Контакты' на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения раздела 'Контакты' на странице и содержание блока 'Расположение'.")
    def test_displaying_contacts_block_location(self, homepage):
        expected_text = "Город Казань"
        logger.info("Checking the display of the header of the block location!")

        try:
            assert homepage.location_is_visible(),\
                f"The content of block_location does not match the expectation: {expected_text} or is not displayed!"
            logger.info("The test 'test_displaying_contacts_block_location' was successful")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise

    @allure.feature("Тестирование страницы 'Главная'")
    @allure.story("Проверка отображения  раздела 'Заявка на консультацию' на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка отображения раздела 'Заявка на консультацию'"
                        " на странице и содержание заголовка раздела.")
    def test_application_block_text(self, homepage):
        expected_text = "Заявка на консультацию"
        logger.info("We are checking the display of the 'Request for consultation' block header!")

        try:
            assert homepage.application_block_has_expected_text(expected_text=expected_text),\
                "The 'Request for consultation' block does not contain the expected text!"
            logger.info("The test 'test_application_block_text' was successful")
        except AssertionError as e:
            logger.error(f"Test failed with error: {e}")
            raise