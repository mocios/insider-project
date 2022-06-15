from selenium.webdriver.common.by import By


class QACareersPage:

    qa_jobs = (By.XPATH, "//a[text()='See all QA jobs']")

    def __init__(self, driver):
        self.driver = driver

    def get_qa_jobs(self):
        return self.driver.find_element(*QACareersPage.qa_jobs)
