# -*- charset:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
from robobrowser import RoboBrowser


def parsing_site():
    br = RoboBrowser(parser="lxml")
    return br

def check_button():
    pass

def press_button():
    pass


if __name__ == '__main__':
    parsing_site()
