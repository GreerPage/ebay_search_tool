"""
greer page & jack taylor

cgpage@uvm.edu
jwtaylor@uvm.edu

cs 1210 final project
"""

import requests
from .item import Item
from bs4 import BeautifulSoup

def search(item):
    """Searches Ebay and returns the items found."""
    r = requests.get(f'https://www.ebay.com/sch/i.html?_nkw={item}')
    soup = BeautifulSoup(r.text, 'html.parser')
    items = []
    for item in soup.find_all('li', class_='s-item'):
        i = Item(item)
        i.get_filters()
        i.get_price()
        i.get_seller_rating()
        items.append(i)

    return items
