from selenium.webdriver.common.by import By
from pageObjects import LoginPage


def login(driver, username, password):
    driver.implicitly_wait(5)
    driver.find_element(By.ID(LoginPage.login_screen['textbox_username_id'])).clear()
    driver.find_element(By.ID(LoginPage.login_screen['textbox_password_id'])).clear()
    driver.find_element(By.ID(LoginPage.login_screen['textbox_username_id'])).send_keys(username)
    driver.find_element(By.ID(LoginPage.login_screen['textbox_password_id'])).send_keys(password)
    driver.find_element(By.ID(LoginPage.login_screen['button_login_id'])).click()



