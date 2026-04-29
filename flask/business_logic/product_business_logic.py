import data_access.product_data_access as product_da #dependency

#Create
def create_product(name,price):
    #validation
    #Is it existing product?
    #Is it correct price?
    product_da.create_product(name,price)

#Retrieve
def get_products():
    return product_da.get_products()

def get_product_by_index(index):
    #correct index, number?
    #is index in correct range?
    return product_da.get_product_by_index(index)

#Update
def update_product(index,name,price):
    #validation
    product_da.update_product(index,name,price)

#Delete
def delete_product(index):
    #validation
    product_da.delete_product(index)