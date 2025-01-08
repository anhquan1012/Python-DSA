# Key/value pairs
# From Python 3.7, dict is ordered

#%%
# Create new dict
x = {'a': 1, "b": '2', "c": 3.}
print(x)
x = dict([('a', 1), ('b', '2'), ('c', 3.)])
print(x)
x = dict(a=1, b='2', c=3.)
print(x)

#%%
# Dict operations
## Add or update
x['d'] = "hello"
print(x)
## Delete an item
del x['d']
print(x)
## Get length
print(len(x))
## Clear
x.clear()
print(x)
## Delete dict
del x
# print(x) -> Error

#%%
# Access keys and values in dict
x = {'chicken': 2, 'pork': 3, 'beef': 1}
print(x.keys())
print(x.values())
print(x.items())
# Check member in dict (dick keys)
print('beef' in x)
print('monkey' in x.keys())
# Check member in values
print(2 in x.values())

#%%
# Iterate a dict
for key in x:
    print(key, x[key])

for key, value in x.items():
    print(key, value)
    