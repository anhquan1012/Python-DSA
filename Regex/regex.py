# %%
import re

# %%
# find_all() function return a list containing all matches
# The matches in list returned in the order ther are found
# If no matches are found, an empty list is returned
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# %%
# search() function searches string for a match, returns a Match object (or None)
# Only the first occurence of the match is returned
txt = "The rain in Spain rain"
x = re.search("rain", txt)

print("The span of the match: ", x.span())
print("The start position of the match: ", x.start())
print("The end position of the match: ", x.end())
print("The string: ", x.string)
print("The searched match: ", x.group())
#%%
# split() returns a list where the string has been split at each match
# Use maxsplit to control the number of times of splitting
txt = "The rain in Spain"
x = re.split("\s", txt, maxsplit=2)
x
#%%
# sub() function replaces the matches with the text of your choice
# Control the number of replacement by count
txt = "The rain in Spain rain rain"
x = re.sub("rain", "9", txt, count=2)
x

#%%
# compile() is used to precompile a regular expression pattern into a regular expression object
# fullmatch() matches the entire string against the pattern
# match() matches the pattern only at the beginning of the string
pattern = re.compile('this is a really cool string really!')
d = pattern.fullmatch('this is a really cool string really!')
e = pattern.fullmatch('this is a really cool string really really!')    # this should be exact match, otherwise returns none

pattern = re.compile('really')
f = pattern.match('really cool feature')    # it starts matching from the first character otherwise returns none
g = pattern.match('yo really')

print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")

