import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import time
import csv

chromedriver = "/Users/applemac/Downloads/chromedriver"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
}


def main():
    opers = []
    url_a = None
    data = []
    link = []
    global speciality
    global links
    url = "https://ulyanovsk.hh.ru/search/resume?clusters=true&exp_period=all_time&logic=normal&no_magic=false&order_by=relevance&pos=full_text&text=%D0%92%D1%80%D0%B0%D1%87&area=113&from=cluster_area&page=0"
    driver = wd.Chrome(chromedriver)
    driver.get("https://hh.ru/account/login?backurl=%2F")
    login = driver.find_element_by_name('username')
    login.clear()
    login.send_keys("resler174@mail.ru")
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys("rjynfrn_vjq1")
    driver.find_element_by_class_name("bloko-button").click()
    driver.get(url)
    page = get_page(url)
    # Получаем ссылки на резюме и парсим их
    time.sleep(5)
    try:
        for op in page:
            time.sleep(5)
            driver.get(op)
        url_a = driver.find_elements_by_xpath(
            "//div[@class='resume-search-item__content-wrapper']//a[@itemprop='jobTitle']")

        for j in url_a:
            speciality = j.text  # Специальность врача
            links = {
                'href': j.get_attribute('href'),
                'speciality': speciality
            }
            link.append(links)

        for i in link:
            try:
                driver.get(i['href'])  # Проходим по ссылке
                name = driver.find_element_by_class_name("header").text  # Берем имя
                phone = driver.find_element_by_class_name("bloko-link-switch").get_attribute(
                    "data-phone")  # Берем номер
                email = driver.find_element_by_xpath("//a[@itemprop='email']").text  # Берем почту
                data_user = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'speciality': i['speciality'],
                    'href': i['href']
                }
                data= []
                data.append(data_user)
                filew(data)
            except:
                pass
    except:
        pass
    return data


def filew(data):
    with open("animals.csv", "w") as file:
        wrtr = csv.writer(file)
        wrtr.writerow(("Имя", "Номер", "Почта", "Специальность", "Ссылка"))
        for i in data:
            wrtr.writerow((i['name'], i['phone'], i['email'], i['speciality'], i['href']))


def get_page(url):
    urls = []
    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        soup = bs(response.content, "lxml")
        try:
            pagintaion = soup.find_all('a', attrs={'data-qa': 'pager-page'})
            count = int(pagintaion[-1].text)
            for i in range(count):
                url = f"https://ulyanovsk.hh.ru/search/resume?clusters=true&exp_period=all_time&logic=normal&no_magic=false&order_by=relevance&pos=full_text&text=%D0%92%D1%80%D0%B0%D1%87&area=113&from=cluster_area&page={i}"
                if url not in urls:
                    urls.append(url)
        except:
            pass

    else:
        print("ERROR")
    return urls


if __name__ == '__main__':
    main()
