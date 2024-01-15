
# Recruitment bot

A bot for searching recruitment candidates with certain skillset, roles and location.


## Features

- user can pass search params
- bot automatically will pass those to Google in order to find Linkedin profiles that match params
- after scraping bot will save results into csv file for future use



## Tech Stack

**Server:** Python, Selenium, time, csv


## Installation and running locally

To install and run this bot locally you need at least Python 3.11

1. First clone repository:
```bash
git clone https://github.com/k-stopczynska/rekru_bot.git
cd rekru_bot
```

2. Activate pipenv shell and install dependencies:
```bash
pipenv shell
pipenv install
```

3. Get your chromedriver:
You need chromedriver, here is the list of downloads for Chrome
version above 115: https://googlechromelabs.github.io/chrome-for-testing/
And here is the list of downloads for 115 and older:
https://chromedriver.chromium.org/downloads
Remember to put it in PATH executable or add it to you environmental paths
If you don't know the version of your Chrome,
type in you browser: chrome://version

4. Run:
Run main.py file
    
## Authors

- [@k-stopczynska](https://www.github.com/k-stopczynska)

