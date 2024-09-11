from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import framework.services.MyConfig

def main():
  MyConfig = framework.services.MyConfig
  print(MyConfig.strPathDatatable)
    # print("asd")
  # do something

if __name__ == "__main__": 
  main()

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()