"""
greer page & jack taylor

cgpage@uvm.edu
jwtaylor@uvm.edu

cs 1210 final project
"""

def user_input():
    """Recieves user input for various queries and outputs a strings and a dict"""
    uri = input("What item are you looking for?: ").lower()
    uri = uri.replace(" ", "+")
    
    while True:
        try:
            budget = float(input('Enter your budget: '))
            if budget > 0:
                break
            else:
                print('Enter a positive number.')
        except ValueError:
            print('Please enter a number.')
        
    filters = {
        'free_shipping': False, 
        'free_returns': False, 
        'new': False,
        'buy': False
    }

    while True:
        fs = input("Would you like free shipping? (y/n): ")
        if fs.lower() not in ["y", "n"]:
            print("Please only enter 'y' for yes or 'n' for no.")
        else:
            if fs == "y":
                filters['free_shipping'] = True
            break

    while True:
        fr = input("Would you like free returns? (y/n): ")
        if fr.lower() not in ["y", "n"]:
            print("Please only enter 'y' for yes or 'n' for no.")
        else:
            if fr == "y":
                filters['free_returns'] = True
            break

    while True:
        new = input("Would you like your item new? (y/n): ")
        if new.lower() not in ["y", "n"]:
            print("Please only enter 'y' for yes or 'n' for no.")
        else:
            if new == "y":
                filters['new'] = True
            break

    while True:
        buy = input("Are you buying or bidding? (buy/bid): ").lower()
        if buy != "buy" and buy != "bid":
            print("Please only enter 'bid' or 'buy'.")
        else:
            if buy == "buy":
                filters["buy"] = True
            break

    return uri, budget, filters
