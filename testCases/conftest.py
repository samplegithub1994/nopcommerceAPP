from selenium import webdriver
import pytest
# we create conftest file for duplication of test cases
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lauching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Lauching firefox browser")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption('--broser')   # This will gives value from hooks

@pytest.fixture()
def browser(request):     # This will return the browser value to setup method
    return request.config.getoption("--browser")


# pytest html report
