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

def ask_uni():
  while True:
    uni = input("Which university are you studying in right now? ")
    if (uni == ""):
      print("University cannot be empty!")
    else:
      return uni

def ask_enroll():
  while True:
    enroll = input("When did you join your university?[dd/MM/yyyy]   ")
    if (enroll == ""):
      print("Enroll date cannot be empty!")
    else:
      return enroll

def ask_major():
  while True:
    major = input("What is your major? ")
    if (major == ""):
      print("Major cannot be empty!")
    else:
      return major

def ask_eng():
  while True:
    eng = input("What is your English Score?")
    if eng == "" :
      print("Score cannot be empty!")
    elif int(eng) < 0 :
      print("Score must be positive integer!")
    elif int(eng) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(eng)

def ask_math():
  while True:
    math = input("What is your Mathematics Score?")
    if math == "" :
      print("Score cannot be empty!")
    elif int(math) < 0:
      print("Score must be positive integer!")
    elif int(math) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(math)

def ask_ops():
  while True:
    ops = input("What is your Operation System Score?")
    if os == "" :
      print("Score cannot be empty!")
    elif int(ops) < 0:
      print("Score must be positive interger!")
    elif int(ops) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(ops)

def ask_cns():
  while True:
    cns = input("What is your Control System Score?")
    if cns == "" :
      print("Score cannot be empty!")
    elif int(cns) < 0:
      print("Score must be positive interger!")
    elif int(cns) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(cns)

def ask_acn():
  while True:
    acn = input("What is your Advanced Control Network Score?")
    if acn == "" :
      print("Score cannot be empty!")
    elif int(acn) < 0:
      print("Score must be positive interger!")
    elif int(acn) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(acn)

def ask_cao():
  while True:
    cao = input("What is your Computer Architecture Score?")
    if cao == "" :
      print("Score cannot be empty!")
    elif int(cao) < 0:
      print("Score must be positive interger!")
    elif int(cao) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(cao)

def ask_admt():
  while True:
    admt = input("What is your ADMT Score?")
    if admt == "" :
      print("Score cannot be empty!")
    elif int(admt) < 0:
      print("Score must be positive interger!")
    elif int(admt) > 100:
      print("Score must not be larger than 100!")
    else:
      return int(admt)

name = ask_name()
birthday = ask_birthday()
uni = ask_uni()
enroll = ask_enroll()
major = ask_major()
eng =ask_eng()
math = ask_math()
ops = ask_ops()
cns = ask_cns()
acn = ask_acn()
cao = ask_cao()
admt = ask_admt()
os.system("cls")
print()
print("Personal Information Collector".upper())

bd_date = datetime.strptime(birthday,"%d/%m/%Y")
age = datetime.now().year - bd_date.year
enroll_date = datetime.strptime(enroll,"%d/%m/%Y")
year = datetime.now().year - enroll_date.year
average = (eng + math + ops + cns + acn + cao + admt)/7
gpa = average/25

student_information =f""" 
Name : {name}
Birthday : {birthday} ({age}years old)
University : {uni}
EntryDate : {enroll}({year}th year)
Major : {major}
Eng Score :{eng}
Math Score :{math}
OS Score :{ops}
CS Score : {cns}
ACN Score : {acn}
CAO Score : {cao}
ADMT Score : {admt}
Average Score : {average}
GPA : {gpa}

"""
print(student_information)
print("end".upper( ))
