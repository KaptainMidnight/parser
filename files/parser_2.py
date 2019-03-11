import csv

import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

BASE_URL = input("Enter site URL: ")


# Получаем html разметку главной страницы
def get_html(url):
    # req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    # response = urlopen(req).read()
    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        try:
            if driver.find_element_by_class_name("DnHhI").is_displayed():
                button = driver.find_element_by_class_name("_2bexo")
                button.click()
        except:
            continue
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    return driver.page_source


# Парсим ссылки на объявления
def parse_url_city(html):
    global user_data
    global users
    users = []
    soup = bs(html, 'lxml')
    main_div = soup.find_all('div', attrs={'class': '_328WR'})
    for i in main_div:
        try:
            a = i.find('a', attrs={'class': 'MBUbs'})['href']
            ls = f'https://m.avito.ru{a}'
            links = {
                'href': ls
            }
            headers = {
                "accept": "*/*",
                "user-agent": "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
            }
            for i in links:
                session = requests.Session()
                response = session.get(links[i], headers=headers)
                if response.status_code == 200:
                    soup = bs(response.content, 'lxml')
                    contact_div = soup.find_all('div', {'class': '_37BGw'})
                    for lp in contact_div:
                        try:
                            name = lp.find('span', {'class': 'ZvfUX'}).text
                            phone = lp.find('a', {'class': '_2MOUQ'}).get('href')
                            if "tel:" in phone:
                                phone.split()
                                phone = phone[4::1]
                            user_data = {
                                "name": name,
                                "phone": phone
                            }
                            users.append(user_data)
                            print(len(users))
                        except:
                            pass
                else:
                    print("Error")
        except:
            pass
    return users


def file_save(data):
    with open("base.csv", "w") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Номер"))
        for i in data:
            wrtr.writerow((i['name'], i['phone']))


parse_url = parse_url_city(get_html(BASE_URL))
file_save(parse_url)
