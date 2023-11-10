

def view_product_list():
    file = open("products.txt", "r")
    contents = file.read()
    print(contents)
    file.close()


def create_new_product_ui():
    view_product_list()
    print("Above is the list of existing products, please input new product name or input 0 to cancel: ")
    product = input()
    # if product == "0":
    #     menu()
    # else:    
    create_new_product(product)
    print("Updated product list below:")
    view_product_list()
    menu()


def update_product_ui():
    view_product_list()
    print("Above is the list of existing products, which product would you like to replace? Input 0 to cancel: ")
    replace_product = input()
    # if replace_product == "0":
    #     menu()
    # else:
    print("What would you like to replace it with? ")
    new_product = input()
    update_product(replace_product, new_product)
    print("Updated product list below:")
    view_product_list()
    menu()


def delete_product_ui():
    view_product_list()
    print("Above is the list of existing products, which product would you like to delete? Input 0 to cancel: ")
    product = input()
    # if product == "0":
    #     menu()
    # else:
    delete_product(product)
    print("Updated product list below:")
    view_product_list()
    menu()    


# def view_courier_list():
#     file = open("couriers.txt", "r")
#     contents = file.read().splitlines()
#     print("\n The list of couriers can be seen below \n")
#     print(contents)
#     print("\n")
#     file.close()

# view_courier_list()

