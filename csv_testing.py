import csv
from csv import DictWriter
from csv import DictReader
from pprint import pprint

# # write to a CSV file
# with open("couriers.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 28, "New York"])
#     writer.writerow(["Bob", 35, "San Francisco"])
#     # file.close()

products = []

# # read from a CSV file
def read_products_from_csv():
        with open("products.csv", "r", encoding = 'utf-8-sig') as file:
            reader = DictReader(file)
            products = list(reader)
            # pprint(products, sort_dicts = False)
            for product in products:
                for key, value in product.items():
                    print(key, value)
    

read_products_from_csv()

def search_lists(ID, products):
    return [element for element in products if element['Product_Name'] == ID]

update_item = search_lists('T', products)

print(update_item)


# # csv data
# row = ['6', 'Jake', '07780585751']

# with open("products.csv", 'a', newline = '') as file:
#     writer = csv.writer(file)
#     writer.writerow(row)


