class Student:
  def __init__(self, name):
    self.name = name
    self.__age = 0

  def get__age(self):
    return self.__age

  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self, age):
    if 1 <= age <= 18:
      self.__age = age
    else:
      print("Age must be between 1 and 18.")

mgmg = Student("Mg Mg")
mgmg.age = 10
print(mgmg.age)