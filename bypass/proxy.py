import requests
from bs4 import BeautifulSoup as bs


def main():
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)"
    }
    url = "http://spys.one/proxys/"
    session = requests.session()
    response = session.get(url, headers="")
    if response.status_code == 200:
        soup = bs(response.content, 'lxml')
        main_div = soup.find_all('tr', attrs={'class': 'spy1xx'})
        for i in main_div:
            a = i.find("a")
            links = {
                'href': a.get('href')
            }
            for pr in links:
                new_session = requests.Session()
                new_response = new_session.get(links[pr], 'lxml')
                if new_response.status_code == 200:
                    new_soup = bs(new_response.content, 'lxml')
                    proxy = new_soup.find_all('tr', attrs={'class': 'spy1xx'})
                    for j in proxy:
                        proxies = j.find('font', attrs={'class': 'spy14'}).text
                        print(proxies)


if __name__ == '__main__':
    main()
