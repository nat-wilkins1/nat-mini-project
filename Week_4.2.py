import sys
import csv
from csv import DictReader
from csv import writer
from pprint import pprint

# item_types = ['product', 'courier', 'order']
products = []
couriers = []
orders = []

def read_products_from_csv():
        with open("products.csv", "r", encoding = 'utf-8-sig') as file:
            reader = DictReader(file)
            products = list(reader)
            pprint(products, sort_dicts = False)

def read_couriers_from_csv():
        with open("couriers.csv", "r", encoding = 'utf-8-sig') as file:
            reader = DictReader(file)
            couriers = list(reader)
            pprint(couriers, sort_dicts = False)

def read_orders_from_csv():
        with open("orders.csv", "r", encoding = 'utf-8-sig') as file:
            reader = DictReader(file)
            orders = list(reader)
            pprint(orders, sort_dicts = False)

def search_lists(ID, list):
    return [element for element in list if element['ID'] == ID]

# orders = []
# with open("orders.csv", 'r', encoding = 'utf-8-sig') as file:
#     reader = DictReader(file)
#     orders = list(reader)


def write_items_to_file(new_item, item_type):
# This function opens the file named after the item_type and 
# writes the new dictionary as a new line

    update_file = f"{item_type}s.csv"
    try:
        with open(update_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_item)

    except FileNotFoundError as fnfe:
        print("Unable to open file: " + str(fnfe))
    except Exception as e:
        print("An error occurred: " + str(e))

    finally:   
        file.close()
    
    read_products_from_csv()


def create_new_item(new_item, item_type):
# This function adds the item to the list or notifies the user that
# the item already exists within the list

    # if type(new_item) is str:
    # if new_item in list:
    #     print(f"This item already exists in {item_type}s")
    # else:
    #     # list.append(new_item)
    write_items_to_file(new_item, item_type)
    # else:
    #     print("You must enter a string")
    # return(list)



def create_new_item_ui(item_type, list):
    read_products_from_csv()
    print(f"Above is the list of existing {item_type}s, please input new {item_type} ID: ")
    new_item_ID = input()
    print(f"Please input new {item_type} name: ")
    new_item_name = input()
    print(f"Please input the selling price for {new_item_name}: ")
    new_item_price = input()

    new_item = [new_item_ID, new_item_name, new_item_price]

    create_new_item(new_item, item_type)
    print(f"Updated {item_type}s list below:")
    read_products_from_csv()
    sub_menu(list, item_type)


def update_item_ui(item_type, list):
    print(list)
    print(f"Above is the list of existing {item_type}s, which {item_type} would you like to replace? Input 0 to cancel: ")
    replace_item = input()
    if replace_item == "0":
        sub_menu(list, item_type)
    elif replace_item not in list:
        print(f"This item does not exist in {item_type}s")
    else:
        print("What would you like to replace it with? ")
        new_item = input()
        if new_item in list:
            print(f"This item already exists in {item_type}s")
        else:
            update_item(list, replace_item, new_item, item_type)
            print(f"Updated {item_type}s list below:")
            print(list)
            sub_menu(list, item_type)


def update_item(list, replace_item, new_item, item_type):
    if type(new_item) is str:
        if replace_item in list:
            item_index = list.index(replace_item)
            list[item_index] = new_item
            write_items_to_file(item_type, list)
        else:
            print(f"This item does not exist in {item_type}s")
    else:
        print("You must enter a string")
    return(list)


def delete_item_from_list(delete_item, item_type, list):
    if type(delete_item) is str:
        if delete_item not in list:
            print(f"Item does not exist in {item_type}s")
        else:
            list.remove(delete_item)
            write_items_to_file(item_type, list)
    else:
        print("You must enter a string")
    return(list)


def delete_item_ui(item_type, list):
    print(list)
    print(f"Above is the list of existing {item_type}s, which {item_type} would you like to delete? Input 0 to cancel: ")
    delete_item = input()
    if delete_item == "0":
        sub_menu(list)
    elif delete_item not in list:
        print(f"This item does not exist in {item_type}s")
    else:
        delete_item_from_list(delete_item, item_type, list)
        print(f"Updated {item_type} list below:")
        print(list)
        sub_menu(list, item_type)

def create_new_order(item_type, list, new_order):
    list.append(new_order)
    write_items_to_file(item_type, list)
    return(list)  


def create_new_order_ui(item_type, list):
    print(list)
    print(f"Above is the current list of {item_type}s, please enter the name of the Customer to create a new {item_type}:")
    new_order = {}
    new_order["customer_name"] = input()
    print("Please add a customer address to the order")
    new_order["customer_address"] = input()
    print("Please add a customer phone number to the order")
    new_order["phone_number"] = input()
    new_order["status"] = "PREPARING"
    create_new_order(item_type, list, new_order)
    print(f"Updated {item_type} list below:")
    print(list)
    sub_menu(list, item_type)

def update_order_status(item_type, list, update_order, status_update):
    update_order["status"] = status_update
    write_items_to_file(item_type, list)
    return(list)  

def update_order_status_ui(item_type, list):
    print(list)
    print(f"Above is the current list of {item_type}s, please select an order to update its status:")
    for order in orders:
        # if input() == "0":
        #     sub_menu(list, item_type)
        if order["customer_name"] == input():
            update_order = order
            print(f"What should the status be changed to?")
            # update_order["status"] = input()
            status_update = input()
            update_order_status(item_type, list, update_order, status_update)
    print(f"Updated {item_type} list below:")
    print(list)
    sub_menu(list, item_type)


def sub_menu(list, item_type):
    choice = ''

    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input(f"What would you like to do? \n 0: Return to Main Menu \n 1: View {item_type}s \n 2: Create a New {item_type} \n 3. Update a {item_type} \n 4. Delete a {item_type} \n Please select a menu option above: ")

    if choice == "0":
        main_menu()
    
    elif choice == "1":
        print(f"Below is the current list of {item_type}s: \n")
        read_products_from_csv()
        sub_menu(list, item_type)

    elif choice == "2":
        if item_type == "order":
            create_new_order_ui(item_type, list)
        else:
            create_new_item_ui(item_type, list)

    elif choice == "3":
        if item_type == "order":
            update_order_status_ui(item_type, list)
        else:
            update_item_ui(item_type, list)

    elif choice == "4":
        delete_item_ui(item_type, list)



def main_menu():
    choice = ''

    while choice != "0" and choice != "1" and choice != "2" and choice != "3": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Product Menu \n 2: View Courier Menu \n 3: View Order Menu \n Please select a menu option above: ")

    if choice == "0":
        sys.exit
    
    elif choice == "1":
        sub_menu(products, "product")

    elif choice == "2":
        sub_menu(couriers, "courier")

    elif choice == "3":
        sub_menu(orders, "order")


if __name__ == '__main__':
    main_menu()









        




