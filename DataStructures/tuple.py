# Immutable (cannoot add/change)
# Useful for fixed data
# Faster than  lists
# Sequence type

#%%
# Creating new tuple
x = (1,2,3)
y = 1,2,3
z = 1,
print(x)
print(y)
print(z)

#%%
# Tuple is immutable, but member objects of tuple may be mutable
tp = ([1,2], 1, 2)
# del tp[0] -> fail
# tp[1] = 2  -> fail
tp[0][0] = 2
print(tp)

#%%
# Concatenate 2 tuples
x = (1,2,3)
x += 4,
print(x)
