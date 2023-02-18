from selenium import webdriver
from selenium.webdriver.common.by import By

# Find count of wiki pages from wiki main page
chrome_driver_path ="edgedriver_win64/msedgedriver.exe"
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.ChromiumEdge(options=option,executable_path=chrome_driver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

wiki_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a').text
print(wiki_count.replace(",",""))


driver.quit()

