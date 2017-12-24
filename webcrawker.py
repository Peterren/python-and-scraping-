# Yincheng Ren  (yr5ka)
from bs4 import BeautifulSoup
import urllib
import re
import pandas as pd
import requests
from urllib.request import urlopen
from urllib.parse import urlparse
import os
import string

#need to get url, get links, get content
#put a seed first
#seed is https://www.google.com/search?q=

def search_on_google(keywords):
    google_search = "https://www.google.com/search?q="+keywords
    google_response = requests.get(google_search)
    return google_response.text

seed_page = search_on_google("Happy")
soup = BeautifulSoup(seed_page, 'lxml')
all_result=soup.find_all('div',attrs={'class':['g']})
print(all_result)
print('-----------')
all_seeds = [item['href']
             for result in all_result
             for item in result.find_all('a')
             if 'href' in item.attrs]
all_seeds = [seed for seed in all_seeds
             if not seed.startswith("/search?")
             ]
for seed in all_seeds:
    str.replace(seed, "/url?q=", "?")
print(all_seeds)

def get_page(page_url):
    """
    based on the url, get the page information
    """
    try:
        r = requests.get(page_url)
        return r.text
    except Exception as inst:
        return None