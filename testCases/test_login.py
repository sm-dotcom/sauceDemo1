import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login

class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_homePageTitle(self, setup):
        self.driver = setup
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_url = self.driver.current_url
        if act_url == "https://www.saucedemo.com/inventory.html":
            assert True
        else:
            assert False

    def test_loginWithoutUsername(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False


    def test_loginWithoutPassword(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False
