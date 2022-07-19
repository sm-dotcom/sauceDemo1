from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    # driver.get('https://www.saucedemo.com/')
    return driver