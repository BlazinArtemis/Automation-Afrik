from selenium.webdriver.common.by import By

class LandingPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.products = (By.CLASS_NAME, "col-sm-4") #Products Div
        self.product_label= (By.TAG_NAME, "p") # Product Label
        self.price = (By.TAG_NAME, "h2")    # Price

        #Locators to get to the Featured Products 
        self.product_info_div = (By.CSS_SELECTOR, ".productinfo.text-center") 
        self.single_products_div = (By.CLASS_NAME, "single-products") 
        self.product_image_wrapper_div = (By.CLASS_NAME, "product-image-wrapper")
        
        self.dismiss_button = (By.ID, "dismiss-button") # Dismiss Button ( Attempt at fixing ads)
        self.featured_items = (By.CLASS_NAME, "features_items") #Featured Items DIv
        self.category_check = (By.CLASS_NAME, "panel-title") # Page Category Label
        self.category_div = (By.TAG_NAME, "a")  # Category Div
        self.category_items = (By.TAG_NAME, "li")   # Category Items List
        self.category = (By.ID, "Women")    # Women Category

    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # FInd Profuct Div
    def find_products(self,element):
        return element.find_elements(*  self.products)
    
    # FInd Product Label
    def product_label_text(self,element):
        return element.find_element(*  self.product_label).text 
    
    # Retrieve Price
    def find_price(self,element):
        return element.find_element(*  self.price)

#Too complex - breakdown - -    Go to Women's Category
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
        
        
    #Convert Price to FLoat (takes the Retrieve Price Element/Function)
    def convert_price_to_float(self,element):
        # print(element.text.replace("Rs. ", "").strip(" "))
        return float(element.text.replace("Rs. ", "").strip()) 

    # Get Featured Items Div
    def featured_items_div(self):
        return self.driver.find_element(*  self.featured_items)
    
    # Get Product Info Divs
    def product_info_divs(self,element):
        return element.find_element(*  self.product_info_div)
    
    # Single Product Divs
    def single_products_divs(self,element):
        return element.find_element(*  self.single_products_div)

    # Get Product Image Wraper Div
    def product_image_wrapper_divs(self,element):
        return element.find_element(*  self.product_image_wrapper_div)

    # Click Dismiss Button
    def click_dismiss_button(self):
        self.driver.find_element(*  self.dismiss_button).click()


    
