# -*- charset: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import csv
import time


def parser():
    # --------------------[ Links ]---------------
    links_ad = []
    users_data = []
    global city
    global name
    global phone
    global category
    global a
    # --------------------[ Links ]--------------
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    b_url = input("Enter url: ")
    session = requests.Session()
    request = session.get(b_url, headers=headers)
    print(request.status_code)
    if request.status_code == 200:
        try:
            soup = bs(request.content, "lxml")
            divs = soup.find_all("div", attrs={"class": "_328WR"})  # Search ad in url
            # ----------[ Search url ]----------
            for div in divs:
                a = div.find("a", attrs={"class": "eXo1j"}).get('href')
                city = div.find("div", attrs={"class": "_20Ixl"}).text
                url_ad = f"https://m.avito.ru{a}"  # URL ad
                links_ad.append({  # Dictionary with URL'S
                    "href": url_ad
                })
                # ----------[ Search in url ]----------
                for i in links_ad:  # Search in URL: phone number, city, name
                    new_session = requests.Session()
                    new_request = new_session.get(i['href'], headers=headers)
                    if new_request.status_code == 200:
                        new_soup = bs(new_request.content, "lxml")
                        jo = new_soup.find_all("div",
                                               attrs={"data-marker": "item-contact-bar"})  # Phone number and name
                        category_div = new_soup.find_all("div", attrs={"class": "_1qEI9"})
                        for sad in category_div:
                            category = sad.find("div", attrs={"class": "_1Jm7J"}).text
                        for j in jo:
                            name = j.find("span", attrs={"class": "ZvfUX"}).text  # Name seller
                            phone = j.find("a", attrs={"data-marker": "item-contact-bar/call"})['href']  # Phone
                            if "tel:" in phone:  # Delete "tel:"
                                phone.split()
                                phone = phone[5::1]
                        users_data.extend(name)
        except:
            pass
        print(f"Всего спаршено: {len(links_ad)}")
    return users_data


# _3H0VH - Обновление объявлений
# DnHhI - Объявления

def file_write(users):  # Write result data users
    with open("peoples.csv", "w") as file:
        a_pen = csv.writer(file)
        a_pen.writerow(("Имя", "Номер", "Город", "Категория"))  # Create columns 'name', 'phone', 'city', 'category'
        for job in users:
            a_pen.writerow((job['name'], job['phone'], job['city'], job['category']))  # Insert in table data users


parser = parser()
print(parser)
file_write(parser)
# https://m.avito.ru/rossiya/uslugi
