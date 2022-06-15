from selenium.webdriver.common.by import By


class OpenPositionsPage:

    job_list = (By.ID, "jobs-list")
    location_dropdown = (By.ID, "select2-filter-by-location-container")
    department_dropdown = (By.ID, "select2-filter-by-department-container")
    istanbul_turkey_filter = (By.XPATH, "//li[contains(text(),'Istanbul, Turkey')]")
    qa_filter = (By.XPATH, "//li[contains(text(),'Quality Assurance')]")
    filtered_positions = (By.XPATH, "//div[@class='position-list-item-wrapper bg-light']")
    position_title = (By.XPATH, "p")
    position_department = (By.XPATH, "span")
    position_location = (By.XPATH, "div")
    position_apply = (By.XPATH, "a")
    apply_now_button = (By.XPATH, "//a[text()='Apply Now']")

    def __init__(self, driver):
        self.driver = driver

    def get_job_list(self):
        return self.driver.find_element(*OpenPositionsPage.job_list)

    def get_location_dropdown(self):
        return self.driver.find_element(*OpenPositionsPage.location_dropdown)

    def get_department_dropdown(self):
        return self.driver.find_element(*OpenPositionsPage.department_dropdown)

    def get_istanbul_turkey_filter(self):
        return self.driver.find_element(*OpenPositionsPage.istanbul_turkey_filter)

    def get_qa_filter(self):
        return self.driver.find_element(*OpenPositionsPage.qa_filter)

    def get_filtered_positions(self):
        return self.get_job_list().find_elements(*OpenPositionsPage.filtered_positions)

    def get_filtered_position(self):
        return self.get_job_list().find_element(*OpenPositionsPage.filtered_positions)

    def get_position_title(self, position):
        return position.find_element(*OpenPositionsPage.position_title)

    def get_position_department(self, position):
        return position.find_element(*OpenPositionsPage.position_department)

    def get_position_location(self, position):
        return position.find_element(*OpenPositionsPage.position_location)

    def get_position_apply_now(self, position):
        return position.find_element(*OpenPositionsPage.position_apply)

    def apply_to_position(self):
        apply_now_btn = self.driver.find_element(*OpenPositionsPage.apply_now_button)
        return self.driver.execute_script("arguments[0].click();", apply_now_btn)
