import time

from pageObjects.HomePage import HomePage
from pageObjects.CareersPage import CareersPage
from pageObjects.QACareersPage import QACareersPage
from pageObjects.OpenPositionsPage import OpenPositionsPage
from pageObjects.LeverPage import LeverPage
from utilities.BaseClass import BaseClass


class TestProject(BaseClass):
    def test_e2e(self):
        home_page = HomePage(self.driver)
        assert home_page.get_page_title() == home_page.expected_title
        menu_captions = home_page.get_header_menu_items()
        for caption in menu_captions:
            if caption.text == "More":
                caption.click()
        home_page.get_career_item().click()

        careers_page = CareersPage(self.driver)
        self.verify_presence(careers_page.navigation_bar)
        locations_section = careers_page.get_locations_section()
        assert locations_section.is_displayed()
        life_section = careers_page.get_life_section()
        assert life_section.is_displayed()
        teams_section = careers_page.get_teams_section()
        assert teams_section.is_displayed()

        self.verify_if_clickable(careers_page.all_teams)
        careers_page.get_all_teams()
        self.verify_presence(careers_page.quality_assurance)
        careers_page.get_quality_assurance_jobs()

        qa_careers_page = QACareersPage(self.driver)
        self.verify_presence(qa_careers_page.qa_jobs)
        qa_careers_page.get_qa_jobs().click()

        open_positions_page = OpenPositionsPage(self.driver)
        self.verify_presence(open_positions_page.job_list)
        open_positions_page.get_location_dropdown().click()
        open_positions_page.get_istanbul_turkey_filter().click()
    
        open_positions_page.get_department_dropdown().click()
        open_positions_page.get_qa_filter().click()
        job_list = open_positions_page.get_job_list()
        assert job_list.is_displayed()

        positions = open_positions_page.get_filtered_positions()
        for position in positions:
            assert "Quality Assurance" in open_positions_page.get_position_title(position).text
            assert "Quality Assurance" in open_positions_page.get_position_department(position).text
            assert "Istanbul, Turkey" in open_positions_page.get_position_location(position).text
            apply_now_btn = open_positions_page.get_position_apply_now(position)
            assert apply_now_btn.is_enabled()
    
        self.move_to_element(open_positions_page.get_filtered_position())
        self.verify_presence(open_positions_page.apply_now_button)
        open_positions_page.apply_to_position()

        lever_page = LeverPage(self.driver)
        lever_page.get_lever_window()
        self.verify_presence(lever_page.apply_button)
        assert "lever" in lever_page.get_current_url()
