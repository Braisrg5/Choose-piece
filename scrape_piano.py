'''Program to scrape the page https://www.pianolibrary.org/difficulty/'''
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    URL = 'https://www.pianolibrary.org/difficulty/'
    difficulty = requests.get(URL, timeout=10)
