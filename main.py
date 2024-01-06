from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from dotenv import load_dotenv
import os

"""
This is loading environmental variables for loading credentials to LI.
In root directory create .env file with two variables named: LINKEDIN_LOGIN and
LINKEDIN_PASSWORD, and pass your LI credentials as strings.
"""

load_dotenv()


"""
You need chromedriver for testing, here is the list of downloads for Chrome
version above 115: https://googlechromelabs.github.io/chrome-for-testing/
And here is the list of downloads for 115 and older:
https://chromedriver.chromium.org/downloads
Remember to put it in PATH executable or add it to you environmental paths
I you don't know the version of your Chrome,
type in you browser: chrome://version
"""

cd_path = r"C:\chromedriver-win64\chromedriver.exe"
service = Service(cd_path)
driver = wb.Chrome(service=service)
chrome_options = wb.ChromeOptions()
chrome_options.add_argument("--headless")


def login():

    """
    login function will go to LI login page and pass your credentials from
    .env file
    """

    driver.get("https://www.linkedin.com/home")
    sleep(5)
    driver.find_element(By.ID, "session_key").send_keys(
        os.getenv('LINKEDIN_LOGIN'))
    driver.find_element(By.ID, "session_password").send_keys(
        os.getenv('LINKEDIN_PASSWORD'))
    sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button").click()


def define_search_parameters():

    """
    define_search_parameters function is a place where you can pass skillset,
    location and current role for your search
    :return:
    skillset(List(str)): skills keywords
    location(str): location of a candidate according to LI
    role(str): the role of a candidate
    """

    skillset = ['data', 'architect', 'python']
    skillset = [_.strip().lower().replace(" ", "-") for _ in skillset]

    location = 'Warsaw'
    location = location.strip().lower().replace(" ", "-")

    role = 'data analyst'
    role = role.strip().lower().replace(" ", "-")

    return skillset, location, role


def scroll_down():

    """
    scroll_down function executes javascript script for scrolling down on pages
    that are using lazy loading, and waits for results before next scroll
    for 3 seconds
    """

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)


def dispose_cookie_banner():

    """
    dispose_cookie_banner function searches for a button to consent to all
    cookies and clicks it
    :excepts: any errors raised if no button with this ID is found, and prints
    message to inform user
    """

    try:
        driver.find_element(By.ID, "L2AGLb").click()
    except Exception as e:
        print("No cookie banner this time", e)
        pass


def pass_query_params(params):

    """
    pass_query_params function is looking for an input field to pass params as
    a boolean string and starts searching process by clicking enter key
    :param params: (List(str))list of strings representing skills, role,
    and desired location of candidate
    """

    search_query = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, 'q')))

    query_string = " AND ".join(params)

    search_query.send_keys(f'site:linkedin.com/in/ {query_string}')

    search_query.send_keys(Keys.ENTER)
    sleep(5)


def change_page():

    """
    change_page function is calling scroll down function for lazy loaded results,
    and changes page pages_num times if "next button" is found
    :excepts: any Exception raised if page couldn't be scrolled further or next
    button is not found
    """

    pages_num = 1

    for page in range(pages_num):
        scroll_num = 6

        for scroll in range(scroll_num):
            try:
                scroll_down()

            except Exception as e:
                print("couldn't scroll down anymore, I will try to click load "
                      "more results", e)
                pass

        try:
            next_button = driver.find_element(By.CLASS_NAME, 'kQdGHd')
            next_button.click()
            sleep(5)

        except Exception as e:
            print("No next button on this page", e)


def scrape_google_results():

    """
    scrape_google_results function finds links to candidates' profiles aligned
    with search params, and returns them as a List
    :return: List(str) users' links list
    """

    linkedin_users_urls_list = driver.find_elements(
        By.XPATH,
        '//div[@class="MjjYud"]/div/div/div/div/div/span/a[@href]')

    return [user.get_attribute('href') for user in linkedin_users_urls_list]


def search_in_google(params):

    """
    search_in_google function will open google tab, take search params,
    and type it in, waits for results, scroll down or change the page if
    possible for as many times as specified in change_page fn
    :param params: (List(str))list of strings representing skills, role,
    and desired location of candidate
    :return: a list of linked in links to profiles of candidates
    """

    driver.get('https://www.google.com')

    dispose_cookie_banner()

    pass_query_params(params)

    change_page()

    return scrape_google_results()


def scrap_users_links(links):
    for link in links:
        driver.get(link)
        login()
        sleep(1)

    driver.close()


def run():

    """
    run function is script executable that performs all scripts in order
    """

    skillset, location, role = define_search_parameters()
    google_params = skillset + [role, location]
    links = search_in_google(google_params)
    scrap_users_links(links)


if __name__ == '__main__':
    run()
