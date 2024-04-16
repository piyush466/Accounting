from selenium import webdriver
from selenium.webdriver.common.by import By


class Proceed_Checkout:

    xpath_procced = '//*[@id="page-34"]/div/div[1]/div/div/div/a'
    place_order_id = "place_order"

    def __init__(self,driver):
        self.driver = driver

    def proceed_btn(self):
        self.driver.find_element(By.XPATH, self.xpath_procced).click()

    def order_place_btn(self):
        self.driver.find_element(By.ID, self.place_order_id).click()
