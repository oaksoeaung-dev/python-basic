import os

print()
print("[ welcome to simple registration system]".upper())

full_name = input("Enter full name: ")
email = input("Enter email: ")
username = input("Enter username: ")

password = input("Enter password: ")

invalid_password = password == "" or len(password) < 5

if invalid_password:
    print("Password must not be empty, at least 5 characters. Try Again!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5

if invalid_password:
    print("Password must not be empty, at least 5 characters. Try Again!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5

if invalid_password:
    print("Password must not be empty, at least 5 characters. Try Again!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5

if invalid_password: 
    print("Password must not be empty, at least 5 characters. Last Attempt!!")
    password = input("Enter password: ")
    invalid_password = password == "" or len(password) < 5

if invalid_password:
    print("Password invalid. Try re-register later")
    exit()

confirm_password = input("Enter confirm password: ")

invalid_confirm = confirm_password != password

if invalid_confirm: 
    print("Passwords do not match. Try Again!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm = confirm_password != password

if invalid_confirm: 
    print("Passwords do not match. Try Again!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm = confirm_password != password

if invalid_confirm: 
    print("Passwords do not match. Try Again!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm = confirm_password != password

if invalid_confirm: 
    print("Passwords do not match. Last Attempt!!")
    confirm_password = input("Enter confirm password: ")
    invalid_confirm = confirm_password != password

if invalid_confirm:
    print("Password mismatch. Try re-register later")
    exit()


os.system("cls")
print()
print("Registration successful. Login here!")

login_username = input("Enter username: ")
login_password = input("Enter password: ")

success_login = login_username == username and login_password == password

if not success_login:
    print("Invalid username or password. Try Again!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password

if not success_login:
    print("Invalid username or password. Try Again!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password

if not success_login:
    print("Invalid username or password. Try Again!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password

if not success_login: 
    print("Invalid username or password. Last Attempt!!")
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    success_login = login_username == username and login_password == password

if not success_login:
    print("Invalid login. Try re-register later")
    exit()

os.system("cls")

print()
print(f"[Welcome {full_name}]")
print(f"""
Name : {full_name}
Email : {email}
Username : {username}
""")