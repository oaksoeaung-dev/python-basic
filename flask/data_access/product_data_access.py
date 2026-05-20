import sqlite3
from models.product import Proudct

class ProductDataAccess:
    def __init__(self):
        self.__DATABASE = "appdb.db"

    def __create_connection(self):
        conn = sqlite3.connect(self.__DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    #Create
    def create_product(self, product:Proudct):
        with self.__create_connection() as con:
            con.execute("""
    insert into product 
    (name,price)
    values
    (?,?)""",(product.name,product.price))        
            con.commit() #send to database

    #Retrieve
    def get_products(self) -> list[Proudct]:
        product_list = []
        with self.__create_connection() as con:
            cursor = con.execute("select * from product")
            result = cursor.fetchall()
            for row in result:
                product = Proudct()
                product.map(row)
                product_list.append(product)

        return product_list

    def get_product_by_Id(self,Id):
        with self.__create_connection() as con:
            cursor = con.execute("select * from product where Id = ?",(Id,))
            result = cursor.fetchone()
            product = Proudct()
            product.map(result)
            return product

    #Update
    def update_product(self,product:Proudct):
        with self.__create_connection() as con:
            con.execute(""" 
                        update product 
                        set 
                        name = ?,
                        price = ?
                        where Id = ? """,(product.name,product.price,product.Id))

    #Delete
    def delete_product(self,Id):
        with self.__create_connection() as con:
            con.execute("delete from product where Id = ?",(Id,))