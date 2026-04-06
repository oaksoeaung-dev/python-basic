from datetime import datetime

print()
print("personal information collector".upper())
name = input("What is your name?: ")
birthday = input("What is your birthday? [dd/MM/yyyy]: ")
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