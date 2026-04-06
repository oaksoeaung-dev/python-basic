#hash - set => no duplicate
#Immutable
#Create
numbers = {1,1,2,2,3,3,4,5} #(Unorder)
numbers.add(6)
numbers.add(6)
numbers.add(6)

#Retrieve
for number in numbers:
    print(number)
print(numbers)

#D = Delete 
#remove
numbers.remove(6)
print(numbers)

#pop
numbers.pop()
print(numbers)

#discard
numbers.discard(2)
print(numbers)

#reset 
#numbers = {}
numbers.clear()
print(numbers)

