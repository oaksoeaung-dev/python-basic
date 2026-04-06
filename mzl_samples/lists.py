#list, array, collection

#nameList = ["STD001","STD002",1,2,3,True,"STD005",False]

#print(len(nameList)) #size

# #accessor
# print(nameList[0])

# #update
# nameList[0] = "STD004"
# print(nameList[7])
# print(nameList)

# #iteration
# for name in nameList:
#     print(name)

# #while
# size = len(nameList)
# index = 0
# while index < size:
#     print(nameList[index])
#     index += 1

#first and last
#print(f"First Value: {nameList[0]}, Last Value: {nameList[-1]}")

# #concanate
# students = ["S1","S2"]
# numbers = [1,2,3,4]

# concanation = students + numbers
# print(concanation)


#Tuple

nameList = ("Mg Mg","Aung Aung","Ko Ko")
# print(nameList)

# print(nameList[0])
# print(nameList[-1])

# #loop
# for name in nameList:
#     print(name)

# #Immutable state
# nameList[0] = "Kyaw Kyaw"

#Unpack
# mgmg = nameList[0]
# aung_aung = nameList[1]
# ko_ko = nameList[2]

(aung_aung, mgmg,_) = nameList #discard

print(f"{mgmg} {aung_aung}")