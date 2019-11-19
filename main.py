#web crawler#
import requests
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring
import selenium,time
from selenium import webdriver
from keyboard import press
from pynput.keyboard import Key, Controller

#########################################
def your_search():
    a= input("What do you look for? : ")
    return a
print(your_search)
#########################################


#########################################
browser = webdriver.Chrome('C:/Users/acirimia/Downloads/chromedriver.exe')
#########################################
from search import your_search
var = your_search()
browser.get('https://www.juridice.ro/?s='+ str(var).replace(' ','+'))

def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = ('https://www.juridice.ro/?s='+ str(var).replace(' ','+'))
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.find_all('a',{'rel': 'bookmark'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, features="html.parser")
#     for item_description in soup.findAll('a',{'rel': 'bookmark'}):

web_crawler(2)