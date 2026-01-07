from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EducationPage:
    def __init__(self, driver):
        self.driver = driver
        self.main = (By.XPATH, '//a[contains(text(), "Главная")]')
        self.about_me = (By.XPATH, '//a[contains(text(), "Обо мне")]')
        self.publications = (By.XPATH, '//a[contains(text(), "Публикации")]')
        self.contacts = (By.XPATH, '//a[contains(text(), "Контакты")]')
        self.submit_application = (By.XPATH, '//a[contains(text(), "Оставить заявку")]')

    def open(self):
        self.driver.get("https://psycholog-vam.ru/Education.html")

    def get_title(self):
        return self.driver.title

    def checking_element_menu_main(self):
        element_main = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.main))
        element_main.click()

    def checking_element_menu_about_me(self):
        element_education = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.about_me))
        element_education.click()

    def checking_element_menu_publications(self):
        element_publications = (WebDriverWait(self.driver, 5)
                                .until(EC.visibility_of_element_located(self.publications)))
        element_publications.click()

    def checking_element_menu_contacts(self):
        element_contacts = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.contacts))
        element_contacts.click()

    def checking_element_menu_submit_application(self):
        element_submit_application = (WebDriverWait(self.driver, 5)
                                      .until(EC.visibility_of_element_located(self.submit_application)))
        element_submit_application.click()
