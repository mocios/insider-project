import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption("-B", "--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()

    action = ActionChains(driver)
    wait = WebDriverWait(driver, 10)
    driver.get("https://useinsider.com/")
    driver.maximize_window()
    acc_cookies = driver.find_element(By.ID, "wt-cli-accept-all-btn")
    if acc_cookies.is_displayed():
        acc_cookies.click()
    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.action = action
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if report.failed and not xfail:
            file_name = report.nodeid.replace("::", "_")+".png"
            capture_screenshot(file_name)
        report.extra = extra


def capture_screenshot(name):
    driver.get_screenshot_as_file(name)
