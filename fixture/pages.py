from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, app):
        self.driver = app.wd

    def open_home_page(self):
        self.driver.find_element_by_css_selector("#logotype-wrapper").click()

    def open_cart(self):
        self.driver.find_element_by_css_selector("#cart").click()

    def amount_products_in_cart(self):
        return int(self.driver.find_element_by_css_selector("#cart .quantity").text)


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
        h_values["regular_price_style"] = element.find_element_by_css_selector(".regular-price").get_attribute(
            "tagName")
        h_values["campaign_price_style"] = element.find_element_by_css_selector(".campaign-price").get_attribute(
            "tagName")
        return h_values

    def open_product_page(self, category, index):
        element = self.driver.find_element_by_css_selector("div#box-{0}.box li:nth-child({1})".format(category, index))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

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
        p_values = {
            "product_name": self.driver.find_element_by_css_selector("h1").text,
            "regular_price": self.driver.find_element_by_css_selector(".regular-price").text,
            "campaign_price": self.driver.find_element_by_css_selector(".campaign-price").text,
            "regular_price_style": self.driver.find_element_by_css_selector(".regular-price").get_attribute("tagName"),
            "campaign_price_style": self.driver.find_element_by_css_selector(".campaign-price").get_attribute(
                "tagName")
        }
        return p_values

    def select_product_size(self, size=None):
        if self.driver.find_elements_by_css_selector("[name='options[Size]']"):
            drop_down_size = Select(self.driver.find_elements_by_css_selector("[name='options[Size]']")[0])
            drop_down_size.select_by_index(self.get_index_size(size))

    def get_index_size(self, size):
        if size == 'small':
            return 1
        elif size == 'medium':
            return 2
        elif size == 'large':
            return 3
        else:
            print('Size is incorrect - {0} doesn\'t equal to small, medium or large'.format(size))
            return

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 3)
        products_in_cart = self.amount_products_in_cart()
        self.driver.find_element_by_css_selector("[name='add_cart_product']").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart .quantity"),
                                                    str(products_in_cart + 1)))


class CartPage(BasePage):
    def amount_products_in_table(self):
        amount = 0
        for element in self.driver.find_elements_by_css_selector("table[class='dataTable rounded-corners'] tr"):
            if element.find_elements_by_css_selector("td.item"):
                amount += 1
        return amount

    def remove_first_product(self):
        if self.driver.find_elements_by_css_selector("ul.shortcuts"):
            self.driver.find_elements_by_css_selector("ul.shortcuts li a")[0].click()
        product_in_table = self.driver.find_element_by_css_selector("table[class='dataTable rounded-corners'] tr td")
        self.driver.find_element_by_css_selector("[name='remove_cart_item']").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.staleness_of(product_in_table))
