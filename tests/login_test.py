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
    chromedriver_path = '/home/tester/Downloads/chromedriver-linux64/chromedriver'

    # Create a Service object (recommended)
    service = Service(executable_path=chromedriver_path)
    service.start()

    # Set up Chrome options (headless mode)
    chrome_options = Options()
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Create the WebDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Return the driver
    return driver

def sort_and_print(price):
    sorted_prices = dict(sorted(price.items(), key=lambda item: item[1])) #(O(n log n))

    #Loop through all the sorted prices and print them
    for prices in sorted_prices:      
        print(prices + " - " + str(sorted_prices[prices])) 

def test(driver):
    #Initialize the Page Classes
    login_page = LoginPage(driver)
    landing_page = LandingPage(driver)

    # Open the site and Login
    login_page.open_page("https://www.automationexercise.com/")
    login_page.click_login_page()
    login_page.enter_username("qat@mailinator.com")
    login_page.enter_password("123456")

    #Did this to combat the ads before but no longer needed cause of headless
    try:
        login_page.click_login()
        
    except:
        login_page.click_login()
    
    time.sleep(10)
    
    # Loop through Featured Products and Put them in a Dictionary
    product_info = {}
    featured_items = landing_page.featured_items_div() # Get the Div of Featured Products
    products = landing_page.find_products(featured_items) # Get the Product div for each item

    for product in products: # Loop through each product
        product_image_wrapper_div = landing_page.product_image_wrapper_divs(product)
        single_products_div = landing_page.single_products_divs(product_image_wrapper_div)
        product_info_div = landing_page.product_info_divs(single_products_div)
        label = landing_page.product_label_text(product_info_div) # Get Label 
        price_element = landing_page.find_price(product_info_div) # Get Price
        price = landing_page.convert_price_to_float(price_element) # Remove "Rs." and convert to float
        # print(price)
        product_info[label] = price # Add to Dictionary
    sort_and_print(product_info) # Call the sort and print function
    add_to_cart(driver)# Call the function to start the add to cart flow

def add_to_cart(driver): #function to add the items to the cart
    #Initialize the Page Classes
    landing_page = LandingPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    landing_page.find_and_click_category("WOMEN","Tops") # Go to the Women's Category

    product_page.add_to_cart(product_page.find_product(product_page.find_paragraphs(),"Fancy Green Top")) # Add the top to the Cart
    product_page.add_to_cart(product_page.find_product(product_page.find_paragraphs(),"Summer White Top")) # Add the top to the Cart
    product_page.click_cart_page() # Go to the Cart Page

    cart_page.check_out() # Go to check out page

    # On Checkout Page, Write Comment and Checkout to Payment Page
    checkout_page.write_comment("Order placed.")
    checkout_page.check_out()

    pay_for_item(driver) # Call the pay for item function

def pay_for_item(driver):

    payment_page = PaymentPage(driver)
    payment_page.pay_for_item("Test Card","410000000000", "123", "01", "1900") # Fill in the card details
    payment_page.click_pay() #Click Pay
    confirm_order_final(driver) # Call the Last Function to Confirm the order was placed


def confirm_order_final(driver):
    confirmation_page = ConfirmationPage(driver,unittest.TestCase) # Initialize the COnfirmation Page with the UNittest Class
    confirmation_page.confirm_order("ORDER PLACED!") # Assert that the order was placed

test(driver()) # Call Start Function

