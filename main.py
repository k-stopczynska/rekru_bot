import csv
from linkedin_search import pass_query_params, scrape_google_results
from web_scraping import dispose_cookie_banner, initialize_driver, change_page


def define_search_parameters():

    """
    define_search_parameters function is a place where you can pass skillset,
    location and current role for your search
    :return:
    skillset(List(str)): skills keywords
    location(str): location of a candidate according to LI
    role(str): the role of a candidate
    """

    skillset = ['typescript', 'react', '3D']
    skillset = [_.strip().lower().replace(" ", "-") for _ in
                skillset]

    location = 'Warsaw'
    location = location.strip().lower().replace(" ", "-")

    role = 'developer'
    role = role.strip().lower().replace(" ", "-")

    return skillset, location, role


def save_to_csv(data, csv_filename='users.csv'):

    """
    save_to_csv function writes data to a csv file for future use
    :param data: (List(tuple(str), str)) data List to write into csv file
    :param csv_filename: (str) filename of a file that is used to save results
    """

    with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['lp', 'first name', 'last name', 'linkedin url']
        csv_writer = csv.DictWriter(csv_file, fieldnames)
        lp = 0

        if csv_file.tell() == 0:
            csv_writer.writeheader()

        for entry in data:
            lp += 1
            (first_name, last_name), linkedin_url = entry

            csv_writer.writerow(
                {'lp': lp, 'first name': first_name, 'last name': last_name,
                 'linkedin url': linkedin_url})

    print(f'Data has been written to {csv_filename}')


def search_in_google(params, driver):

    """
    search_in_google function will open google tab, take search params,
    and type it in, waits for results, scroll down or change the page if
    possible for as many times as specified in change_page fn
    :param params: (List(str))list of strings representing skills, role,
    and desired location of candidate
    :param driver: webdriver instance
    """

    driver.get('https://www.google.com')
    dispose_cookie_banner(driver)
    pass_query_params(driver, params)
    change_page(driver)
    users = scrape_google_results(driver)
    save_to_csv(users, csv_filename='users.csv')


def run():

    """
    run function is script executable that performs all scripts in order
    """

    skillset, location, role = define_search_parameters()
    google_params = skillset + [role, location]

    cd_path = r"C:\chromedriver-win64\chromedriver.exe"
    driver = initialize_driver(cd_path)

    try:
        search_in_google(google_params, driver)
    finally:
        driver.quit()


if __name__ == '__main__':
    run()
