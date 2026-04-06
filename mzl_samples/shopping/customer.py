from cart import Cart

class Customer:
    def __init__(self):
        self.__cart = Cart()
        self.__total_cash = 5000

    def go_market(self):
        print("Going to market.")

    def buy_a_product(self,product,price):
        self.__cart.add_product(product)
        self.__total_cash -= price

    def go_back_home(self):
        print("Going back home.")

    def check_products(self):
        self.__cart.display_products()