class BasePage:

    def __init__(self, app):
        self.driver = app.wd


class HomePage(BasePage):

    def get_product_info(self, category, index):
        """        
        categories:
        'most-popular'
        'campaigns'
        'latest-products'
        """
        h_values = {}
        element = self.driver.find_element_by_css_selector("div#box-{0}.box li:nth-child({1})".format(category, index))
        h_values["product_name"] = element.find_element_by_css_selector(".name").text
        h_values["regular_price"] = element.find_element_by_css_selector(".regular-price").text
        h_values["campaign_price"] = element.find_element_by_css_selector(".campaign-price").text
        h_values["regular_price_style"] = element.find_element_by_css_selector(".regular-price").get_attribute("tagName")
        h_values["campaign_price_style"] = element.find_element_by_css_selector(".campaign-price").get_attribute("tagName")
        return h_values

    def open_product_page(self, category, index):
        self.driver.find_element_by_css_selector("div#box-{0}.box li:nth-child({1})".format(category, index)).click()

    def is_logged_in(self):
        if len(self.driver.find_elements_by_css_selector("[name=login]")) > 0:
            return False
        return True

    def logout(self):
        self.driver.find_element_by_css_selector('a[href$="logout"]').click()

    def create_new_customer(self, first_name, last_name, address_1, postcode, city, email, password, phone):
        if self.is_logged_in():
            self.logout()
        self.driver.find_element_by_css_selector("[name=login_form] a").click()
        self.driver.find_element_by_css_selector("[name=firstname]").send_keys(first_name)
        self.driver.find_element_by_css_selector("[name=lastname]").send_keys(last_name)
        self.driver.find_element_by_css_selector("[name=address1]").send_keys(address_1)
        self.driver.find_element_by_css_selector("[name=postcode]").send_keys(postcode)
        self.driver.find_element_by_css_selector("[name=city]").send_keys(city)
        self.driver.find_element_by_css_selector("[name=email]").send_keys(email)
        self.driver.find_element_by_css_selector("[name=password]").send_keys(password)
        self.driver.find_element_by_css_selector("[name=confirmed_password]").send_keys(password)
        self.driver.find_element_by_css_selector("[name=phone]").send_keys(phone)
        self.driver.find_element_by_css_selector("[name=create_account]").click()

    def login_as(self, email, password):
        if self.is_logged_in():
            self.logout()
        self.driver.find_element_by_css_selector("[name=email]").send_keys(email)
        self.driver.find_element_by_css_selector("[name=password]").send_keys(password)
        self.driver.find_element_by_css_selector("[name=login]").click()



class ProductPage(BasePage):

    def get_product_info(self):
        p_values = {}
        p_values["product_name"] = self.driver.find_element_by_css_selector("h1").text
        p_values["regular_price"] = self.driver.find_element_by_css_selector(".regular-price").text
        p_values["campaign_price"] = self.driver.find_element_by_css_selector(".campaign-price").text
        p_values["regular_price_style"] = self.driver.find_element_by_css_selector(".regular-price").\
            get_attribute("tagName")
        p_values["campaign_price_style"] = self.driver.find_element_by_css_selector(".campaign-price").get_attribute(
            "tagName")
        return p_values
