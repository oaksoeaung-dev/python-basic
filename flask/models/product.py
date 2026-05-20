class Proudct:
    def __init__(self, name = "" , price = 0):
        self.Id = 0
        self.name = name
        self.price = price

    def validate(self):
        if(self.name == ""):
            return False,"Product name cannot be empty."
        
        if(self.price <= 0 ):
            return False,"Product price cannot be zero or negative value."
        
        return True,None
    
    def map(self,cursor_row):
        self.Id = cursor_row["id"]
        self.name = cursor_row["name"]
        self.price = cursor_row["price"]
    