# import all required frameworks
import unittest
import time
import string
import csv

from selenium.webdriver.common.touch_actions import TouchActions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        driver.get("https://github.com/search/advanced")

        # assertion to confirm if title has python keyword in it
        #self.assertIn("Github", driver.title)

        # locate element using name
        time.sleep(2)
        driver.find_element_by_link_text("Sign in").click()
        time.sleep(2)
        driver.find_element_by_id("login_field").send_keys("Zubair2019")
        driver.find_element_by_id("password").send_keys("Malla@2019")
        time.sleep(0)
        driver.find_element_by_name("commit").click()
        time.sleep(3)
        elem = driver.find_element_by_id("search_language")
        # send data
        elem.send_keys("Python")
        time.sleep(0)
        driver.find_element_by_id("search_stars").send_keys("40..999")
        driver.find_element_by_id("search_size").send_keys("<5000")
        elem1 = driver.find_element_by_id("search_path")
        elem1.send_keys("/tests")
        time.sleep(0)
        elem1.send_keys(Keys.RETURN)
        time.sleep(0)

        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Best match']").click()
        time.sleep(0)
        driver.find_element_by_xpath("//span[text()='Most stars']").click()
        time.sleep(2)


        for i in range(0,99):
            get_list(driver)
            driver.find_element_by_link_text("Next").click()
            print("Value of i is =",i)
            time.sleep(5)
        print("Length of DIRECTORY is", directory)
        f = open('/Users/mac/Documents/repos.csv', 'a')
        for item in directory:
            f.write(item+'\n')  # Give your csv text here.
        ## Python will convert \n to os.linesep
        f.close()
        assert "No results found." in driver.page_source

    # cleanup method called after every test performed
    # def tearDown(self):
    #     self.driver.close()



# execute the script
if __name__ == "__main__":
    unittest.main()
