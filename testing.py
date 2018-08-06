import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox(executable_path='/home/launchpad/Desktop/python/geckodriver')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("http://www.google.com/")
	
	def test_search_by_text(self):
		self.search_field = self.driver.find_element_by_name('q')
		self.search_field.send_keys("Selenium Webdriver interview quesions")
		self.search_field.submit()
		lists = self.driver.find_elements_by_class_name("r")
		number= len(lists)
		self.assertEqual(number,11)
	
	def test_search_by_name(self):
        # get the search textbox
	        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
       		self.search_field.send_keys("Python class")
        	self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        	list_new = self.driver.find_elements_by_class_name("r")
        	self.assertEqual(10, len(list_new))
	
	def tearDown(self):
        # close the browser window
	        self.driver.quit()
unittest.main()
