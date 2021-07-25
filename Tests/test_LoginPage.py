import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        btn = self.loginPage.is_login_btn_exist()
        assert btn


    @pytest.mark.parametrize('username, password',
                             [
                                 ("   ", "   "),
                                 ("   ", "123456"),
                                 ("TestUser123", "   "),
                                 ("invalid", "invalid"),
                                 ("testuser123", "123456")
                             ]
                             )
    def test_invalid_login(self, username, password):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(username, password)
        #time.sleep(2)
        self.loginPage.accept_alert()
        time.sleep(2)
        login_btn = self.loginPage.is_login_btn_exist()
        assert login_btn

    def test_valid_login(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        dashboardtitle = dashboardPage.is_dashboard_text_exist()
        assert dashboardtitle

    def test_logout_btn(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        dashboardPage.click_menu_btn()
        dashboardPage.click_logout_btn()
        self.loginPage.accept_alert()
        login_btn = self.loginPage.is_login_btn_exist()
        assert login_btn
