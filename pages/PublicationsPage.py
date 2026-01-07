from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PublicationsPage:
    def __init__(self, driver):
        self.driver = driver
        self.main = (By.XPATH, '//a[contains(text(), "Главная")]')
        self.about_me = (By.XPATH, '//a[contains(text(), "Обо мне")]')
        self.education = (By.XPATH, '//a[contains(text(), "Образование")]')
        self.contacts = (By.XPATH, '//a[contains(text(), "Контакты")]')
        self.submit_application = (By.XPATH, '//a[contains(text(), "Оставить заявку")]')
        self.list_publications = (By.CSS_SELECTOR, "#wb_DropList1")
        self.dropList1_button = (By.CSS_SELECTOR, "#DropList1-button")
        self.last_item_list = (By.CSS_SELECTOR, "#DropList1-menu li:last-child > div")

    def open(self):
        self.driver.get("https://psycholog-vam.ru/AllPublications.html")

    def get_title(self):
        return self.driver.title

    def checking_element_menu_main(self):
        element_main = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.main))
        element_main.click()

    def checking_element_menu_about_me(self):
        element_education = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.about_me))
        element_education.click()

    def checking_element_menu_education(self):
        element_publications = (WebDriverWait(self.driver, 5)
                                .until(EC.visibility_of_element_located(self.education)))
        element_publications.click()

    def checking_element_menu_contacts(self):
        element_contacts = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.contacts))
        element_contacts.click()

    def checking_element_menu_submit_application(self):
        element_submit_application = (WebDriverWait(self.driver, 5)
                                      .until(EC.visibility_of_element_located(self.submit_application)))
        element_submit_application.click()

    def element_visibility_list_publications(self):
        element_publications = (WebDriverWait(self.driver, 5)
                                .until(EC.visibility_of_element_located(self.list_publications)))
        return element_publications.is_displayed()

    def opening_list_articles(self):
        element_publications = (WebDriverWait(self.driver, 5)
                                .until(EC.visibility_of_element_located(self.list_publications)))
        element_publications.click()

    def checking_tag_value(self):
        element_teg = (WebDriverWait(self.driver, 5)
                       .until(EC.visibility_of_element_located(self.dropList1_button)))
        return element_teg.get_attribute("aria-expanded")

    def clicking_last_item_list(self):
        last_item_list = (WebDriverWait(self.driver, 5)
                          .until(EC.visibility_of_element_located(self.last_item_list)))
        last_item_list.click()
