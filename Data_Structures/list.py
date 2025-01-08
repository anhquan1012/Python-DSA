# General purpose
# Most widely used data structure
# Grow and shrink size as needed
# Sequence type
# Sortable

#%%
# Creating new list
mylist = ["a", 25, "apple", 2.8]
tuple1 = (10,20)
list1 = list(tuple1)
print(mylist)
print(list1)
print(type(list1))

# %%
# Methods
x = [1,2,3,4]
## Append
x.append(5)
print(x)
## Delete
del x[2] # Del an element
print(x)
del x # Del entire list
# print(x) -> error: 'x' is not defined
## Extend: append a sequence to a list
x = [1,2,3,2]
y = ['a','b']
x.extend(y)
print(x)
## Insert: insert an item at a given index
x.insert(1, "c")
print(x)
## Pop: pop last element and return it
print(x.pop())
print(x)
## Remove: remove first instance of an element
x.remove(2)
print(x)
## Reverse: in-place reverse the order of the list
x.reverse()
print(x)
## Sort
x = [5,2,4,1,3]
y=sorted(x) # creating a new sorted list
print(x)
print(y)
x.sort() # in-place sorting
print(x)
## Reverse sort
x = [5,2,4,1,3]
y=sorted(x, reverse=True) # creating a new sorted list
print(x)
print(y)
x.sort(reverse=True) # in-place sorting
print(x)

#%%
import random
#%%
# List Comprehensions
## Get values in a range
under_10 = [x for x in range(10)]
print("Under 10: ", under_10)
## Get squared values
squares = [x**2 for x in under_10]
print("Squares: ", squares)
## Get odd numbers
odd = [x for x in under_10 if x%2==1]
print("Odd: ", odd)
## Get all numbers from a text
text = "from 0 to 2 and from 3 to 9"
numbers = [x for x in text if x.isnumeric()]
print(f"Numbers in string '{text}' is {numbers}")
## If-else in a comprehension
nums = [5,8,2,5,9,10]
new_nums = [x if x%2==0 else x*10 for x in nums]
print(new_nums)
## Nested loop for 2D list
li = [[1,2],[3,4]]
new_list = [x for li_ in li for x in li_]
print(new_list)
