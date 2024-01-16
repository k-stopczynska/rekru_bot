from unittest import TestCase
from unittest.mock import patch, MagicMock
import selenium.webdriver.chrome.webdriver
from web_scraping import *
from linkedin_search import *


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

	@patch('time.sleep', return_value=None)
	@patch('selenium.webdriver.remote.webdriver.WebDriver.find_element')
	def test_change_page_success(self, mock_find_elem, mock_sleep):
		mock_find_elem(By.CLASS_NAME, 'kQdGHd')
		button = MagicMock()
		mock_find_elem.return_value = button
		button.click()
		mock_sleep(5)

		mock_find_elem.assert_called_with(By.CLASS_NAME, 'kQdGHd')
		button.click.assert_called_once()
		mock_sleep.assert_called_once_with(5)

	@patch('selenium.webdriver.remote.webdriver.WebDriver.find_element')
	def test_dispose_cookie_banner_success(self, mock_find_elem):
		button = MagicMock()
		mock_find_elem.return_value = button
		button.click()

		button.click.assert_called_once()

	@patch('selenium.webdriver.support.wait.WebDriverWait.until')
	def test_pass_query_params(self, mock_wait):
		params = ['typescript', 'react', '3D', 'warsaw', 'developer']
		mock_wait(ec.visibility_of_element_located((By.NAME, 'q')))
		search_query = MagicMock()
		mock_wait.return_value = search_query
		query_string = " AND ".join(params)
		search_query.send_keys(f'site:linkedin.com/in/ {query_string}')

		mock_wait.assert_called_once()
		search_query.send_keys.assert_called_with(
			f'site:linkedin.com/in/ typescript AND react AND 3D AND warsaw '
			f'AND developer')

	@patch('selenium.webdriver.remote.webdriver.WebDriver.find_elements')
	def test_scrape_google_results(self, mock_find_elems):
		mock_find_elems(
			By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a[@href]')

		mock_find_elems.assert_called_with(
			By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a[@href]')

		mock_find_elems(
			By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a/h3')

		mock_find_elems.assert_called_with(
			By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a/h3')






