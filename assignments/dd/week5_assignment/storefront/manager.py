import os
from product import Product 

class StoreManager:
    def __init__(self):
        self.product_list = [
            Product("Apple", 100),
            Product("Orange", 80)
        ]

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def is_empty(self, value):
        return value.strip() == ""

    def create_product(self):
        name = input("Name : ")
        price = input("Price : ")

        if self.is_empty(name) or self.is_empty(price):
            return "Creation failed! Empty input."
        
        if not price.isdigit():
            return "Creation failed! Price must be a number."

        new_product = Product(name, int(price))
        self.product_list.append(new_product)
        return "Product has been created successfully."

    def retrieve_products(self):
        if not self.product_list:
            return "No products found to display."
        
        print("\n--- INVENTORY LIST ---")
        for index, product in enumerate(self.product_list):
            print(f"[{index}] {product}")
        print("----------------------")
        
        input("\nPress Enter to return to menu...")
        return "Inventory viewed successfully."

    def update_product(self):
        if not self.product_list:
            return "No products available to update."

        try:
            index = int(input("Enter index to update: "))
            if 0 <= index < len(self.product_list):
                name = input("New Name : ")
                price = input("New Price : ")

                if self.is_empty(name) or self.is_empty(price):
                    return "Update failed! Inputs cannot be empty."
                
                if not price.isdigit():
                    return "Update failed! Price must be a number."

                self.product_list[index].name = name
                self.product_list[index].price = int(price)
                return "Updated product successfully!"
            else:
                return "Invalid index!"
        except ValueError:
            return "Invalid input! Please enter a number for index."

    def delete_product(self):
        if not self.product_list:
            return "No products to delete."
        
        try:
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(self.product_list):
                self.product_list.pop(index)
                return "Deleted product successfully."
            else:
                return "Product not found (Invalid index)."
        except ValueError:
            return "Invalid input! Please enter a number."

    def run(self):
        message = ""
        while True:
            self.clear_screen()
            print("=== STORE FRONT (OOP VERSION) ===")
            if message:
                print(f"\nSystem Message: {message}")
                message = ""
            
            print("""
    [1] Create
    [2] Retrieve
    [3] Update
    [4] Delete
    [5] Exit
            """)
            
            choice = input("Select Menu : ")
            
            if choice == "1":
                message = self.create_product()
            elif choice == "2":
                message = self.retrieve_products()
            elif choice == "3":
                message = self.update_product()
            elif choice == "4":
                message = self.delete_product()
            elif choice == "5":
                self.clear_screen()
                print("Exiting program... Bye Bye!")
                break
            else:
                message = "Invalid option. Please try again."