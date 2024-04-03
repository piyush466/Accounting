from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    username_name = "username"
    password_name = "password"
    login_btn_name = "login"

    def __init__(self,driver):
        self.driver= driver

    def set_username(self,username):
        self.driver.find_element(By.NAME, self.username_name).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def login(self):
        self.driver.find_element(By.NAME, self.login_btn_name).click()