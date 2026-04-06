class Animal:
    def __init__(self, type_name):
        print(f"\n{type_name}")
        self._type_name = type_name

    def eat(self):
        print(f"{self._type_name} is Eating..")

    def sleep(self):
        print(f"{self._type_name} is Sleeping..")

animal = Animal("Animal")
animal.eat()
animal.sleep()

#inherit (dog is-a Animal)
class Dog(Animal):
    def eat(self): #polymorphism
        print(f"{self._type_name} is Eating in Dog form.")

    def sleep(self): #polymorphism
        print(f"{self._type_name} is Sleeping in Dog form.")
    
    def make_sound(self): #polymorphism
        print("Wook Wook")

dog = Dog("Dog")
dog.eat()
dog.sleep()

#inherit (cat is-a Animal)
class Cat(Animal):
    def eat(self): #polymorphism
        print(f"{self._type_name} is Eating in Cat form.")

    def sleep(self): #polymorphism
        print(f"{self._type_name} is Sleeping in Cat form.")

    def make_sound(self): #polymorphism
        print("Meow Meow")

cat = Cat("Cat")
cat.eat()
cat.sleep()

print()

animal_list = [Dog("Dog"),Cat("Cat")]
for _animal in animal_list:
    _animal.make_sound() #abstraction

