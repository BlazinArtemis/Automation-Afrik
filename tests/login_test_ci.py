# Version for CI/ CD 

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.landing_page import LandingPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.confirmation_page import ConfirmationPage
import unittest

def driver():
    chromedriver_path = '/home/runner/work/Automation-Afrik/Automation-Afrik/chromedriver'

    # Create a Service object (recommended)
    service = Service(executable_path=chromedriver_path)
    service.start()

    # Set up Chrome options (headless mode)
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # Create the WebDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Return the driver
    return driver

def sort_and_print(price):
    sorted_prices = dict(sorted(price.items(), key=lambda item: item[1])) #(O(n log n))
    for prices in sorted_prices:
        print(prices + " - " + str(sorted_prices[prices])) 

def test(driver):
    login_page = LoginPage(driver)
    landing_page = LandingPage(driver)
    login_page.open_page("https://www.automationexercise.com/")
    login_page.click_login_page()
    login_page.enter_username("qat@mailinator.com")
    login_page.enter_password("123456")
    try:
        login_page.click_login()
        
    except:
        login_page.click_login()
    
    time.sleep(30)
    

    product_info = {}
    featured_items = landing_page.featured_items_div()
    products = landing_page.find_products(featured_items)

    for product in products:
        product_image_wrapper_div = landing_page.product_image_wrapper_divs(product)
        single_products_div = landing_page.single_products_divs(product_image_wrapper_div)
        product_info_div = landing_page.product_info_divs(single_products_div)
        label = landing_page.product_label_text(product_info_div)
        price_element = landing_page.find_price(product_info_div)
        price = landing_page.convert_price_to_float(price_element) # Remove "Rs." and convert to float
        # print(price)
        product_info[label] = price
    sort_and_print(product_info)
    add_to_cart(driver)

def add_to_cart(driver):
    landing_page = LandingPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    landing_page.find_and_click_category("WOMEN","Tops")

    product_page.add_to_cart(product_page.find_product(product_page.find_paragraphs(),"Fancy Green Top"))
    product_page.add_to_cart(product_page.find_product(product_page.find_paragraphs(),"Summer White Top"))
    product_page.click_cart_page()

    cart_page.check_out()

    # On Checkout Page, Write Comment and Checkout to Payment Page
    checkout_page.write_comment("Order placed.")
    checkout_page.check_out()

    pay_for_item(driver)

def pay_for_item(driver):
    payment_page = PaymentPage(driver)
    payment_page.pay_for_item("Test Card","410000000000", "123", "01", "1900")
    payment_page.click_pay()
    confirm_order_final(driver)


def confirm_order_final(driver):
    confirmation_page = ConfirmationPage(driver,unittest.TestCase)
    confirmation_page.confirm_order("ORDER PLACED!")

test(driver())

