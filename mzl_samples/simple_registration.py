#register
    #ask user information, login (username,password)
    #password must not be emtpy, must be at least 5 length
    #password must be match with confirm password
    #rule validation attempt 3 times

#-- clear screen --

#login
    #ask user login 
    #validate user with username and password
    #rule validation attempt 3 times

#-- clear screen --

#welcome
    #show off user info

import os

print()
print("[ welcome to simple registration system]".upper())

full_name = input("Enter full name: ")
email = input("Enter email: ")
username = input("Enter username: ")

password = input("Enter password: ")

#password validation
invalid_password = password == "" or len(password) < 5
if invalid_password: #2 attempt
    print("Password must not be emtpy, must be at least 5 length. Try Again!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5
if invalid_password: #3 attempt
    print("Password must not be emtpy, must be at least 5 length. Last Attempt!!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5
if invalid_password: #break
    print("Password must not be emtpy, must be at least 5 length. Try re-register later")
    exit()

confirm_password = input("Enter confirm password: ")

#confirm password validation
invalid_confirm_password = confirm_password != password

if invalid_confirm_password: #2 attempt
    print("Password and confirm password do not match. Try Again!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm_password = confirm_password != password
if invalid_confirm_password: #3 attempt
    print("Password and confirm password do not match. Last Attempt!!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm_password = confirm_password != password
if invalid_confirm_password: #break
    print("Password and confirm password do not match. Try re-register later")
    exit()

os.system("cls")
print()
print("Registration successful. Login here!")

login_username = input("Enter username: ")
login_password = input("Enter password: ")

#login validation 
success_login = login_username == username and login_password == password

if not success_login: #2 attempt
    print("Invalid username or password. Try Again!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password
if not success_login: #3 attempt
    print("Invalid username or password. Last Attempt!!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password
if not success_login: #break
    print("Invalid username or password. Try re-register later")
    exit()

#show off
os.system("cls")
print()
print(f"[Welcome {full_name}]")
print()
show_off_message =f"""
Name : {full_name}
Email : {email}
Username : {username}
"""
print(show_off_message)
