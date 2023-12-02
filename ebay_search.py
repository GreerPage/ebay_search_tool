"""
greer page & jack taylor

cgpage@uvm.edu
jwtaylor@uvm.edu

cs 1210 final project
"""

from ebay_search import user_input, search, sort


if __name__ == '__main__':
    item, budget, filters = user_input()
    items = search(item)
    items = sort(items, filters, budget)
    if not items:
        print('No items found, try changing your search criteria.')

    for item in items:
        print(item.name, item.link)
        choice = input('Press enter to show another item, or q to quit. ')
        if choice == 'q':
            break
        print()