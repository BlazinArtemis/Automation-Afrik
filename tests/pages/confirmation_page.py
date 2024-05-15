from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ConfirmationPage:

    def __init__(self, driver, unittests):
        self.driver = driver
        self.order_div= (By.CSS_SELECTOR, ".col-sm-9.col-sm-offset-1")
        self.confirm_text = (By.TAG_NAME, "b")
        self.test = unittests

    def open_page(self, url):
        self.driver.get(url)

    def confirm_order(self,confirm_ord):
        confirm_section = self.driver.find_element(*    self.order_div)
        text = confirm_section.find_element(*  self.confirm_text).text
        self.test.assertTrue(text == confirm_ord, f"Expected confirmation text: '{confirm_ord}', but got: '{text}'")
        print("Order Confirmed!")  # Print message after successful assertion

