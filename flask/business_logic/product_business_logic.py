from data_access.product_data_access import ProductDataAccess #dependency
from models.product import Proudct

class ProductBusinessLogic:
    def __init__(self):
        self.da = ProductDataAccess()

    #Create
    def create_product(self,product:Proudct):
        #validation
        #Is it existing product?
        #Is it correct price?
        success,message =  product.validate()
        if not success:
            return success,message
        
        self.da.create_product(product)        
        return True,None

    #Retrieve
    def get_products(self):
        return self.da.get_products()

    def get_product_by_Id(self,Id):
        #correct index, number?
        #is index in correct range?
        return self.da.get_product_by_Id(Id)

    #Update
    def update_product(self,product:Proudct):
        #validation
        success,message =  product.validate()
        if not success:
            return success,message
        
        self.da.update_product(product)
        return True,None

    #Delete
    def delete_product(self,id):
        #validation
        self.da.delete_product(id)