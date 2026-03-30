import os
from datetime import datetime

def ask_name():
  while True:
    name = input("What is your name? ")
    if (name == ""):
      print("Name cannot be empty!")
    else:
      return name

def ask_birthday():
  while True:
    birthday = input("What's your birthday? [dd/MM/yyyy] ")
    if (birthday == ""):
      print("Birthday cannot be empty!")
    else:
      return birthday

def ask_address():
  while True:
    address = input("What is your address?  ")
    if (address == ""):
      print("Address cannot be empty!")
    else:
      return address
      
def ask_myanmar():
  while True:
    myanmar = input("What is your Myanamr Score?")
    if myanmar == "" :
      print("Score cannot be empty!")
    elif int(myanmar) < 0 :
      print("Score must be positive integer!")
    elif int(myanmar) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(myanmar)

def ask_eng():
  while True:
    eng= input("What is your English Score?")
    if eng== "" :
      print("Score cannot be empty!")
    elif int(eng) < 0:
      print("Score must be positive integer!")
    elif int(eng) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(eng)

def ask_maths():
  while True:
    maths = input("What is your Mathematics Score?")
    if maths == "" :
      print("Score cannot be empty!")
    elif int(maths) < 0:
      print("Score must be positive interger!")
    elif int(maths) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(maths)

def ask_science():
  while True:
    science = input("What is your Science Score?")
    if science == "" :
      print("Score cannot be empty!")
    elif int(science) < 0:
      print("Score must be positive interger!")
    elif int(science) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(science)

name = ask_name()
birthday = ask_birthday()
address =ask_address()
myanmar = ask_myanmar()
eng = ask_eng()
maths = ask_maths()
science = ask_science()
os.system("cls")   

print()
print("Student Information Collector".upper())
birthday_date = datetime.strptime(birthday,"%d/%m/%Y")
age = datetime.now().year - birthday_date.year

total_marks = myanmar + english + maths + science
average_marks = total_marks / 4

personal_information = f"""
Name        : {name}
Birthday    : {birthday} ({age} years old)
Address     : {address}

Myanmar     : {myanmar}
English     : {english}
Maths       : {maths}
Science     : {science}

Total Marks : {total_marks}
Average     : {average_marks:.2f}
"""

print(personal_information)
print("End".upper())