from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path ="edgedriver_win64/msedgedriver.exe"
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.ChromiumEdge(options=option,executable_path=chrome_driver_path)
driver.get('https://www.python.org/')
# price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(price.get_attribute("textContent").replace(".",""))

time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu time')

event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .menu  a')

python_events = {}

for i in range(len(time)):
    python_events[i]={
        "time": time[i].text,
        "Event": event[i].text,
    }

print(python_events)

driver.quit()











