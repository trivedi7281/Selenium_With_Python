import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.....")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.....")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser Value to Setup method
    return request.config.getopion("--browser")


########## Pytest HTML Report ############
def pytest_configure(config):
    config._metadata['Project Name'] = 'Selenium_with_Python'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Preeti'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
