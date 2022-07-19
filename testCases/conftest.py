from selenium import webdriver
import pytest
from os.path import abspath
import sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
chromepath = os.path.join(os.path.sep, ROOT_DIR, 'drivers' + os.sep)



@pytest.fixture()
def setup():
    chromepath = abspath("C:\\Users\\Saad\\PycharmProjects\\sauceDemo1\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(chromepath)
    # driver.get('https://www.saucedemo.com/')
    return driver
