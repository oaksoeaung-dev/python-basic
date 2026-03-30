import os

print()
print("welcome to bank registration system".upper())

name = input("Enter your name :")
phone = input ("Enter your Phone Number: ")
email = input ("Enter your Email Address :")
if "@" not in email and ".com" not in email:
  print("Email must contain '@' and '.com'.Try Again.")
  email = input ("Enter your Email Address :")
if "@" not in email and ".com" not in email:
  print("Email must contain '@' and '.com'.Try Again")
  email = input ("Enter your Email Address :")
if "@" not in email and ".com" not in email:
  print("Email must contain '@' and '.com'.Try Again Later.")
  exit()
pin = input("Enter your PIN number :")
invalid_pin = pin =="" or  len(pin)<6
if invalid_pin :
  print("PIN number must have atleast 6 digits! Try Again.")
  pin = input("Enter your PIN number :")
  invalid_pin = pin =="" or  len(pin)<6
if invalid_pin :
  print("PIN number must have atleast 6 digits!Try Again.")
  pin = input("Enter your PIN number :")
  invalid_pin = pin =="" or  len(pin)<6
if invalid_pin:
  print("PIN number must have atleast 6 digits !Try again later.")
  exit()

confirm_pin = input("Confirm your PIN number :")
invalid_confirm_pin = confirm_pin != pin
if invalid_confirm_pin:
  print("Confirmation failed.PIN numbers do not match.Try Again!")
  confirm_pin = input("Confirm your PIN number :")
  invalid_confirm_pin = confirm_pin != pin
if invalid_confirm_pin:
  print("Confirmation failed.PIN numbers do not match.Try Again!")
  confirm_pin = input("Confirm your PIN number :")
  invalid_confirm_pin = confirm_pin != pin
if invalid_confirm_pin:
  print("Confirmation failed.PIN numbers do not match.Try Again Later.")
  exit()
os.system("cls")

print()
print("registration completed.Login your bank account".upper())
login_phone =input("Enter phone number:")
login_email = input("Enter Email: ")
login_pin = input("Enter PIN :")

error1 = login_phone != phone 
error2 = login_email != email
error3 = login_pin != pin
error_login = error1 or error2 or error3
if error_login :
  print("Login Failed!.Try Again")
  if error1:
    print("Incorrect phone number.")
  if error2:
    print("Incorrect email.")
  if error3:
    print("Incorrect pin.")
  login_phone =input("Enter phone number:")
  login_email = input("Enter Email: ")
  login_pin = input("Enter PIN :")

  error1 = login_phone != phone 
  error2 = login_email != email
  error3 = login_pin != pin
  error_login = error1 or error2 or error3
if error_login :
  print("Login Failed!.Try Again")
  if error1:
    print("Incorrect phone number.")
  if error2:
    print("Incorrect email.")
  if error3:
    print("Incorrect pin.")
  login_phone =input("Enter phone number:")
  login_email = input("Enter Email: ")
  login_pin = input("Enter PIN :")

  error1 = login_phone != phone 
  error2 = login_email != email
  error3 = login_pin != pin
  error_login = error1 or error2 or error3
if error_login:
  print("Login Failed!.Try Again Later")
  if error1:
    print("Incorrect phone number.")
  if error2:
    print("Incorrect email.")
  if error3:
    print("Incorrect pin.")
  exit()

os.system("cls")
print()
print(f"LogIn Successful!WELCOME {name}")
print()
message = f"""
Name : {name}
Phone Number : {phone}
Email Address : {email}
Balance : $2500
"""
print(message)



  

  
  
