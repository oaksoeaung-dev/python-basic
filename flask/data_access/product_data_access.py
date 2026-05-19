import sqlite3

DATABASE = "appdb.db"

def create_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

#Create
def create_product(name,price):
    with create_connection() as con:
        con.execute("""
insert into product 
(name,price)
values
(?,?)""",(name,price))        
        con.commit() #send to database

#Retrieve
def get_products():
    #products = []
    with create_connection() as con:
        cursor = con.execute("select * from product")
        return cursor.fetchall()
        # result = cursor.fetchall()
        # for row in result:
        #     products.append({"id":row["Id"],"name":row["name"],"price":row["price"]})

    #return products

def get_product_by_Id(Id):
    with create_connection() as con:
        cursor = con.execute("select * from product where Id = ?",(Id,))
        return cursor.fetchone()

#Update
def update_product(Id,name,price):
    with create_connection() as con:
        con.execute(""" 
                    update product 
                    set 
                    name = ?,
                    price = ?
                    where Id = ? """,(name,price,Id))

#Delete
def delete_product(Id):
    with create_connection() as con:
        con.execute("delete from product where Id = ?",(Id,))