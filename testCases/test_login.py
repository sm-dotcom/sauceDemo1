import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage



class Test_Login:
    baseURL = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    invalidUsername = "someone@email.com"
    invalidPassword = "12345"


    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_loginWithoutUsername(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
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
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.username)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_loginWithInvalidPassword(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.invalidPassword)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_loginWithInvalidUsername(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.invalidUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swag Labs":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_url = self.driver.current_url
        if act_url == "https://www.saucedemo.com/inventory.html":
            assert True
        else:
            assert False

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickLogout()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            assert False


































### Rough


# from utilities.DriverClass import Driver
# Driver()
# driver = Driver.driver

# # Should be placed in the env file
# baseURL = "https://www.saucedemo.com/"
# username = "standard_user"
# password = "secret_sauce"




# def test_homePageTitle():
#     driver.get(baseURL)
#     act_title = driver.title
#     driver.close()
#     if act_title == "Swag Labs":
#         assert True
#     else:
#         assert False
#
# def test_loginWithoutUsername():
#     driver.get(baseURL)
#     driver.find_element(By.ID, LoginPage.login_screen['textbox_username_id']).clear()
#     driver.find_element(By.ID, LoginPage.login_screen['textbox_password_id']).send_keys(password)