from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Form filling using selenium
chrome_driver_path ="edgedriver_win64/msedgedriver.exe"
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.ChromiumEdge(options=option,executable_path=chrome_driver_path)
driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')

username = driver.find_element(By.NAME, value='username')
username.click()
username.send_keys("Fuck You")

password = driver.find_element(By.NAME,value='password')
password.click()
password.send_keys("AgainFuckYou")

comments = driver.find_element(By.NAME,value='comments')
comments.clear()
comments.click()
comments.send_keys("100000timesAgainFuckYou")

submit = driver.find_element(By.CLASS_NAME, value='styled-click-button')
submit.submit()



