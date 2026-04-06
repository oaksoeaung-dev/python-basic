
from math_tool.math_helper import add
from math_tool.math_helper import multiply

#class creation
class Person:

    #constructor => intial
    def __init__(self): #default function called initially when object is created
        print("I am created!")

    #function
    def greet(self, name): # self is default parameter for instance
        print(f"Hello {name}!")
    
    #destructor => delete
    def __del__(self):
        print("I am deleted!")


#object creation
person = Person()

#del person

#print(person)
person.greet("MZL")

print(f"Add : {add(1,2)}, Multiply : {multiply(1,2)}")