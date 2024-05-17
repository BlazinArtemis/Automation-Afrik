from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.pay= (By.CSS_SELECTOR, ".form-control.btn.btn-primary.submit-button")  # Pay Button
        self.card_name = (By.NAME, "name_on_card")  # Name Field
        self.card_number = (By.NAME, "card_number") # Card Number Field
        self.cvc = (By.NAME, "cvc") # CVC Field
        self.month = (By.NAME, "expiry_month")  # Expiry Month Field
        self.year = (By.NAME, "expiry_year")    # Expiry Year Field

    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # Fill in Card Details
    def pay_for_item(self,card_names,card_numbers,cvcs,months,years):
        card_name_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_name))
        card_name_element.send_keys(card_names)
        self.driver.find_element(*  self.card_name).send_keys(card_names)
        self.driver.find_element(*  self.card_number).send_keys(card_numbers)
        self.driver.find_element(*  self.cvc).send_keys(cvcs)
        self.driver.find_element(*  self.month).send_keys(months)
        self.driver.find_element(*  self.year).send_keys(years)
    
    #   CLick Pay Button
    def click_pay(self):
        self.driver.find_element(*  self.pay).click()

