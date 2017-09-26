from selenium import webdriver
from fixture.pages import HomePage
from fixture.pages import ProductPage


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.home_page = HomePage(self)
        self.product_page = ProductPage(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        self.wd.get("http://localhost/litecart")
