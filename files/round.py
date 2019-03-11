from selenium import webdriver as wd
import csv


def main(url):
    global href
    urls = []
    user_data = []
    global links
    chromedriver = "/Users/applemac/Downloads/chromedriver"
    driver = wd.Chrome(chromedriver)
    driver.get(url)  # Главная ссылка с объявлениями
    divs = driver.find_elements_by_xpath("//div[@class='_3B2-r']//a[@class='MBUbs']")
    href = driver.find_elements_by_xpath("//a[@class='MBUbs']")
    print(len(href))
    # for j in urls:
    #     driver.get(j['href'])
    #     name = driver.find_elements_by_class_name("ZvfUX")
    #     phone = driver.find_elements_by_class_name("_2MOUQ")
    #     for f, b in zip(name, phone):
    #         user = {
    #             "name": f.text,
    #             "phone": b.get_attribute("href")
    #         }
    #         user_data.append(user)
    return user_data


def file_writer(data):
    with open("base.csv", "w") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Телефон"))
        for i in data:
            wrtr.writerow((i['name'], i['phone']))


url = input("Enter site URL: ")
parser = main(url)
file_writer(parser)
