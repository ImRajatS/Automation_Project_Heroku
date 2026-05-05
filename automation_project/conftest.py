import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def init_driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()



    