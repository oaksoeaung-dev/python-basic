#LIST Manipulation

#C = > Create 
numbers = [1,2,3,4,5] #(Ordered)

#Create => append => Create item => Append to the last
numbers.append(6)
numbers.append(7)

#Create => insert => index base
numbers.insert(0,0)

#R = Retrieve => Read
print(numbers)

#U Update 
numbers[0] = 10
print(numbers)

#D Delete
#remove => exact item
numbers.remove(10)
print(numbers)

#pop => remove from the last
numbers.pop()
numbers.pop(3) #index
print(numbers)

#reverse
numbers.reverse()
print(numbers)

#reset 
numbers = []
numbers.clear()
print(numbers)