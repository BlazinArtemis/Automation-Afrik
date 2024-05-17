from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.paragraph = (By.TAG_NAME, "p") # Locator for Paragraphs
        self.cart = (By.TAG_NAME, "a")   #  Add to Cart Button
        self.continue_shopping = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")    # Continue Shopping Button
        self.cart_button = (By.CSS_SELECTOR, "a[href='/view_cart']")   # View Cart

    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # FInd all Paragraphs 
    def find_paragraphs(self):
        return self.driver.find_elements(*  self.paragraph)

    # Find a Particular Product ( takes product name) - Search all Paragraphs to Locate a Product
    def find_product(self, element, product_name):
        for paragraph in element:
            # print(paragraph.text.strip())
            if (paragraph.text.strip() == product_name):
                parent_div = paragraph.find_element(By.XPATH, "..")
                return parent_div
            else: 
                continue
    
    # Click Cart Page
    def click_cart_page(self):
        self.driver.find_element(*  self.cart_button).click()
    
    #   Add to Cart and then Continue Shopping
    def add_to_cart(self,element): 
        element.find_element(*    self.cart).click()
        # print(self.driver.find_element(*  self.continue_shopping).tag_name)
        continue_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_shopping))
        continue_click.click()

    
