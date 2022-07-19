from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver = webdriver.Chrome(r"C:\Users\Saad\PycharmProjects\sauceDemo1\drivers\chromedriver.exe")
    # driver.get('https://www.saucedemo.com/')
    return driver