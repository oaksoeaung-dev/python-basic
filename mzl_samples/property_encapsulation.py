#class
class Human:
    def __init__(self):
        #encapsulated
        self.__left_hand = "left hand"
        self.__right_hand = "right hand"
    
    #function property
    def get_left_hand(self):
        return self.__left_hand

    def get_righ_hand(self):
        return self.__left_hand

class Car:
    def __init__(self):
        #backing fields
        self.__left_wheel = "left wheel"
        self.__right_wheel = "right wheel"
        self.__brake = "Car Brake"
        self.streering = "Car streering"
    
    #function property getter
    def get_left_wheel(self):
        return self.__left_wheel

    #setter
    def set_left_wheel(self, wheel):
        self.__left_wheel = wheel

    #getter
    def get_right_wheel(self):
        return self.__right_wheel

    #setter
    def set_righ_wheel(self, wheel):
        if(wheel == "" or len(wheel)>10):
            print("wheel cannot be empty or longer than 10.")
            return
        self.__right_wheel = wheel

    #decorator property
    @property
    def brake(self):        
        return self.__brake
    
    @brake.setter
    def brake(self,car_brake):
        if(car_brake != ""):
            self.__brake = car_brake


human = Human()
car = Car()

#getter
print(f"Human fields [left:{human.get_left_hand()} rigth:{human.get_righ_hand()}]")
print()
print(f"Car fields [left:{car.get_left_wheel()} rigth:{car.get_right_wheel()} \n brake:{car.brake} streering:{car.streering}]")

#setter

car.set_left_wheel("new left wheel")
car.set_righ_wheel("new right wheel")
car.brake = "AAAA"
car.streering = ""

print(f"Human fields [left:{human.get_left_hand()} rigth:{human.get_righ_hand()}]")
print()
print(f"Car fields [left:{car.get_left_wheel()} rigth:{car.get_right_wheel()}]  \nbrake:{car.brake} streering:{car.streering}]")