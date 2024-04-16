import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
driver.maximize_window()

# radio Buttons

radio_btn = driver.find_elements(By.XPATH, "//input[@class='radioButton']")

for radio in radio_btn:
    time.sleep(1)
    radio.click()


#dropdown
drop = driver.find_element(By.ID, "dropdown-class-example")
select = Select(drop)
select.select_by_visible_text("Option1")

suggest =  driver.find_element(By.ID, "autocomplete")
suggest.send_keys("In")

contrynames = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")

for contrie in contrynames:
    print(contrie.text)
    if contrie.text == "India":
        contrie.click()
        break
print(driver.title)
#checkboxes

checkboxes_names = driver.find_elements(By.XPATH, "//div[@id='checkbox-example']/fieldset/label")
input_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check, input in zip(checkboxes_names,input_checkboxes):
    print(check.text)
    if check.text == "Option2":
        input.click()

#windows
# window = driver.find_element(By.ID, "openwindow")
# window.click()
# window = driver.window_handles
# print(window)
# win = window[1]
# driver.switch_to.window(win)
# print(driver.title)


driver.find_element(By.ID, "opentab").click()

opentab = driver.window_handles
print(opentab)
win2 = opentab[1]
driver.switch_to.window(win2)
print(driver.title)
driver.switch_to.window(opentab[0])
print(driver.title)

#alert

driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

driver.find_element(By.ID, "name").send_keys("Piyush")
time.sleep(2)
driver.find_element(By.ID, "confirmbtn").click()
print(alert.text)
alert.accept()

driver.execute_script("window.scrollBy(0,1300)")
#mouse hover

mouse = driver.find_element(By.ID, "mousehover")

action = ActionChains(driver)
action.move_to_element(mouse).perform()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[4]/div/fieldset/div/div/a[1]").click()
time.sleep(2)
# driver.find_element(By.LINK_TEXT, "Reload").click()
driver.execute_script("window.scrollBy(0,1400)")

driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT, "Practice").click()
print(driver.title)
driver.switch_to.default_content()
driver.execute_script("window.scrollBy(1400,0)")
# driver.find_element(By.XPATH,"/html/body/header/div/a/button").click()

driver.save_screenshot("piyush.png")

waiting = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "opentab")))
waiting.click()
time.sleep(5)
driver.quit()