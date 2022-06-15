import pytest
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_presence(self, element):
        self.wait.until(EC.presence_of_element_located(element))

    def verify_if_clickable(self, element):
        self.wait.until(EC.element_to_be_clickable(element))

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()
