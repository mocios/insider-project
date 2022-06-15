from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class HomePage(BasePage):

    header_menu = (By.XPATH, "//a[@id='mega-menu-1']/span")
    career_item = (By.XPATH, "//h5[text()='Careers']")
    expected_title = "Insider personalization engine for seamless customer experiences"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_header_menu_items(self):
        return self.driver.find_elements(*HomePage.header_menu)

    def get_career_item(self):
        return self.driver.find_element(*HomePage.career_item)
