import selenium
from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os


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


def login():
    driver.get("https://www.linkedin.com/home")
    sleep(5)
    driver.find_element(By.ID, "session_key").send_keys(
        os.getenv('LINKEDIN_LOGIN'))
    driver.find_element(By.ID, "session_password").send_keys(
        os.getenv('LINKEDIN_PASSWORD'))
    sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button").click()


def define_search_parameters():
    skillset = ['data', 'architect', 'python']
    skillset = [_.strip().lower().replace(" ","-") for _ in skillset]

    location = 'Warsaw'
    location = location.strip().lower().replace(" ", "-")

    role = 'data analyst'
    role = role.strip().lower().replace(" ","-")

    return skillset, location, role


def search_in_google(params):
    driver.get('https://www.google.com')

    driver.find_element(By.ID, "L2AGLb").click()

    search_query = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, 'q')))

    search_query.send_keys('site:linkedin.com/in/ AND "data" AND "architect"')

    search_query.send_keys(Keys.ENTER)
    sleep(5)

    linkedin_users_urls_list = driver.find_elements(
         By.XPATH, '//div[@class="MjjYud"]/div/div/div/div/div/span/a[@href]')
    # UWckNb

    print([users.text for users in linkedin_users_urls_list])


def run():
    # login()
    # skillset, location, role = define_search_parameters()
    search_in_google('sth')



if __name__ == '__main__':
    run()
