# Operators: ==, !=, <=, >=, <, >
# Returns Boolean: True or False

x = 'hello'
y = 'hello'

print(x != y) # => False

y = "hello"

print(x == y) # => True
print(x > y)

print('a' > 'Z') # Compares ASCII codes

print(ord('a')) # prints ASCII value of a characters

print(7.0 == 7) # True

# ===================

# Chain Conditions

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

# and, or, not

result4 = result1 or result2 or result3
print(result4)

print(not True) # => False
print(False or True) # => True
print(False and True) # => False
print(True and True) # => True

print(not (False and True)) # => True

## Precendence Order: not, and, or