# LIST []
# Lists are ordered collection of itmes,surrounded by square braces [] with comma(,) seperating elements.
# Lists are mutable (can be updated etcc) 

# creating lists
# empty_list = []
# also_empty = list()

numbers =[1,2,3,4,5]
names = ["alice","amar","shiva"]
mixed = [1,"amar",3.14,True]

# UNDERSTANDING INDEXES
# List are zero based indexing,where the first elemsnt is at index 0.

# positive indexing
fruits = ["apple","banana","cat"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# index out of range
# print(fruits[3])

# LIST METHODS
# Add/Update operations

fruits = ["apple","banana","cat"]
fruits.append("dog")
# append : add to end
fruits.insert(1,"orange")
#insert : add at a specific position
more_fruits = ["mango","garpes"]
fruits.extend(more_fruits)
# extend : add multiple items at once
fruits[0]= "pear"
# Direct update by index 
print(fruits)

