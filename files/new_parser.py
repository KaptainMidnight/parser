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
    global href
    urls = []
    users = []
    links = []
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
    }

    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = wd.Chrome(chromedriver)
    driver.get(b_url)
    # Все что будем брать из главного меню
    city = driver.find_element_by_class_name("_20Ixl")  # Ищем город в ссылках
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        try:
            if driver.find_element_by_class_name("DnHhI").is_displayed():
                button = driver.find_element_by_class_name("_2bexo")
                button.click()
                break
        except:
            continue
        if new_height == last_height:
            driver.quit()
            break
    href = driver.find_elements_by_class_name("MBUbs")  # Ищем ссылки на объявления
    for ls in href:
        links = {
            "href": ls.get_attribute("href")
        }
        urls.append(links)
    print(urls)
    for j in urls:
        print(j['href'])
        session = requests.Session()
        response = session.get(j['href'], headers=headers)
        if response.status_code == 200:
            soup = bs(response.content, "lxml")
            contact_div = soup.find_all("div", attrs={"class": "https://m.avito.ru/rossiya/transport"})
            for data in contact_div:
                try:
                    name = data.find("span", attrs={"class": "ZvfUX"}).text
                    phone = data.find("a", attrs={"class": "_2MOUQ"}).get("href")
                    user_data = {
                        "name": name,
                        "phone": phone
                    }
                    users.append(user_data)
                except:
                    pass
                print(users)
    return users


html = selenium_get_href("https://m.avito.ru/rossiya/dlya_biznesa")
print(html)
