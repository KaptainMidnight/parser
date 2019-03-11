from selenium import webdriver as wd
import time
from bs4 import BeautifulSoup as bs
import requests


def selenium_get_href(b_url):
    global name
    global phone
    global links
    global user_data
    global urls
    global name
    global phone
    global city
    global users
    global block
    global href
    urls = []
    users = []
    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = wd.Chrome(chromedriver)
    driver.get(b_url)
    # Все что будем брать из главного меню
    city = driver.find_element_by_class_name("_20Ixl")  # Ищем город в ссылках

    SCROLL_PAUSE_TIME = 0.5

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            if driver.find_element_by_class_name("DnHhI").is_displayed():
                button = driver.find_element_by_class_name("_2bexo").click()
                time.sleep(SCROLL_PAUSE_TIME)
                href = driver.find_elements_by_class_name("MBUbs")  # Ищем ссылки на объявления
                for j in href:
                    links = {
                        "href": j.get_attribute("href")
                    }
                    if links not in urls:
                        urls.append(links)
                        print(len(urls))
        except:
            continue


def parse_avito(href):
    for data in href:
        session = requests.Session()
        response = session.get(data["href"])
        if response.status_code == 200:
            soup = bs(response.content, "lxml")
            contact_div = soup.find_all("div", attrs={"class": "_3U_HU"})
            for contact in contact_div:
                try:
                    name = contact.find("span", attrs={"class": "ZvfUX"}).text
                    phone = contact.find("span", attrs={"class": "_2MOUQ"})['href']
                    print(name, phone)
                except:
                    continue
        else:
            print("ERROR")


html = selenium_get_href("https://m.avito.ru/rossiya/dlya_biznesa")
parse_avito(html)
