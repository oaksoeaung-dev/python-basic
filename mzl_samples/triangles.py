#problem 1

# *
# **
# ***
# ****
# *****

#problem 2
#     *
#    **
#   ***
#  ****
# *****

#problem 3

#     *
#    * *
#  * * * *

#problem 4

#     *
#    ***
#   *****
#  *******
# *********

import os

def ask_rows():
    while True:
        rows = int(input("Give me the rows: "))
        if rows > 15:
            os.system("cls")
            print("[ Rows must be less than 15! ]")
        else:
            return rows


os.system("cls")
rows = ask_rows()
display = ""
star_icon = "*"
space_icon = " "
new_row = "\n"

for row in range(1, rows + 1):
    for star in range(row):
        display += star_icon
    display +=  new_row

print(display)

display = ""
print()

for row in range(1, rows + 1):
    #print(f"row counter : {row} spacing counter {rows-row}")
    for space in range(rows - row):
        display += space_icon
    for star in range(row):
        display += star_icon  
    display +=  new_row

print(display)


display = ""
print()

for row in range(1, rows + 1):
    for space in range(rows - row):
        display += space_icon
    for star in range(row):
        display += "."  
        display += star_icon  
    display +=  new_row

print(display)

display = ""
print()

for row in range(1, rows + 1):
    for space in range(rows - row):
        display += space_icon
    for star in range(1, row * 2):
        display += star_icon  
    display +=  new_row

print(display)
