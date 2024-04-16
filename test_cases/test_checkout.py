import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from test_cases.test_login import TestLogin

class TestCheckout():

    def test_checkout_page(self,setup):
        self.driver = setup
        self.obj = TestLogin()
        self.obj.test_shopping(self.driver)
        print("passs")
