x = [4, True, 'hi']

print(len(x), len('y')) # => length of a list, also works on Strings

x.append('hello') # Adds element
print(x)

print(x.pop()) # Removes  element, last element if no arguments passed
print(x)

print(x.pop(1)) # pass index to remove element at a particular index, list index starts from 0
print(x)
 
 # Access elements with subscript operator [], type index in it.

print(x[0])

x[0] = 'hello'
print(x[0])
print(x)

y = x # It doesn't copy the list!!! it copies list's address
y[0] = 'bye'
print(y[0] == x[0]) # True, x changed too
print(y)

# For copying a list
z = x[:]
z[0] = 12345
print(z)
print(x)
print(z[0] == x[0]) # False

## Tupple, same like lists
## However, it can't be changed. That's why, it is immutable
## Defined with small brackets (), unlike lists []

x = (0, 0, 2, 2)
#x[0] = 5 # ERROR
print(x[0])

## Nesting
# You can have list inside list: x = [[], [], []]
# Tupple inside Tupple: x = ((), (), ())
# Or, you can mix them: x = [(), [], (), []]