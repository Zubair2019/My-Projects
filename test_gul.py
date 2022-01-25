# import all required frameworks
import unittest
import time
import string
import csv
import urllib

from selenium.webdriver.common.touch_actions import TouchActions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options    

chrome_options = Options()
directory = []
sufix = 'github.com/'
# inherit TestCase Class and create a new test class
def get_list(driver):

    # lst = driver.find_elements_by_class_name("v-align-middle")
    lst = driver.find_elements_by_xpath("//*[@class='v-align-middle']")
    lnks = driver.find_elements_by_xpath("//*[@class='Link--muted']")

    print("Number of Anchors are:", len(lnks))
    for (name,star) in zip(lst,lnks):
        if sufix + name.text not in directory:
            # print(int(float(star.get_attribute('text').strip().replace("k", "")) * 1000))
            directory.append(sufix+name.text+ ',' + str(int(float(star.get_attribute('text').strip().replace("k",""))*1000)))

class TestGithub(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_search_in_python_org(self):

        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.maximize_window()
        chrome_options.add_argument("--start-fullscreen")
        driver.get("https://thispersondoesnotexist.com/")
        
        dir = "/Users/mac/Documents/gul/"
        
        
        for i in range(0,4):
            time.sleep(2)
            with open(dir + str(i) +'.png', 'wb') as file:
                file.write(driver.find_element_by_id('face').screenshot_as_png)
            driver.refresh()
        assert 1+1 == 2

# execute the script
if __name__ == "__main__":
    unittest.main()