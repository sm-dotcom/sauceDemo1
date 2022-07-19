from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_menu_id = "react-burger-menu-btn"
    link_logout_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickLogout(self):
        self.driver.find_element(By.ID, self.button_menu_id).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.link_logout_id).click()













# login_screen = {
#     "textbox_username_id": "user-name",
#     "textbox_password_id": "password",
#     "button_login_id": "login-button",
#     "button_menu_id": "react-burger-menu-btn",
#     "link_logout_id": "logout_sidebar_link"
# }
