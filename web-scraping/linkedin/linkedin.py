from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# LinkedIn project
chrome_driver_path ="edgedriver_win64/msedgedriver.exe"
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.ChromiumEdge(options=option,executable_path=chrome_driver_path)
driver.get('https://www.linkedin.com/login/')

username = driver.find_element(By.ID, value='username')
username.send_keys('oulkarshubhu@gmail.com')

password = driver.find_element(By.ID, value='password')
password.send_keys('xyz')

submit_button = driver.find_element(By.CSS_SELECTOR, value='div .login__form_action_container ')
submit_button.click()

time.sleep(2)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3481097745&f_PP=105556991&f_T=25169&f_WT=2&keywords=python%20developer&sortBy=R')

