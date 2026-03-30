from datetime import datetime

print()
print("Personal Information Collector".upper())
name = input("What's your name? ")
birthday = input("What's your birthday? [dd/MM/yyyy] ")
uni = input("Which university are you studying in right now? ")
enroll = input("When did you join your university? [dd/MM/yyyy]")
major = input("What's your major?  ")
eng =int( input("Enter your English score : "))
math = int(input("Enter your Mathematics score : "))
os = int( input("Enter your Operating System score : "))
cs = int(input("Enter your Control System score : "))
acn = int(input("Enter your Auto Control Networks score : "))
cao = int(input("Enter your Computer Architecture score : "))
admt = int(input("Enter your ADMT score : "))

bd_date = datetime.strptime(birthday,"%d/%m/%Y")
age = datetime.now().year - bd_date.year
enroll_date = datetime.strptime(enroll,"%d/%m/%Y")
year = datetime.now().year - enroll_date.year
average = (eng + math + os + cs + acn + cao + admt)/7
gpa = average/25

student_information =f""" 
Name : {name}
Birthday : {birthday} ({age}years old)
University : {uni}
EntryDate : {enroll}({year}th year)
Eng Score :{eng}
Math Score :{math}
OS Score :{os}
CS Score : {cs}
ACN Score : {acn}
CAO Score : {cao}
ADMT Score : {admt}
Average Score : {average}
GPA : {gpa}

"""
print(student_information)
print("end".upper( ))
