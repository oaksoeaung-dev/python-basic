class Animal():
  def __init__(self, name):
    self._name = name

  def eat(self):
    print("Animal is eating")

  def sleep(self):
    print("Animal is sleeping")

class Dog(Animal):
  def eat(self):
    print(f"{self._name} is eating in dog form.")

class Cat(Animal):
  def eat(self):
    print(f"{self._name} is eating in cat form.")

  def eat(self):
    print(f"{self._name} is sleeping in cat form.")

  def makeSound(self):
    print(f"{self._name} said Meow Meow.")

dog = Dog("Dog")
dog.eat()
dog.sleep() # Dog class မှာ sleep ကို morph မလုပ်ထားတဲ့အတွက် parent class ကအတိုင်းပဲရလာတယ်။

cat = Cat("Cat")
cat.eat()
cat.sleep()
cat.makeSound()