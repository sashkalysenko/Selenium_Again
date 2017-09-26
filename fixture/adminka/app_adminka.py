from selenium import webdriver
from fixture.adminka.pages import HomePage
from fixture.adminka.pages import CountryPage


class AdminApplication:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.home_page = HomePage(self)
        self.country_page = CountryPage(self)

    def destroy(self):
        self.logout()
        self.wd.quit()

    def open_login_page(self):
        driver = self.wd
        driver.get("http://localhost/litecart/admin")

    def login_as(self, username, password):
        driver = self.wd
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("login").click()

    def logout(self):
        driver = self.wd
        logout_btn = driver.find_elements_by_css_selector("i.fa.fa-sign-out.fa-lg")
        if len(logout_btn) > 0:
            logout_btn[0].click()
        else:
            raise LookupError("Logout button has not found")
