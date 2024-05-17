from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.checkout= (By.CSS_SELECTOR, ".btn.btn-default.check_out") # Check out button
        self.comment = (By.TAG_NAME, "textarea") # Comment text area

    # Open a url
    def open_page(self, url):
        self.driver.get(url)

    # Wait for Checkout Button and Click
    def check_out(self):
        checkout_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout))
        checkout_click.click()


    #   Write a comment -- Takes the Comment
    def write_comment(self,comment):
        self.driver.find_element(*  self.comment).send_keys(comment)

