import os

product_list = [ {"Name": "Apple", "Price": 100},
  {"Name": "Orange", "Price": 80},]
def is_empty(value):
  if value == "":
    return True
  return False
  
  

def create_product():
  name = input("Name : ")
  price = input("Price : ")

  if is_empty(name) or is_empty(price):
    return "Creation failed! Empty input."
  if not price.isdigit():
    return "Creation failed! Price must be number."
  product = {
    "Name" : name,
    "Price" : int(price)
  }
  product_list.append(product)
  return "Product has been created successfully."

def retrieve_product():
    if not product_list:
        return "No products found to display."
    
    print("\nRetrieve Product")
    
    for index, product in enumerate(product_list):
        print(f"[{index}] Name: {product['Name']} | Price: {product['Price']}")
    
    print("------------------------")
    
    input("\nPress Enter to return to menu...")
    
    return "Inventory viewed successfully."
    
    print("-" * 15) 
    input("\nPress Enter to return to menu...")
 
    return "Retrieved product list successfully."

def update_product():
  index = int(input("Index : "))
  name = input("Name : ")
  price = int(input("Price : "))
  product = product_list[index]
  product["Name"] = name
  product["Price"] = price
  return "Updated product successfully!"

def delect_product():
  if len(product_list) == 0:
    return "No product to delect."
  index = int(input("Index : "))
  if index < 0 or index >= len(product_list):
    return "Product not found."
  product_list.pop(index)

  return "Delected product successfully."

def display():
  message = ""
  while True:
    os.system("cls"if os.name == "nt" else "clear" )
    print("store front!".upper())
    if message :
      print(f"\nSystem message : {message}")
      message = ""
    print("""
    [1]Create
    [2]Retrieve
    [3]Update
    [4]Delect
    [5]Exit
    """)
    menu = input("Menu : ")
    if menu == "1":
      message = create_product()
    elif menu == "2":
      message = retrieve_product()
    elif menu == "3":
      message = update_product()
    elif menu == "4":
      message = delect_product()
    elif menu == "5":
      os.system("cls")
      print("Bye Bye!")
      exit()
    else:
      print("Invalid option.")
display()