import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_selector = (By.TAG_NAME, 'title')
        self.logo_selector = (By.CSS_SELECTOR, "#RollOver1 .hover")
        self.foto_selector = (By.CSS_SELECTOR, "#Picture2")
        self.first_section_selector = (By.CSS_SELECTOR, "#whyHeading")
        self.second_section_selector = (By.CSS_SELECTOR, "#Heading1")
        self.third_section_selector = (By.CSS_SELECTOR, "#howHeading")
        self.publications_block_selector = (By.CSS_SELECTOR, "#testimonialsHeading")
        self.contacts_block_selector = (By.CSS_SELECTOR, "#wb_Text8 span")
        self.phone_number_selector = (By.XPATH, "//ul[@id='formListView']/li[p[text()='+7 903 344 89 75']]//p")
        self.location_selector = (By.XPATH, "//ul[@id='formListView']/li[p[text()='Город Казань']]//p")
        self.application_block_selector = (By.CSS_SELECTOR, "#wb_Text6 span")
        self.about_me = (By.XPATH, '//a[contains(text(), "Обо мне")]')
        self.element_education = (By.XPATH, '//a[contains(text(), "Образование")]')
        self.element_publications = (By.XPATH, '//a[contains(text(), "Публикации")]')
        self.element_contacts = (By.XPATH, '//a[contains(text(), "Контакты")]')
        self.element_application = (By.XPATH, '//a[contains(text(), "Оставить заявку")]')
        self.element_blog_subject = (By.CSS_SELECTOR, "#Article1 .blogsubject")
        self.element_blog_subject_span = (By.CSS_SELECTOR, "#Article1 span.blogsubject > span")

    def open(self):
        self.driver.get("https://psycholog-vam.ru")

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def fill_form_and_submit(self, name, email, message):
        """
        Заполняет форму и отправляет её.

        :param name: Имя пользователя
        :param email: Email пользователя
        :param message: Сообщение
        """
        field_name = (WebDriverWait(self.driver, 3)
                      .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#formName"))))
        field_email = self.driver.find_element(By.CSS_SELECTOR, "#formEmail")
        field_message = self.driver.find_element(By.CSS_SELECTOR, "#formMessage")

        field_name.send_keys(name)
        field_email.send_keys(email)
        field_message.send_keys(message)

    def installing_checkbox(self):
        """
        Устанавливает флажок согласия на обработку персональных данных.
        """

        element_checkbox = (WebDriverWait(self.driver, 10)
                            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#privacyConsent"))))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                   element_checkbox)

        element_checkbox.click()

    def button_click(self):
        element_button = self.driver.find_element(By.CSS_SELECTOR, "#formButton")
        element_button.click()

    def wait_for_alert(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def is_logo_visible(self):
        logo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logo_selector))
        return logo.is_displayed()

    def is_photo_visible(self):
        foto = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.foto_selector))
        return foto.get_attribute('src') == "https://psycholog-vam.ru/images/DSC_6602_smol.JPG"

    def first_section_has_expected_text(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.first_section_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.first_section_selector))

        return expected_text in visible_element.text

    def second_section_has_expected_text(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.second_section_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.second_section_selector))

        return expected_text in visible_element.text

    def third_section_has_expected_text(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.third_section_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.third_section_selector))

        return expected_text in visible_element.text

    def publications_block_is_visible(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.publications_block_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.publications_block_selector))

        return expected_text in visible_element.text

    def contacts_block_is_visible(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.contacts_block_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.contacts_block_selector))

        return expected_text in visible_element.text

    def application_block_has_expected_text(self, expected_text):
        section_element = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.application_block_selector))
        self.driver.execute_script("arguments[0].scrollIntoView();", section_element)
        visible_element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(self.application_block_selector))

        return expected_text in visible_element.text

    def phone_number_is_visible(self):
        number = (WebDriverWait(self.driver, 5)
                  .until(EC.visibility_of_element_located(self.phone_number_selector)))
        return number.is_displayed()

    def location_is_visible(self):
        loc = (WebDriverWait(self.driver, 5)
                .until(EC.visibility_of_element_located(self.location_selector)))
        return loc.is_displayed()

    def checking_element_about_me(self):
        element_about_me = (
            WebDriverWait(self.driver, 3).
            until(EC.visibility_of_element_located(self.about_me)))
        element_about_me.click()

    def checking_element_menu_education(self):
        element_education = (
            WebDriverWait(self.driver, 3).
            until(EC.visibility_of_element_located(self.element_education)))
        element_education.click()

    def checking_element_menu_publications(self):
        element_publications = (
            WebDriverWait(self.driver, 3).
            until(EC.visibility_of_element_located(self.element_publications)))
        element_publications.click()

    def checking_element_menu_contacts(self):
        element_contacts = (
            WebDriverWait(self.driver, 3).
            until(EC.visibility_of_element_located(self.element_contacts)))
        element_contacts.click()

    def checking_element_menu_application(self):
        element_application = (
            WebDriverWait(self.driver, 3).
            until(EC.visibility_of_element_located(self.element_application)))
        element_application.click()

    def not_displaying_information_publications_section(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        control_element = (WebDriverWait(self.driver, 5)
                           .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#Article1"))))
        self.driver.execute_script("arguments[0].scrollIntoView();", control_element)
        '''time.sleep(3)'''
        blog_subject = (WebDriverWait(self.driver, 5)
                        .until(EC.visibility_of_element_located(self.element_blog_subject)).text)
        blog_subject_span = (WebDriverWait(self.driver, 5)
                             .until(EC.visibility_of_element_located(self.element_blog_subject_span)).text)
        return blog_subject, blog_subject_span

    def click_element_intro_button(self, locator):
        element_click = (WebDriverWait(self.driver, 5)
                                .until(EC.visibility_of_element_located(locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element_click)
        element_click.click()
































