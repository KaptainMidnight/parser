# -*- charset: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import csv
import time


def main():
    # -----[ Headers ]-----
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    # -----[ Headers ]-----

    # -----[ Global vars ]-----
    global city
    global name
    global phone
    global user_data
    global a
    global var
    global user
    # -----[ Global vars ]-----
    b_url = input("Enter site URL: ")
    session = requests.Session()
    response = session.get(b_url, headers=headers)
    if response.status_code == 200:  # If the answer is 200, then we do the pars
        try:
            user = []
            soup = bs(response.content, "lxml")
            ads = soup.find_all("div", attrs={"class": "_328WR"})
            for data in ads:
                try:
                    a = data.find("a", attrs={"class": "MBUbs"})["href"]
                except:
                    pass
                city = data.find("div", attrs={"class": "_20Ixl"}).text
                url_add = f"https://m.avito.ru{a}"
                links = {
                    "href": url_add
                }
                for data_user in links:
                    time.sleep(5)
                    new_session = requests.Session()
                    new_response = new_session.get(links[data_user], headers=headers)
                    if new_response.status_code == 200:
                        new_soup = bs(new_response.content, "lxml")
                        contact_bar = new_soup.find_all("div", attrs={"class": "_3U_HU"})
                        for info in contact_bar:
                            name = info.find("span", attrs={"class": "ZvfUX"}).text
                            try:
                                phone = info.find("a", attrs={"class": "_2MOUQ"})["href"]
                            except:
                                pass
                            if "tel:" in phone:
                                phone.split()
                                phone = phone[4::1]
                            user_data = {
                                "name": name,
                                "phone": phone,
                                "city": city
                            }
                            user.append(user_data)
                            print(user)
        except:
            pass
    else:
        print(f"Произошла ошибка: {response.status_code}")
    return user

def file_write(data):
    with open("file.csv", "w", encoding="utf-8") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Номер", "Город"))
        for i in data:
            wrtr.writerow((i['name'], i['phone'], i['city']))
            print("oK")


parser = main()
print(parser)
file_write(parser)

# https://m.avito.ru/rossiya/uslugi?owner[]=private&sort=default&withImagesOnly=false
