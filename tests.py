from unittest import TestCase
from unittest.mock import patch
import selenium.webdriver.chrome.webdriver
from web_scraping import *


class TestRecruitmentBot(TestCase):

	def test_initialize_driver(self):
		cd_path = r"C:\chromedriver-win64\chromedriver.exe"
		driver = initialize_driver(cd_path)

		self.assertNotEqual(driver, None)
		self.assertIsInstance(driver, selenium.webdriver.chrome.webdriver.WebDriver)

	@patch('time.sleep', return_value=None)
	@patch('selenium.webdriver.remote.webdriver.WebDriver.execute_script')
	def test_scroll_down(self, mock_execute_script, mock_sleep):

		mock_execute_script(
			"window.scrollTo(0, document.body.scrollHeight);")
		mock_sleep(3)

		mock_execute_script.assert_called_once_with(
			"window.scrollTo(0, document.body.scrollHeight);")
		mock_sleep.assert_called_once_with(3)
