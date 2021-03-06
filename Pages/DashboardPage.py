import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    """By Locators name"""
    dashboard_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[1]/p')
    partner_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[1]/p')
    customer_name_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[2]/p')
    order_status_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[5]')
    payment_status_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[6]')
    city_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[7]')
    action_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[8]')
    notes_text_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/table/thead/tr/th[9]')
    button_placeorder_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/button')
    button_orders_xpath = (By.XPATH, '//button[contains(text(),"Orders")]')
    button_logout_xpath = (By.XPATH, '//button[contains(text(),"LogOut")]')
    button_menu_xpath = (By.XPATH, '//button[@class="chakra-button css-zke2o8"]')
    button_cancel_xpath = (By.XPATH, '//button[@aria-label="Cancel order"]')
    button_stay_xpath = (By.XPATH, '//button[@class="chakra-button css-1h7v26a"]')
    button_yes_xpath = (By.XPATH, '//button[@class="chakra-button css-1guk514"]')
    button_submit_cancel_xpath = (By.XPATH, '//button[@class="chakra-button css-s2npsv"]')
    dropdown_reason_xpath = (By.XPATH, '//select[@id="reason"]')
    button_export_xpath = (By.XPATH, '//button[contains(text(),"Export Data")]')
    button_manage_orders_xpath = (By.XPATH, '//button[contains(text(),"Manage Orders")]')
    pending_tab_Id = (By.ID, 'tabs-60--tab-0')
    button_orderid_xpath = (By.XPATH, '(//button[@class="chakra-text css-z28hru"])')
    text_name_xpath = (By.XPATH, '//*[@id="chakra-modal--body-338"]/div/div[1]/p[1]')
    checkbox_xpath = (By.XPATH, '//label[@class="chakra-checkbox css-1uiwwan"]')
    button_assign_xpath = (By.XPATH, '/html/body/div/div/div[2]/div/div/div[1]/button[2]')
    assigned_tab_xpath = (By.ID, '//button[@id="tabs-3--tab-1"]')


    """Place order fields locators"""
    textbox_partnerorderid_xpath = (By.XPATH, '//input[@id="partner_order_id"]')
    text_box_Name_xpath = (By.XPATH, '//input[@id="name"]')
    textbox_mobile_xpath = (By.XPATH, '//input[@name="mobile"]')
    textbox_alternateMobile_xpath = (By.XPATH, '//input[@name="alternative_mobile"]')
    textbox_email_xpath = (By.XPATH, '//input[@id="email"]')
    textbox_address_xpath = (By.XPATH, '//input[@id="address"]')
    textbox_landmark_xpath = (By.XPATH, '//input[@id="landmark"]')
    textbox_pincode_xpath = (By.XPATH, '//input[@name="pin_code"]')
    textbox_city_xpath = (By.XPATH, '//input[@id="city"]')
    textbox_state_xpath = (By.XPATH, '//input[@id="state"]')
    textbox_doctor_xpath = (By.XPATH, '//input[@id="doctor"]')
    textbox_medicineName_xpath = (By.XPATH, '//input[@id="medicineName"]')
    select_medicine_xpath = (By.XPATH, '(//p[@class="chakra-text css-a7dbc6"])')
    button_submit_xpath = (By.XPATH, '//button[@type="submit"]')
    button_file_upload_xpath = (By.XPATH, '//input[@type="file"]')
    order_partner_id = (By.ID, 'order_partner')
    partner_callhealth_xpath = (By.XPATH, '//*[@id="order_partner"]/option[3]')


    """Constructors of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_text_exist(self):
        return self.is_visible(self.dashboard_text_xpath)

    def is_menu_btn_exist(self):
        menu_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/button')
        return menu_btn.is_enabled()

    def click_menu_btn(self):
        self.do_click(self.button_menu_xpath)

    def is_place_order_btn_exist(self):
        place_orderbtn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/button')
        return place_orderbtn.is_enabled()

    def is_column_partner_order_exists(self):
        return self.get_element_text(self.partner_text_xpath)

    def is_column_customer_name_exists(self):
        return self.get_element_text(self.customer_name_text_xpath)

    def is_column_order_status_exists(self):
        return self.get_element_text(self.order_status_text_xpath)

    def is_column_payment_status_exists(self):
        return self.get_element_text(self.payment_status_text_xpath)

    def is_column_city_exists(self):
        return self.get_element_text(self.city_text_xpath)

    def is_column_action_exists(self):
        return self.get_element_text(self.action_text_xpath)

    def is_column_notes_exists(self):
        return self.get_element_text(self.notes_text_xpath)

    def click_orders_btn(self):
        self.do_click(self.button_orders_xpath)
        return self.is_visible(self.dashboard_text_xpath)

    def click_logout_btn(self):
        self.do_click(self.button_logout_xpath)

    def click_cancel_btn(self):
        self.do_click(self.button_cancel_xpath)
        return self.is_visible(self.button_stay_xpath)

    def click_cancel_yes(self):
        self.do_click(self.button_cancel_xpath)
        self.do_click(self.button_yes_xpath)
        return self.is_visible(self.button_submit_cancel_xpath)

    def click_cancel_reason(self):
        self.do_click(self.button_cancel_xpath)
        self.do_click(self.button_yes_xpath)
        reason = self.driver.find_element_by_xpath('//select[@id="reason"]')
        reason.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
        self.do_click(self.button_submit_cancel_xpath)
        self.accept_alert()
        return self.is_visible(self.button_submit_cancel_xpath)

    def download_orders(self):
        self.do_click(self.button_export_xpath)
        return self.is_visible(self.button_export_xpath)

    def place_order(self, partnerorderid, name, mobile, alternatemobile, email, address, landmark, pincode, city, state, doctor, medicine):
        self.do_click(self.button_placeorder_xpath)
        time.sleep(2)
        self.do_click(self.partner_callhealth_xpath)
        time.sleep(1)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath('//input[@id="partner_order_id"]'))
        action.click()
        action.perform()
        time.sleep(1)
        self.do_send_keys(self.textbox_partnerorderid_xpath, partnerorderid)
        self.do_send_keys(self.text_box_Name_xpath, name)
        self.do_send_keys(self.textbox_mobile_xpath, mobile)
        self.do_send_keys(self.textbox_alternateMobile_xpath, alternatemobile)
        self.do_send_keys(self.textbox_email_xpath, email)
        self.do_send_keys(self.textbox_address_xpath, address)
        self.do_send_keys(self.textbox_landmark_xpath, landmark)
        self.do_send_keys(self.textbox_pincode_xpath, pincode)
        self.do_send_keys(self.textbox_city_xpath, city)
        self.do_send_keys(self.textbox_state_xpath, state)
        time.sleep(1)
        self.do_send_keys(self.textbox_doctor_xpath, doctor)
        self.do_send_keys(self.textbox_medicineName_xpath, medicine)
        time.sleep(2)
        self.do_click(self.select_medicine_xpath)
        self.do_click(self.button_submit_xpath)
        return self.is_visible(self.button_placeorder_xpath)

    def navigate_to_manage(self):
        self.do_click(self.button_menu_xpath)
        self.do_click(self.button_manage_orders_xpath)
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_by_offset(100, 100)
        action.click()
        action.perform()
        time.sleep(2)

    def manage_orders(self):
        self.do_click(self.button_menu_xpath)
        self.do_click(self.button_manage_orders_xpath)
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_by_offset(200, 200)
        action.click()
        action.perform()
        time.sleep(2)
        return self.pending_tab_Id

    def assign_order(self):
        self.do_click(self.button_menu_xpath)
        self.do_click(self.button_manage_orders_xpath)
        time.sleep(1)
        action = ActionChains(self.driver)
        action.move_by_offset(200, 200)
        action.click()
        action.perform()
        self.do_click(self.button_orderid_xpath)
        time.sleep(2)
        self.do_click_js(self.checkbox_xpath)
        time.sleep(1)
        return self.is_visible(self.checkbox_xpath)

    def assigned_tab(self):
        self.do_click(self.button_assign_xpath)
        time.sleep(2)
        return self.is_visible(self.button_assign_xpath)





