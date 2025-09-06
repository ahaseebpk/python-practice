hello = 'hello'.upper()
print(hello)

print(hello.lower())

print(hello.capitalize())

# Count number of substrings, case sensitive
print(hello.count('ll')) # => 0, hello: "HELLO"
print(hello.count("LL")) # => 1, hello: "HELLO"

# Method chaining:
print('HELLO WORLD'.lower().count('o'))