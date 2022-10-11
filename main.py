from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True


driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
# driver.get("https://www.youtube.com")

driver.get("https://www.youtube.com/watch?v=qPYqmNnEPC0")
print("SELENUMM:::",driver)
print('VIDEO:::',video)
hrefs = [video.get_attribute('href') for video in driver.find_elements_by_id("thumbnail")]

for href in hrefs:
    print(href)