import sys
# from functions_RF1 import create_new_product_ui, update_product_ui, delete_product_ui


products = open("products.txt").read().splitlines()
couriers = open("couriers.txt").read().splitlines()

# my_lists = [{'item_type':'product','list':products}, 'courier']

def write_items_to_file(item_type, list):
# This function opens the file names after the item_type and 
# writes each item on the list as a new line item

    update_file = f"{item_type}s.txt"
    file = open(update_file, "w")
    for list_item in list:
        file.write("%s\n" % list_item)   
    file.close()


def create_new_item(new_item, item_type, list):
# This function adds the item to the list or notifies the user that
# the item already exists within the list

    if type(new_item) is str:
        if new_item in list:
            print(f"This item already exists in {item_type}s")
        else:
            list.append(new_item)
            write_items_to_file(item_type, list)
    else:
        print("You must enter a string")
    return(list)



def create_new_item_ui(item_type, list):
    print(list)
    print(f"Above is the list of existing {item_type}s, please input new {item_type} name or input 0 to cancel: ")
    new_item = input()
    if new_item == "0":
        sub_menu(list, item_type)
    else: 
        create_new_item(new_item, item_type, list)
        print(f"Updated {item_type}s list below:")
        print(list)
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


def sub_menu(list, item_type):
    choice = ''

    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input(f"What would you like to do? \n 0: Return to Main Menu \n 1: View {item_type}s \n 2: Create a New {item_type} \n 3. Replace a {item_type} \n 4. Delete a {item_type} \n Please select a menu option above: ")

    if choice == "0":
        main_menu()
    
    elif choice == "1":
        print(f"Below is the current list of {item_type}s: \n")
        print(list)
        sub_menu(list, item_type)

    elif choice == "2":
        create_new_item_ui(item_type, list)

    elif choice == "3":
        update_item_ui(item_type, list)

    elif choice == "4":
        delete_item_ui(item_type, list)


def main_menu():
    choice = ''

    while choice != "0" and choice != "1" and choice != "2": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Product Menu \n 2: View Courier Menu \n Please select a menu option above: ")

    if choice == "0":
        # ÷for list in my_lists:
        write_items_to_file('product', products)
        write_items_to_file('courier', couriers)
        sys.exit
    
    elif choice == "1":
        sub_menu(products, "product")

    elif choice == "2":
        sub_menu(couriers, "courier")


if __name__ == '__main__':
    main_menu()









        




