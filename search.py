from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class search(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/launchpad/Desktop/python/geckodriver')
    
    def test_getnnfo(self):
        driver = self.driver
        driver.get('http://www.google.com/')
        driver.implicitly_wait(30)
        element = driver.find_element_by_xpath('//*[@id="lst-ib"]')
        element.clear()
        element.send_keys('python')
        element.send_keys(Keys.RETURN)
        self.assertIn('Python',driver.title)
        assert "No results found." not in driver.page_source
    def tearDown(self):
        self.driver.close()

unittest.main()
