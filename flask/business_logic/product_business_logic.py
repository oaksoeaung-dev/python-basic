import data_access.product_data_access as product_da #dependency

#Create
def create_product(name,price):
    #validation
    #Is it existing product?
    #Is it correct price?
    price = int(price)
    if price <= 0 :
        return False,"Price cannot be zero or negative value."
    
    product_da.create_product(name,price)
    return True,""

#Retrieve
def get_products():
    return product_da.get_products()

def get_product_by_Id(Id):
    #correct index, number?
    #is index in correct range?
    return product_da.get_product_by_Id(Id)

#Update
def update_product(id,name,price):
    #validation
    product_da.update_product(id,name,price)

#Delete
def delete_product(id):
    #validation
    product_da.delete_product(id)