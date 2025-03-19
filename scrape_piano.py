'''Program to scrape the page https://www.pianolibrary.org/difficulty/'''
from bs4 import BeautifulSoup
import requests


def main():
    '''Main program.'''
    url = 'https://www.pianolibrary.org/difficulty/'
    difficulty = requests.get(url, timeout=10)
    soup = BeautifulSoup(difficulty.text, 'html.parser')
    print(soup.body.contents)


if __name__ == '__main__':
    main()
