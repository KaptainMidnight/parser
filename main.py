# -*- charset: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import csv
# Имя, телефон, город, рубрика


def parser():
    #--------------------[ Ссылки ]---------------
    links_ad = []
    users_data = []
    global city, name, phone, category
    # --------------------[ Ссылки ]--------------
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    b_url = input("Enter url: ")
    session = requests.Session()
    request = session.get(b_url, headers=headers)
    if request.status_code == 200:
        try:
            soup = bs(request.content, "lxml")
            divs = soup.find_all("div", attrs={"class": "_328WR"})  # Search ad in url
            for div in divs:  # Search in url
                a = div.find("a", attrs={"class": "MBUbs"})['href']
                city = div.find("div", attrs={"class": "_20Ixl"}).text
                url_ad = f"https://m.avito.ru{a}"
                links_ad.append({
                    "href": url_ad
                })
                for i in links_ad:
                    new_session = requests.Session()
                    new_request = new_session.get(i['href'], headers=headers)
                    if new_request.status_code == 200:
                        new_soup = bs(new_request.content, "lxml")
                        jo = new_soup.find_all("div", attrs={"data-marker": "item-contact-bar"})  # Phone number and name
                        asjdf = new_soup.find_all("div", attrs={"class": "_1qEI9"})
                        for sad in asjdf:
                            category = sad.find("div", attrs={"class": "_1Jm7J"}).text
                        for j in jo:
                            try:
                                name = j.find("span", attrs={"class": "ZvfUX"}).text
                                phone = j.find("a", attrs={"data-marker": "item-contact-bar/call"})['href']
                                if "tel:" in phone:
                                    phone.split()
                                    phone = phone[5::1]
                                users_data.append({
                                    "name": name,
                                    "phone": phone,
                                    "city": city,
                                    "category": category
                                })
                            except:
                                pass
         except:
             print("Error")
             pass

        # except Exception as e:
            # pass


def file_write(users):
    with open("peoples.csv", "w") as file:
        a_pen = csv.writer(file)
        a_pen.writerow(("Имя", "Номер", "Город", "Категория"))
        for job in users:
            a_pen.writerow((job['name'], job['phone'], job['city'], job['category']))


row = parser()
file_write(parser)

