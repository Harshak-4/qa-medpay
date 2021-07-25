from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.DashboardPage import DashboardPage


class LoginPage(BasePage):
    """By Locators name"""
    textbox_username_id = (By.ID, "username")
    textbox_password_id = (By.ID, "password")
    #button_login_class = (By.CLASS_NAME, "chakra-button css-1kz2znw")
    button_login_xpath = (By.XPATH, '//*[@id="root"]/div/form/div[3]/button')

    """Constructors of the page class"""
    def  __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.textbox_username_id, username)
        self.do_send_keys(self.textbox_password_id, password)
        self.do_click(self.button_login_xpath)
        return DashboardPage(self.driver)

    def is_login_btn_exist(self):
        login_btn = self.is_visible(self.button_login_xpath)
        return login_btn