import os
import pytest
from selenium import webdriver

URL = "https://rahulshettyacademy.com/angularpractice"
CHROME_DRIVER = os.environ.get("CHROME_DRIVER_PATH")
GECKO_DRIVER = os.environ.get("GECKO_DRIVER_PATH")



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path=GECKO_DRIVER)
    elif browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
    driver.get(URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

