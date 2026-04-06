# #while loop
# #increment
# counter = 0
# while counter < 5:
#     print("hello")
#     counter += 1

# #decrements
# counter = 5
# while counter != 0:
#     print("hello")
#     counter -= 1

# #infinite loop
# while True: 
#     print("Hey, I can't stop") # Ctrl+C to stop

# password = ""
# while password != "12345":
#     password = input("Enter password :")

# print("Login success")


# #for loop
# for step in range(5): # default start from 0, default increment 1
#     print("Hello world")

# #intial >=, exit <
# for counter in range(1,6): #control initial piont
#     print(counter)

# for counter in range(5, 10, 5): # control inital piont and increment
#     print(counter)

# #for loop in array

# names  = ["A","B","C"]
# for name in names:
#     print(name)

counter = 0
while True:
    counter += 1

    if counter % 2 == 0:
        continue

    print(f"Counter is now {counter}")

    if counter >= 20:
        break

# for counter in range(100):
#     print(f"Counter is now {counter}")
#     if counter == 10:
#         break