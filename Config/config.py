import random
n = random.randint(900, 10000)
class TestData:
    CHROME_EXECUTABLE_PATH = "/Users/teamstreamz/Downloads/chromedriver"

    BASE_URL = "https://testing.d3eymc78cqte40.amplifyapp.com/login"
    USER_NAME = "TestUser123"
    PASSWORD = "123456"
    LOGIN_PAGE_TITLE = "Order Dashboard"
    COLUMN_PARTNER_TITLE = "Partner Order ID"
    COLUMN_CUSTOMER_TITLE = "Customer Name"
    COLUMN_ORDER_TITLE = "Order Status"
    COLUMN_STATUS_TITLE = "Payment status"
    COLUMN_CITY_TITLE = "City"
    COLUMN_ACTION_TITLE = "Actions"
    COLUMN_NOTES_TITLE = "Notes"

    """Place order values"""

    PARTNER_ORDER_ID = str(n)
    NAME = "Test user 145"
    MOBILE = "9090909090"
    ALTERNATE_MOBILE = "8989898989"
    EMAIL = "testing@ts.net"
    ADDRESS = "Test address 1234 skddkgndg g"
    LANDMARK = "Test landmark"
    PINCODE = "560078"
    CITY = "BENGALURU"
    STATE = "KARNATAKA"
    DOCTOR = "TEST DOCTOR"
    MEDICINE_NAME = "dolo"

