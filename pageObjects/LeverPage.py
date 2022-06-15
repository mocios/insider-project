from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage


class LeverPage(BasePage):

    apply_button = (By.XPATH, "//a[text()='Apply for this job']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_lever_window(self):
        lever_window = self.driver.window_handles[1]
        return self.driver.switch_to.window(lever_window)