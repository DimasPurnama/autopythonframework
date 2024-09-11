from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from os import path
import framework.services.MyConfig
import framework.services.ScreenshotService

def main():
#   initial var class
  MyConfig = framework.services.MyConfig
  ScreenshotService = framework.services.ScreenshotService
  
  ScreenshotService.create_folder_if_not_exist(MyConfig.strPathReport)

#   print(MyConfig.strPathDatatable)
    # print("asd")

if __name__ == "__main__": 
  main()

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.XPATH, "//input[@id='id-search-field']")
# elem.clear()
# elem.send_keys("pycon")

# driver.save_screenshot('D:/SS_001_001.png')

# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()