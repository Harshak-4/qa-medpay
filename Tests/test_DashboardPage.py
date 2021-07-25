import time
import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Dashboard(BaseTest):

    def test_menu_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(3)
        menubtn = dashboardPage.is_menu_btn_exist()
        assert menubtn

    def test_placeorder_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(3)
        placeorder = dashboardPage.is_place_order_btn_exist()
        assert placeorder

    def test_partner_order_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_partner_order_exists()
        assert name.lower() == TestData.COLUMN_PARTNER_TITLE.lower()

    def test_customer_name_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_customer_name_exists()
        assert name.lower() == TestData.COLUMN_CUSTOMER_TITLE.lower()

    def test_order_status_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_order_status_exists()
        assert name.lower() == TestData.COLUMN_ORDER_TITLE.lower()

    def test_payment_status_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_payment_status_exists()
        assert name.lower() == TestData.COLUMN_STATUS_TITLE.lower()

    def test_city_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_city_exists()
        assert name.lower() == TestData.COLUMN_CITY_TITLE.lower()

    def test_actions_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_action_exists()
        assert name.lower() == TestData.COLUMN_ACTION_TITLE.lower()

    def test_notes_exists(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        name = dashboardPage.is_column_notes_exists()
        assert name.lower() == TestData.COLUMN_NOTES_TITLE.lower()

    def test_order_btn(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        dashboardPage.click_menu_btn()
        time.sleep(1)
        order_btn = dashboardPage.click_orders_btn()
        assert order_btn

    def test_cancel_order_stay(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        stay_btn = dashboardPage.click_cancel_btn()
        assert stay_btn

    def test_cancel_order_yes(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        yes_btn = dashboardPage.click_cancel_yes()
        assert yes_btn

    def test_cancel_order_no_reason(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        submit_btn = dashboardPage.click_cancel_reason()
        assert submit_btn

    def test_place_order(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        order_dolo = dashboardPage.place_order(TestData.PARTNER_ORDER_ID, TestData.NAME, TestData.MOBILE, TestData.ALTERNATE_MOBILE, TestData.EMAIL, TestData.ADDRESS, TestData.LANDMARK, TestData.PINCODE, TestData.CITY, TestData.STATE, TestData.DOCTOR, TestData.MEDICINE_NAME)
        assert order_dolo

    def test_export_order(self):
        self.loginPage = LoginPage(self.driver)
        dashboardPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(1)
        export_btn = dashboardPage.download_orders()
        assert export_btn