class Animal():
  def eat(self):
    print("Animal is eating")

  def sleep(self):
    print("Animal is sleeping")

class Dog(Animal):
  pass

class Cat(Animal):
  pass

dog = Dog()
dog.eat()
dog.sleep()

cat = Cat()
cat.eat()
cat.sleep()
