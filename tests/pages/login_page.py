from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CSS_SELECTOR, "a[href='/login']")
        self.username_textbox= (By.CSS_SELECTOR, "input[placeholder='Email Address']")
        self.password_textbox = (By.CSS_SELECTOR, "input[placeholder='Password']")
        self.login = (By.XPATH, "//button[normalize-space()='Login']")
        self.dismiss_button = (By.ID, "dismiss-button")


    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_page(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        login_click.click()
        

    def click_dismiss_button(self):
        self.driver.find_element(*  self.dismiss_button).click()
    
    def click_login(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login))
        login_click.click()
