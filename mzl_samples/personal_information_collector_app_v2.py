from datetime import datetime
import os

def clear_default():
    os.system("cls")
    print()
    print("personal information collector".upper())
    print()

def ask_name():
    while True:
        name = input("What is your name?: ")
        clear_default()
        if(name == ""):
            print("[ Name cannot be empty! ]")
        elif len(name) > 12:
            print("[ Name cannot be longer than 12 length! ]")
        else:
            return name

def ask_birthday():
    while True:
        birthday = input("What is your birthday? [dd/MM/yyyy]: ")
        clear_default()
        if(birthday == ""):
            print("[ Birthday cannot be empty! ]")
        else:
            return birthday

            
clear_default()
name = ask_name()
birthday = ask_birthday()
address = input("Where are you live in now?: ")
monthly_income = input("How much do you earn monthly? [Int]: ")
year_bonus  = input("How much is your yearly bonus?: ")

birthday_date = datetime.strptime(birthday,"%d/%M/%Y")
age = datetime.now().year - birthday_date.year
yearly_income = int(monthly_income) * 12
tax = (yearly_income * 5) /100

#Name : blah blah
#Birthday : date

personal_information = f"""
Name : {name}
Birthday : {birthday} ({age} years old)
Address : {address}
Monthly Income : {monthly_income}
Yearly Income : {yearly_income}
Tax : {tax}
Gross Income : {yearly_income - tax + int(year_bonus)}
"""
print(personal_information)

print("end".upper())