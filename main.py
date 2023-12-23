import selenium
from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


"""
You need chromedriver for testing, here is the list of downloads for Chrome 
version above 115: https://googlechromelabs.github.io/chrome-for-testing/
And here is the list of downloads for 115 and older: 
https://chromedriver.chromium.org/downloads
Remember to put it in PATH executable or add it to you environmental paths
I you don't know the version of your Chrome, type in you browser: chrome://version
"""

cd_path = r"C:\chromedriver-win64\chromedriver.exe"
service = Service(cd_path)
driver = wb.Chrome(service=service)


def run():
    print("hello bot")


if __name__ == '__main__':
    run()


