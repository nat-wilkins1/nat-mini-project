def define_products_from_file():
    products = open("products.txt").read().splitlines()
    print(products)

define_products_from_file()
