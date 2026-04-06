# a customer who have money
# he will go to market
# he will carry a cart
# he will by a products
# he will go back to home

# a cart has a capacity which can store 5 product =>Property
# can add a product => Function
# which has a carrier => Function

from customer import Customer

customer = Customer()
customer.go_market()
customer.buy_a_product("Apple",1000)
customer.buy_a_product("Mango",2000)
customer.buy_a_product("Oragne",3000)

customer.go_back_home()