import os
import sys
# from shopping_items import Fruits


def display_help():
	print('''
	=======> Help <=======
	'HELP' to display this menu
	'START' to start creating your shopping list
	'SHOW' to display your current items
	'DEL' to delete an item
	'QUIT' to exit the program
	''')
# create a list with the items needed

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



# Create function to change values of current items or update price of items in the cart

def begin_attempt():
    print('Here\'s a list of possible commands: HELP, START, QUIT')
    print('Welcome! What would you like to do?')
    while True:
        choose = input('> ')
        if choose.upper() == 'START':
            print('Shopping has begun\n')
            shopping_list()
        elif choose.upper() == 'HELP':
            display_help()
            continue
        elif choose.upper() == 'QUIT':
            sys.exit('Goodbye')


def shopping_list():
    clear_screen()
    print('It\'s time to go shopping!')
    # Convert all floating point numbers to max digits of 2 after the decimal
    clear_screen()
    item_dict = {}
    print('Enter HELP at any moment for HELP menu')
    cart = 0

    def asktodelete():
        while True:
            deleting_item = input("What item would you like to delete? ")
            if deleting_item.upper() == 'SHOW':
                show_items()
                continue
            if deleting_item in item_dict:
                item_dict.pop(deleting_item)
                show_items()
                print("You've successfully deleted {}.".format(deleting_item))
                if item_dict:
                    asking = input("Would you like to delete another item? ")
                    if asking.upper() == 'Y':
                        continue
                    elif asking.upper() == 'N':
                        break
                    elif asking.upper() != 'Y' or 'N':
                        break
                else:
                    print("You no longer have items in your cart..")
                    break
            elif deleting_item not in item_dict:
                print("That item is not in your cart..")
                continue

    def show_items():
        for key, value in item_dict.items():
            print(key + '-' * 5 + str(value))
        print('Current cart total: ', sum(item_dict.values()))
    while True:
        shop = input('Please enter an item: ')
        if shop.upper() == 'HELP':
            display_help()
            continue
        elif shop.upper() == 'EXIT':
            ''' Show total with taxes (or without taxes) with all the items in
            cronological order
            start without taxes first '''
            sys.exit("Goodbye")
        elif shop.upper() == 'SHOW':
            show_items()
            continue
        elif shop.upper() == 'DEL':
            asktodelete()
            continue
        quantity = int(input("How many would you like to add? "))
        print('You have added {} to your list\n'.format(shop))
        cost = float(input('Price of {}: '.format(shop)))
        item_dict[shop] = cost
        cart = sum(item_dict.values())
        print('You entered {} as the price of {}\n'.format(cost, shop))
        print('You now have {} items in your list.\n'.format(len(item_dict)))
        print('The total currently on your cart is {}'.format(cart))
        add_more_items = input('Would you like to add more items?(Y/N) ')
        if add_more_items == 'Y'.lower():
            pass
        else:
            print(f'Here\'s your cart and your total: \n')
            show_items()
            sys.exit('Goodbye')
        try:
            cost is float()
        except ValueError:
            print('Please enter a number')




begin_attempt()
