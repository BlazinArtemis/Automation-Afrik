from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CSS_SELECTOR, "a[href='/login']")   #Login Link
        self.username_textbox= (By.CSS_SELECTOR, "input[placeholder='Email Address']")  #   Username 
        self.password_textbox = (By.CSS_SELECTOR, "input[placeholder='Password']")  # Password
        self.login = (By.XPATH, "//button[normalize-space()='Login']")  # Login Button
        self.dismiss_button = (By.ID, "dismiss-button") # Dismiss Button

    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # Enter Username (Takes Username)
    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    #   Enter Password (Takes Password)
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    # Open Login Page
    def click_login_page(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        login_click.click()
        
    # Click Dismiss Button
    def click_dismiss_button(self):
        self.driver.find_element(*  self.dismiss_button).click()
    
    # Click Login Button
    def click_login(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login))
        login_click.click()
