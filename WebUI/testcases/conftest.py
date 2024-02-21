'''this is a centralized fixture which executes before running actual test case'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

'''request instance comes by default when we declare a fixture'''
@pytest.fixture(scope="class")
def setup(request):
    # will pull the value from 'browser_name' which you passed at run time
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":

        service_obj = Service()
        '''invoking chrome browser'''
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser_name == "edge":

        service_obj = Service()
        driver=webdriver.Edge(service=service_obj)
        driver.maximize_window()
    '''assigning local driver to class driver so which ever class uses this fixture can use this driver'''
    request.cls.driver=driver
    yield
    driver.close()

''' Pytest HTML Report '''
'''it is hook for adding Environment info to HTML Report'''
def pytest_configure(config):
    config._metadata['Project Name'] = 'Front End Automation Testing-SDET Assignment'
    config._metadata['Module Name'] = 'Users-Editors'
    config._metadata['Tester'] = 'Amulya Reddimalla'

'''it is hook to delete or modify Environment info to HTML report'''
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)

