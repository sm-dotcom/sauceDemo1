import time
from selenium import webdriver
import os


class Driver:
    def __init__(self):
        Driver.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        time.sleep(2)