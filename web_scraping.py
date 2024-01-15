from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def initialize_driver(cd_path):

    """
    You need chromedriver for testing, here is the list of downloads for Chrome
    version above 115: https://googlechromelabs.github.io/chrome-for-testing/
    And here is the list of downloads for 115 and older:
    https://chromedriver.chromium.org/downloads
    Remember to put it in PATH executable or add it to you environmental paths
    If you don't know the version of your Chrome,
    type in you browser: chrome://version
    :returns webdriver instance
    """

    service = Service(cd_path)
    options = Options()
    options.add_argument("--disable-redirects")
    options.add_argument("--headless")
    driver = wb.Chrome(service=service, options=options)
    return driver


def scroll_down(driver):

    """
    scroll_down function executes javascript script for scrolling down on pages
    that are using lazy loading, and waits for results before next scroll
    for 3 seconds
    """

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)


def change_page(driver):

    """
    change_page function is calling scroll down function for lazy loaded
    results, and changes page pages_num times if "next button" is found
    :params driver: webdriver instance
    :excepts: any Exception raised if page couldn't be scrolled further or next
    button is not found
    """

    pages_num = 1

    for page in range(pages_num):
        scroll_num = 8

        for scroll in range(scroll_num):
            try:
                scroll_down(driver)

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


def dispose_cookie_banner(driver):

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
