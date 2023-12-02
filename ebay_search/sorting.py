"""
greer page & jack taylor

cgpage@uvm.edu
jwtaylor@uvm.edu

cs 1210 final project
"""

def meets_filters(items, filters):
    """Removes items that do not meet the specified filters."""
    new = []
    for item in items: 
        if item.filters == filters:
            new.append(item)

    return new

def sort_highest_rating(items):
    """Sorts items by highest seller rating."""
    ratings = [e.rating for e in items]
    ratings.sort()
    ratings = ratings[::-1]
    sorted_items = []
    for rating in ratings:
        for item in items:
            if item.rating == rating:
                sorted_items.append(item)
                items.remove(item)
    
    return sorted_items

def budget_filter(items, budget):
    """Removes items that are out of budget."""
    new_prices = []
    for item in items:
        try:
            if item.price < budget:
                new_prices.append(item)
        except TypeError:
            avg = (item.price[1] - item.price[0]) / 2
            price = item.price[0] + avg
            if price < budget:
                new.append(item)
    
    return new_prices



def sort(items, filters, budget):
    """Handles all of the item sorting"""
    print(len(items))
    items = meets_filters(items, filters)
    print(len(items))
    items = budget_filter(items, budget)
    print(len(items))
    items = sort_highest_rating(items)
    print(len(items))
    return items
    



