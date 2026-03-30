from datetime import datetime

print()
print("Student Information Collector".upper())

name = input("Student name: ")
birthday = input("Date of birth (dd/MM/yyyy): ")
address = input("Current address: ")
myanmar = int(input("Myanmar mark: "))
english = int(input("English mark: "))
math = int(input("Math mark: "))
science = int(input("Science mark: "))
birthday_date = datetime.strptime(birthday,"%d/%m/%Y")
age = datetime.now().year - birthday_date.year

total_marks = myanmar + english + math + science
average_marks = total_marks / 4

personal_information = f"""
Name        : {name}
Birthday    : {birthday} ({age} years old)
Address     : {address}

Myanmar     : {myanmar}
English     : {english}
Math        : {math}
Science     : {science}

Total Marks : {total_marks}
Average     : {average_marks:.2f}
"""

print(personal_information)
print("End".upper())