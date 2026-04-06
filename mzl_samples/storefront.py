#CURD Aplication
#Create
#Update
#Delete 
#Retrieve

import os

product_list = []

def show_menu(menu_name):
    os.system("cls")
    print(f"\n[ {menu_name} ]\n")

def create_product():
    show_menu("Create Product")
    #name - price => keys
    name = input("Name: ")
    price = int(input("Price: "))

    product = {
        "Name" : name,
        "Price" : price
    }  
    product_list.append(product)
    return "Create product successfully."

def retrieve_product_list():
    show_menu("Retrieve Product")
    index = 0
    for product in product_list:
        for key,value in product.items():
            print(f"{index}. {key} - {value}")
        index += 1

    return "Retrieved product list successfully."

def update_product():
    show_menu("Update Product")
    index = int(input("Index: "))

    if index < 0 or index >= len(product_list):
        return "Product not found."

    name = input("Name: ")
    price = int(input("Price: "))

    product = product_list[index]
    product["Name"] = name
    product["Price"] = price

    return "Updated product successfully."

def delete_product():
    show_menu("Delete Product")
    index = int(input("Index: "))

    if index < 0 or index >= len(product_list):
        return "Product not found."

    product_list.pop(index)

    return "Delete product successfully."

message = ""

while True:
    print("\nStore front!\n")
    if(message != ""):
        print(f"\nSystem message: {message} \n")
    print("""
[1] Create
[2] Retrieve
[3] Update
[4] Delete
[5] Exit
""")

    menu = input("Menu: ")

    if menu == "1":
        message = create_product()
    elif menu == "2":
        message = retrieve_product_list()
    elif menu == "3":
        message = update_product()
    elif menu == "4":
        message = delete_product()
    elif menu == "5":
        os.system("cls")
        print("Bye Bye!")
        exit()
    else:
        os.system("cls")
        message = "Invalid menu."

