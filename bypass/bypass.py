import requests
from bs4 import BeautifulSoup as bs
from random import choice


def get_html(url, useragent=None, proxy=None):
    response = requests.get(url, headers=useragent, proxies=proxy)
    return response.text


def get_ip(html):
    soup = bs(html, "lxml")
    ip = soup.find("span", attrs={"class": "ip"}).text.strip()
    ua = soup.find("span", attrs={"class": "ip"}).find_next_sibling("span").text.strip()
    print(ip)
    print(ua)


def main():
    url = "http://sitespy.ru/my-ip"
    user_agents = open("useragents.txt").read().split("\n")
    proxies = open("foxproxy.txt").read().split("\n")
    proxy = {"http": "http://" + choice(proxies)}
    user_agent = {"user-agent": choice(user_agents)}
    html = get_html(url, user_agent, proxy)
    try:
        html = get_html(url, user_agent, proxy)
    except:
        pass
    get_ip(html)


print(main())
