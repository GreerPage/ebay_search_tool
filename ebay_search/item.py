"""
greer page & jack taylor

cgpage@uvm.edu
jwtaylor@uvm.edu

cs 1210 final project
"""

class Item():
    """parse html into useful information for sorting."""

    def __init__(self, item):
        self.item = item
        self.price = item.find('span', class_='s-item__price')
        self.rating = item.find('span', class_='s-item__seller-info-text')
        self.link = item.find_all('a')[0].get('href')
        self.name = item.find('div', class_='s-item__title').span.text
        self.filters = {
            'new': False, 
            'buy': False, 
            'free_shipping': False, 
            'free_returns': False
        }
    
    def get_price(self):
        self.price = self.price.text.replace('$', '').replace(',', '')
        try:
            self.price = float(self.price)
        except ValueError:
            self.price = self.price.replace(' to ', ' ')
            self.price = self.price.split(' ')
            self.price = [float(p) for p in self.price]
    
    def get_seller_rating(self):
        try:
            self.rating = self.rating.text.split(' ')[-1].replace('%', '')
            self.rating = float(self.rating)
        except AttributeError:
            self.rating = 0
    
    def get_filters(self):
        if self.item.findAll(text='Brand New'):
            self.filters['new'] = True
        if self.item.findAll(text='Free shipping'):
            self.filters['free_shipping'] = True
        if self.item.findAll(text='Free returns'):
            self.filters['free_returns'] = True
        if self.item.findAll(text='Buy It Now') or self.item.findAll(text='or Best Offer'):
            self.filters['buy'] = True
