class Cart:
    def __init__(self):
        self.__max_storage = 5
        self.__products = []
    
    def add_product(self,product):
        if self.__max_storage == 0:
            print("No space left.")
            return

        self.__products.append(product)
        self.__max_storage -= 1

    def move(self):
        print("Cart is moving")

    def display_products(self):
        for product in self.__products:
            print(product)