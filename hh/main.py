import csv
from bs4 import BeautifulSoup as bs
import requests
from robobrowser import RoboBrowser as rb


def main():
    browser = rb(history=True)
    browser.open("https://hh.ru/account/login?backurl=%2F.php")
    form = browser.get_form(action="/account/login.php")
    form['HH-AuthForm-Login'].value = "resler174@mail.ru"
    form['HH-AuthForm-Password'].value = "rjynfrn_vjq1"
    print(form)


main()
