import os
import sys
from functions import view_product_list, create_new_product_ui, update_product_ui, delete_product_ui
  

def create_new_product(product):
    file = open("products.txt", "a+")
    file.write(product)
    file.write("\n")
    file.close()

def update_product(replace_product, new_product):
    file = open("products.txt", "r")
    content = file.read()
    content = content.replace(replace_product, new_product)
    file = open("products.txt", "w")
    file.write(content)
    file.close()


def delete_product(product):
    file = open("products.txt", "r")
    content = file.read()
    content = content.replace(product + "\n", "")
    file = open("products.txt", "w")
    file.write(content)
    file.close

def create_new_courier(courier):
    file = open("couriers.txt", "a+")
    file.write(courier)
    file.write("\n")
    file.close()

def update_courier(replace_courier, new_courier):
    file = open("couriers.txt", "r")
    content = file.read()
    content = content.replace(replace_courier, new_courier)
    file = open("couriers.txt", "w")
    file.write(content)
    file.close()

def delete_courier(courier):
    file = open("couriers.txt", "r")
    content = file.read()
    content = content.replace(courier + "\n", "")
    file = open("couriers.txt", "w")
    file.write(content)
    file.close


def main_menu():
    choice = ''


    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Product Menu \n 2: View Courier Menu \n Please select a menu option above: ")

    if choice == "0":
        sys.exit
    
    elif choice == "1":
        product_menu()

    elif choice == "2":
        courier_menu()



def product_menu():
    choice = ''


    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Products \n 2: Create a New Product \n 3. Replace a Product \n 4. Delete a Product \n Please select a menu option above: ")

    if choice == "0":
        sys.exit
    
    elif choice == "1":
        view_product_list()
        menu()

    elif choice == "2":
        create_new_product_ui()

    elif choice == "3":
        update_product_ui()

    elif choice == "4":
        delete_product_ui()



def courier_menu():
    choice = ''


    while choice != "0" and choice != "1" and choice != "2" and choice != "3" and choice != "4": 
        choice = input("What would you like to do? \n 0: Exit App \n 1: View Couriers \n 2: Create a New Courier \n 3. Replace a Courier \n 4. Delete a Courier \n Please select a menu option above: ")

    if choice == "0":
        sys.exit
    
    elif choice == "1":
        view_courier_list()
        main_menu()

    elif choice == "2":
        create_new_courier_ui()

    elif choice == "3":
        update_courier_ui()

    elif choice == "4":
        delete_courier_ui()



main_menu()



        




