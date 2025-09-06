hello = 'hello'.upper()
print(hello)

print(hello.lower())

print(hello.capitalize())

# Count number of substrings, case sensitive
print(hello.count('ll')) # => 0, hello: "HELLO"
print(hello.count("LL")) # => 1, hello: "HELLO"

# Method chaining:
print('HELLO WORLD'.lower().count('o'))

# Multiply Operator:
x = "hello"
y = 3
# Even these are different data types, but for strings, * operator can be used to multiply them
print(x * 3) # => hellohellohello

# + Operator: Used to concatenate two strings 
x = "hello"
y = "world"
print(x+y)