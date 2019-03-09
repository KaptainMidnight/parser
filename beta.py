# -*- charset: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
from headers import fake_user


def main():
    # -----[ Settings ]-----
    links = []
    user_data = []
    # -----[ Settings ]-----

    # -----[ Global vars ]-----
    global exile
    global reference
    global city
    global name
    global phone
    global category
    # -----[ Global vars ]-----
    headers = fake_user()
    b_url = str(input("Enter site URL: "))
    session = requests.Session()
    response = session.get(b_url, headers=headers)
    if response.status_code == 200:  # If the answer is 200, then we do the pars
        soup = bs(response.content, "lxml")
        announcements = soup.find_all("div", attrs={"class": "_328WR"})
        # -----[ Looking for links ]-----
        for data in announcements:
            try:
                exile = data.find("a", attrs={"class": "eXo1j"})['href']
                reference = f"https://m.avito.ru{exile}"
                links.append({
                    "href": reference
                })
            except TypeError:
                pass
            for contact in links:
                new_session = requests.Session()
                new_requests = new_session.get(contact['href'], headers=headers)
                if new_requests.status_code == 200:
                    new_soup = bs(new_requests.content, "lxml")
                    contact_bar = new_soup.find_all("div", attrs={"class": "ZvfUX"})
                    for loop in contact_bar:
                        name = loop.find("span", attrs={"class": "ZvfUX"}).text
                        user_data.append({
                            "name": name
                        })
                        print(user_data)
                else:
                    print("Could not connect to the site")
    else:  # If the server response is not equal to 200, we display an error
        print(f"Could not connect to the site: {b_url}")


print(main())
