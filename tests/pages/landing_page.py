from selenium.webdriver.common.by import By

class LandingPage:

    def __init__(self, driver):
        self.driver = driver
        self.products = (By.CLASS_NAME, "col-sm-4")
        self.product_label= (By.TAG_NAME, "p")
        self.price = (By.TAG_NAME, "h2")
        self.product_info_div = (By.CSS_SELECTOR, ".productinfo.text-center")
        self.single_products_div = (By.CLASS_NAME, "single-products")
        self.product_image_wrapper_div = (By.CLASS_NAME, "product-image-wrapper")
        self.dismiss_button = (By.ID, "dismiss-button")
        self.featured_items = (By.CLASS_NAME, "features_items")
        self.category_check = (By.CLASS_NAME, "panel-title")
        self.category_div = (By.TAG_NAME, "a")
        self.category_items = (By.TAG_NAME, "li")
        self.category = (By.ID, "Women")

    def open_page(self, url):
        self.driver.get(url)

    def find_products(self,element):
        return element.find_elements(*  self.products)
    
    def product_label_text(self,element):
        return element.find_element(*  self.product_label).text 
        
    def find_price(self,element):
        return element.find_element(*  self.price)

#Too complex - breakdown
    def find_and_click_category(self,line_item,category_item):
        categories_check = self.driver.find_element(*  self.category_check) #implement item function
        categories = self.driver.find_element(* self.category)
        items = categories.find_elements(*   self.category_div)
        if (categories_check.text == line_item):
            # print(items)
            for item in items:
                if (item.get_attribute("textContent").strip() == category_item):
                    href = item.get_attribute("href")
                    self.driver.get(href)
                    break
                else: 
                    # print("Item Not Found")
                    continue
        else: 
            print("Wrong Category Found")
        
        

    def convert_price_to_float(self,element):
        # print(element.text.replace("Rs. ", "").strip(" "))
        return float(element.text.replace("Rs. ", "").strip()) 

    def featured_items_div(self):
        return self.driver.find_element(*  self.featured_items)
    
    def product_info_divs(self,element):
        return element.find_element(*  self.product_info_div)
    
    def single_products_divs(self,element):
        return element.find_element(*  self.single_products_div)

    def product_image_wrapper_divs(self,element):
        return element.find_element(*  self.product_image_wrapper_div)

    def click_dismiss_button(self):
        self.driver.find_element(*  self.dismiss_button).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_page(self):
        self.driver.find_element(*  self.login_button).click()
    
    def click_login(self):
        self.driver.find_element(*  self.login).click()