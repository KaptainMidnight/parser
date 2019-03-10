from selenium import webdriver as wd
import csv
import time


def main(url):
    urls = []
    user_data = []
    global links
    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = wd.Chrome(chromedriver)
    driver.get(url)  # Главная ссылка с объявлениями
    block = driver.find_elements_by_class_name("_2bexo")
    if block == []:
        pass
    else:
        for ui in block:
            ui.click()
    href = driver.find_elements_by_class_name("MBUbs")
    for i in href:
        links = {
            "href": i.get_attribute("href")
        }
        urls.append(links)
    for j in urls:
        if j['href'] == None:
            block = driver.find_elements_by_class_name("_2bexo")
            for ui in block:
                ui.click()
        time.sleep(2)
        driver.get(j['href'])
        name = driver.find_elements_by_class_name("ZvfUX")
        phone = driver.find_elements_by_class_name("_2MOUQ")
        for f, b in zip(name, phone):
            user = {
                "name": f.text,
                "phone": b.get_attribute("href")
            }
            user_data.append(user)
            print(len(user_data))
    return user_data


def file_writer(data):
    with open("dase.csv", "w") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Телефон"))
        for i in data:
            wrtr.writerow((i['name'], i['phone']))


url = input("Enter site URL: ")
parser = main(url)
file_writer(parser)
