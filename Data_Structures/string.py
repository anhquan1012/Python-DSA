#%%
# Strings are surrounded by either single quotes or double quotes
a = 'hello'
b = "Hello"
print(a)
print(b)
#%%
# We can use quotes inside a string, as long as they don't match the quotes surrounding the string
c = "hello 'Paul'"
d = 'hello "Paul"'
print(c, d)
# %%
# Multiple lines. We can use three double quotes or three single quotes
aa = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
bb = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(aa)
print("----")
print(bb)
#%%
# String is an array
text = "Hello World!"
## Get character by index
print(text[3])
## Loop through the string
for c in text:
    print(c, end=" ")
## Get length of the string
print(len(text))
## Check if a string in another string
print("hello" in text)
#%%
# Slice a string
text = "Hello World!"
## From start index to end index
print(text[:6])
## From start to end index
print(text[:3])
## From start index to end
print(text[2:])
## Use negative index to start from the end
print(text[-5:-1])
# %%
# Concatenate
a = "Hello"
b = "World"
c = a + " " + b
c
# %%
# Placeholder and modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# %%
# Some methods
## Upper case
text = "Hello, World!"
print(text.upper())
## Lower case
print(text.lower())
## Remove white space from the beginning and the end
text = "     Hello, World!   "
print(text.strip())
## Replace 
print(text.replace("l", "i"))
## Split: return a list where the texts between the specified seperator becomes items
print(text.split(","))
