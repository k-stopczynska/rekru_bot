from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


def pass_query_params(driver, params):

    """
    pass_query_params function is looking for an input field to pass params as
    a boolean string and starts searching process by clicking enter key
    :param params: (List(str))list of strings representing skills, role,
    and desired location of candidate
    :param driver: webdriver instance
    """

    search_query = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, 'q')))

    query_string = " AND ".join(params)

    search_query.send_keys(f'site:linkedin.com/in/ {query_string}')

    search_query.send_keys(Keys.ENTER)
    sleep(5)


def scrape_google_results(driver):

    """
    scrape_google_results function finds links to candidates' profiles and
    their names aligned with search params
    :params driver: webdriver instance
    :return: (List(str)) users' links list
    """

    linkedin_users_urls = driver.find_elements(
        By.XPATH,
        '//div[@class="MjjYud"]/div/div/div/div/div/span/a[@href]')

    parsed_urls = [user.get_attribute('href') for user in linkedin_users_urls]

    linkedin_users_names = driver.find_elements(
        By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a/h3')

    parsed_names = [[name.text.split(' ')[0], name.text.split(' ')[1]] for name
                    in linkedin_users_names]

    users_data = zip(parsed_names, parsed_urls)
    return [data for data in users_data]
