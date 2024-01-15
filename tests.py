from unittest import TestCase

import selenium.webdriver.chrome.webdriver

from web_scraping import *


class TestRecruitmentBot(TestCase):

	def test_initialize_driver(self):
		cd_path = r"C:\chromedriver-win64\chromedriver.exe"
		driver = initialize_driver(cd_path)
		self.assertNotEqual(driver, None)
		self.assertIsInstance(driver, selenium.webdriver.chrome.webdriver.WebDriver)
