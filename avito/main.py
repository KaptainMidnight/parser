# -*- charset: utf-8 -*-

import csv
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = input("Enter site: ")  # Получаем от пользователя ссылку на сайт


# Получаем html разметку главной страницы
def get_html(b_url):
    chromedriver = "/Users/applemac/Downloads/chromedriver"  # Подключаем драйвер для браузера
    driver = webdriver.Chrome(chromedriver)  # Открываем браузер
    driver.get(b_url)  # Переходим по ссылке на сайт
    SCROLL_PAUSE_TIME = 3  # Задержка на прокрутку сайта

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:  # Прокрутка сайта вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        try:
            if driver.find_element_by_class_name("DnHhI").is_displayed():
                driver.find_element_by_class_name("_2bexo").click()
        except:
            continue
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
    driver.quit()
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
            city = i.find("div", attrs={"class": "_20Ixl"}).text
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
                                "phone": phone,
                                "city": city
                            }
                            users.append(user_data)
                            print(len(users))
                        except:
                            pass
                else:
                    print("Error")
        except:
            continue
    return users


def file_save(data):
    with open("animals.csv", "a") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Номер", "Город"))
        for i in data:
            wrtr.writerow((i['name'], i['phone'], i['city']))


parse_url = parse_url_city(get_html(url))
file_save(parse_url)
