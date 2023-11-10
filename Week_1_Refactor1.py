import sys
# from functions_RF1 import create_new_product_ui, update_product_ui, delete_product_ui


products = open("products.txt").read().splitlines()
couriers = open("couriers.txt").read().splitlines()


def write_products_to_file():
    file = open("products.txt", "w")
    for product in products:
        file.write("%s\n" % product)   
    file.close()

def write_couriers_to_file():
    file = open("couriers.txt", "w")
    for courier in couriers:
        file.write("%s\n" % courier)   
    file.close()

def create_new_product(product):
    if type(product) is str:
        if product in products:
            print("This product already exists")
        else:
            products.append(product)
    else:
        print("You must enter a string")
    write_products_to_file()

def create_new_product_ui():
    print(products)
    print("Above is the list of existing products, please input new product name or input 0 to cancel: ")
    product = input()
    create_new_product(product)
    print("Updated product list below:")
    print(products)
    product_menu()

def update_product_ui():
    print(products)
    print("Above is the list of existing products, which product would you like to replace? Input 0 to cancel: ")
    replace_product = input()
    if replace_product == "0":
        product_menu()
    else:
        print("What would you like to replace it with? ")
        new_product = input()
        update_product(replace_product, new_product)
        print("Updated product list below:")
        print(products)
        product_menu()


def update_product(replace_product, new_product):
    product_index = products.index(replace_product)
    products[product_index] = new_product
    write_products_to_file()


def delete_product(product):
    products.remove(product)
    write_products_to_file()

def delete_product_ui():
    print(products)
    print("Above is the list of existing products, which product would you like to delete? Input 0 to cancel: ")
    product = input()
    if product == "0":
        product_menu()
    else:
        delete_product(product)
        print("Updated product list below:")
        print(products)
        product_menu()


def create_new_courier(courier):
    if type(courier) is str:
        if courier in couriers:
            print("This courier already exists")
        else:
            couriers.append(courier)
    else:
        print("You must enter a string")
        write_couriers_to_file()

def create_new_courier_ui():
    print(couriers)
    print("Above is the list of existing products, please input new courier name or input 0 to cancel: ")
    courier = input()
    create_new_courier(courier)
    print("Updated courier list below:")
    print(couriers)
    product_menu()

def update_courier_ui():
    print(couriers)
    print("Above is the list of existing couriers, which courier would you like to replace? Input 0 to cancel: ")
    replace_courier = input()
    if replace_courier == "0":
        courier_menu()
    else:
        print("What would you like to replace it with? ")
        new_courier = input()
        update_courier(replace_courier, new_courier)
        print("Updated courier list below:")
        print(couriers)
        courier_menu()


def update_courier(replace_courier, new_courier):
    courier_index = couriers.index(replace_courier)
    couriers[courier_index] = new_courier
    write_couriers_to_file()


def delete_courier(courier):
    couriers.remove(courier)
    write_couriers_to_file()

def delete_courier_ui():
    print(couriers)
    print("Above is the list of existing couriers, which courier would you like to delete? Input 0 to cancel: ")
    courier = input()
    if courier == "0":
        courier_menu()
    else:
        delete_courier(courier)
        print("Updated courier list below:")
        print(couriers)
        courier_menu()

def product_menu():
    choice = ''

    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input("What would you like to do? \n 0: Return to Main Menu \n 1: View Products \n 2: Create a New Product \n 3. Replace a Product \n 4. Delete a Product \n Please select a menu option above: ")

    if choice == "0":
        main_menu()
    
    elif choice == "1":
        print(products)
        product_menu()

    elif choice == "2":
        create_new_product_ui()

    elif choice == "3":
        update_product_ui()

    elif choice == "4":
        delete_product_ui()


def courier_menu():
    choice = ''

    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input("What would you like to do? \n 0: Return to Main Menu \n 1: View Couriers \n 2: Create a New Courier \n 3. Replace a Courier \n 4. Delete a Courier \n Please select a menu option above: ")

    if choice == "0":
        main_menu()
    
    elif choice == "1":
        print(couriers)
        courier_menu()

    elif choice == "2":
        create_new_courier_ui()

    elif choice == "3":
        update_courier_ui()

    elif choice == "4":
        delete_courier_ui()



def main_menu():
    choice = ''


    while choice != "0" and choice != "1" and choice != "2": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Product Menu \n 2: View Courier Menu \n Please select a menu option above: ")

    if choice == "0":
        write_products_to_file
        write_couriers_to_file
        sys.exit
    
    elif choice == "1":
        product_menu()

    elif choice == "2":
        courier_menu()

main_menu()









        




