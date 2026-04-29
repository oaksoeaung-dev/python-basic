products = []

#Create
def create_product(name,price):
    products.append({"name": name, "price":price})

#Retrieve
def get_products():
    return products

def get_product_by_index(index):
    return products[index]

#Update
def update_product(index,name,price):
    current = products[index]
    current["name"] = name
    current["price"] = price

#Delete
def delete_product(index):
    products.pop(index)