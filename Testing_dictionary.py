# def create_new_order(item_type, list, new_order):
#     list.append(new_order)
#     # write_items_to_file(item_type, list)
#     return(list)   
orders = [{"customer_name": "John", "customer_address": "Unit 12, BA4 1BD", "phone_number": "07695746882", "status": "PREPARING"}]

# def create_new_order_ui(item_type, list, new_order):
    # print(list)
print(f"Above is the current list of orders, please enter the name of the Customer to create a new order:")
order = {}
order["customer_name"] = input()
print("Please add a customer address to the order")
order["customer_address"] = input()
print("Please add a customer phone number to the order")
order["phone_number"] = input()
order["status"] = "PREPARING"
orders.append(order)
# # create_new_order(item_type, list, new_order)
# print(f"Updated orders list below: \n")
print(orders)
    # sub_menu(list, item_type)

# item_type = "order"
# create_new_order_ui(item_type, list, new_order)


# for key, value in orders.items():
#     print('key: ' + key + ", " + 'value: ' + str(value))
