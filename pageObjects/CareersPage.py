from selenium.webdriver.common.by import By


class CareersPage:

    locations_section = (By.XPATH, "//section[@id='career-our-location']")
    life_section = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")
    teams_section = (By.XPATH, "//h3[contains(text(),'Find your calling')]")
    all_teams = (By.CSS_SELECTOR, "a[class*='loadmore']")
    quality_assurance = (By.XPATH, "//h3[text()='Quality Assurance']")
    navigation_bar = (By.XPATH, "//div[@id='navbarNavDropdown']")

    def __init__(self, driver):
        self.driver = driver

    def get_locations_section(self):
        return self.driver.find_element(*CareersPage.locations_section)

    def get_life_section(self):
        return self.driver.find_element(*CareersPage.life_section)

    def get_teams_section(self):
        return self.driver.find_element(*CareersPage.teams_section)

    def get_all_teams(self):
        btn = self.driver.find_element(*CareersPage.all_teams)
        return self.driver.execute_script("arguments[0].click();", btn)

    def get_quality_assurance_jobs(self):
        btn = self.driver.find_element(*CareersPage.quality_assurance)
        return self.driver.execute_script("arguments[0].click();", btn)
