from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModule.LoginPage import LoginPage
from Utilities.loggerfile import LogGen

class TestLogin:
    log = LogGen.logger()
    username = "piyushdravyakar48@gmail.com"
    password = "Piyush@123"

    def test_logins(self,setup):
        self.log.info("**********Exicution Started*********")
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.log.info("Your Username is: %s -", self.username)
        self.lp.set_password(self.password)
        self.log.info("Your password is: %s -", self.password)
        self.lp.login()
        self.log.info("Click on Login button")
        self.emailcheck = self.driver.find_element(By.XPATH,"//p/strong").text
        if self.emailcheck == "piyushdravyakar4":
            print("test case Passed")
            self.log.info("************Email verified************")

        else:
            print("Test case failed")
            self.log.error("Test case is failed")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\pythonProject1\Screenshots\login.png")

        self.log.info("**********Exicution Succesful*********")