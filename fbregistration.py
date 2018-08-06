from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class facebook_registration(unittest.TestCase):
	
    	def setUp(self):
        	self.driver = webdriver.Firefox(executable_path='/home/launchpad/Desktop/python/geckodriver')

    	def test_fb_registration(self):

        	driver = self.driver 
		driver.get("https://www.facebook.com/") 
        	fname = driver.find_element_by_name('firstname')
        	fname.send_keys('shefali')
        	lname = driver.find_element_by_name('lastname')
        	lname.send_keys('yaduvanshi')
        	email = driver.find_element_by_name('reg_email__')
        	email.send_keys('hello@gmail.com')
        	pwd = driver.find_element_by_name('reg_passwd__')
        	pwd.send_keys('asdfgh')

unittest.main()
