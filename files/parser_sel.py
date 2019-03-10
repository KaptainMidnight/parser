from selenium import webdriver as wd
import csv
import requests
from bs4 import BeautifulSoup as bs


def main(url):
    # -----[ HTTP Headers ]-----
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
    }
    # -----[ HTTP Headers]-----

    # -----[ Global vars ]-----
    global user
    global user_data
    global name
    global phone
    global links
    global city
    # -----[ Global vars ]-----
    with open("file.csv", "w") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Номер", "Город"))  # Имя | Номер | Город
    
    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = wd.Chrome(chromedriver)
    driver.get(url)
    href = driver.find_elements_by_class_name("MBUbs")
    for i in href:
        links = {
            "href": i.get_attribute("href")
        }
        for j in links:
            driver.get(links[j])



def parse(url):
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        soup = bs(response.content, "lxml")
        contact_bar = soup.find_all("div", attrs={"class": "_3U_HU"})
        for i in contact_bar:
            name = i.find("span", attrs={"class": "ZvfUX"}).text
            phone = i.find("span", attrs={"class": "_2MOUQ"}).get("href")
            user_data = {
                "name": name,
                "phone": phone
            }
    else:
        print("ERROR")


if __name__ == "__main__":
    url = "https://m.avito.ru/rossiya/uslugi"
    main(url)
