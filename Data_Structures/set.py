# Store non-dupliate items
# Very fast access vs list
# Math set ops (union, intersect)
# Set is unordered

#%%
# Create new set
x = {3,5,10,1}
y = set([1,2,3])
print(x)
print(y)

#%%
## Add
x = {3,5,10,1}
x.add(7)
print(x)
## Remove
x.remove(7)
print(x)
## Check membership
print(7 in x)
print(10 in x)
## Pop: pop random item from set
print(x.pop())
print(x)
## Clear: remove all items from set
x.clear()
print(x)


#%%
# Math operations
s1 = {3,1,2}
s2 = {4,2,3,50}
## Intersection
print(s1 & s2)
## Union
print(s1 | s2)
## Symmetric difference
print(s1 ^ s2)
## Difference: in s1 but not in s2
print(s1 - s2)
## Subset
print(s1 <= s2)
## Superset
print(s1 >= s2)
