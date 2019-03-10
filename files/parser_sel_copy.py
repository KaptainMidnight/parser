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
        try:
            links = {
                "href": i.get_attribute("href")
            }
            for j in links:
                driver.get(links[j])
                num_page_ads = len(links[j])
                for s in range(num_page_ads):
                    session = requests.Session()
                    response = session.get(links[j], headers=headers)
                    if response.status_code == 200:
                        soup = bs(response.content, "lxml")
                        div_contact_bar = soup.find_all("div", attrs={"class": "_3U_HU"})
                        for data in div_contact_bar:
                            name = data.find("span", attrs={"class": "ZvfUX"}).text
                            phone = data.find("span", attrs={"class": "_2MOUQ"}).get("href")
                            user_data = {
                                "name": name,
                                "phone": phone  # НЕ ЗАБУДЬ ДОПИСАТЬ ГОРОД
                            }
                    else:
                        print(f"Произошла ошибка: {response.status_code}")
        except:
            pass
    driver.quit()


if __name__ == "__main__":
    url = "https://m.avito.ru/rossiya/uslugi"
    main(url)
