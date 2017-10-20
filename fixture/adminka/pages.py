class BasePage:

    def __init__(self, app):
        self.driver = app.wd


class HomePage(BasePage):

    def amount_apps(self):
        return len(self.driver.find_elements_by_css_selector("div#box-apps-menu-wrapper li"))

    def click_app_by_index(self, index):
        self.driver.find_element_by_css_selector("div#box-apps-menu-wrapper li#app-:nth-child({0})".format(index)).\
            click()

    def get_children_names(self):
        """returns children names (property text) from selected app"""
        return self.driver.find_elements_by_css_selector("li#app-.selected li")

    def is_header_exists(self):
        if len(self.driver.find_elements_by_css_selector("h1")) == 0:
            return False
        else:
            return True

    def click_children_by_index(self, index):
        self.driver.find_element_by_css_selector("li#app-.selected li:nth-child({0})".format(index)).click()

    def open_countries(self):
        self.driver.find_element_by_css_selector("#box-apps-menu li:nth-child(3)").click()

    def open_catalog(self):
        self.driver.find_element_by_css_selector("#box-apps-menu li:nth-child(2)").click()

    def open_geozones(self):
        self.driver.find_element_by_css_selector("#box-apps-menu li:nth-child(6)").click()


class CountryPage(BasePage):

    def get_countries(self):
        # get index of column Name
        column_index = self.get_index_of_column("[name=countries_form]", 'Name')
        countries_list = []
        for element in self.driver.find_elements_by_css_selector("[name=countries_form] tr.row"):
            countries_list.append(element.find_element_by_css_selector(
                'td:nth-child({0})'.format(column_index)).text)
        return countries_list

    def get_index_of_column(self, table_locator, column_name):
        column_index = 0
        for element in self.driver.find_elements_by_css_selector("{0} tr.header th".format(table_locator)):
            column_index += 1
            if element.text == column_name:
                break
        return column_index

    def amount_tzs_by_index(self, country_index):
        column_index = self.get_index_of_column("[name=countries_form]", 'Zones')
        return int(self.driver.find_element_by_css_selector(
            "[name=countries_form] tr.row:nth-child({0}) td:nth-child({1})".format(
                country_index + 1, column_index)).text)

    def get_timezones_for_country(self, country_index):
        self.driver.find_element_by_css_selector("[name=countries_form] tr.row:nth-child({0}) .fa-pencil".
                                                 format(country_index + 1)).click()
        column_index = self.get_index_of_column("#table-zones", 'Name')
        timezones_list = []
        for element in self.driver.find_elements_by_css_selector("#table-zones tr.row"):
            timezones_list.append(element.find_element_by_css_selector(
                'td:nth-child({0})'.format(column_index)).text)
        self.driver.find_element_by_css_selector("#box-apps-menu li:nth-child(3)").click()
        return timezones_list

    def add_new_country(self):
        self.driver.find_element_by_css_selector("a.button").click()

    def links_in_separate_window(self):
        return self.driver.find_elements_by_css_selector("a[target='_blank'] i[class='fa fa-external-link']")
