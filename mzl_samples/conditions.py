val = 20

if val % 2 == 0 : #target
    print("Divided by 2")   
elif val % 3 == 0 : #target
    print("Divided by 3")

if val % 4 == 0 : #target
    print("Divided by 4")

if val % 5 == 0 : #target
    print("Divided by 5")
elif val % 6 == 0 : #target
    print("Divided by 6")
else: #default
    print("It's just number")

x = 10
if x > 5:
    print("x is greather than 5.")
    if x % 2 == 0: #nested if
        print("x can divided by 2")
    else:
        print("x cannot divided by 2")
else:
    print("x is not greater than 5")

#print("END") #not related with if statement