# Assign numbers to variables, add them together using "+" operator and save them in a variable
x = 9
y = 3
result = x + y
print(result)

# You can't add a string and a number, it will raise an error
# Like, "Hello" + 9

# Float numbers can also be added to integers

print(3.5 + 4)

# Practice other like operators like -, *, /

# / (division) operator by default returns floating point, even if division is between integers

print(9/3)

# If you want a whole number as an output, you can convert it to int before saving or printing

print(int(9/3))

## Exponent:

x = 3
y = 9
result = y ** x
print(result)

## Floor Division: Returns the integer part of division's result

x = 7
y = 3
result = x // y
print(result)

## Mod: Remainder after division

x = 10
y = 3
result = x % y
print(result)

## Order of operators: BEDMAS

## Input: Eventhough if you type number in input, it will store it as a string. 
## Thus, that string will need to be converted to a number for calculations

# This will raise error
# num = input('Number: ')
# print(num - 5)

num = input('Number: ')
print(int(num) - 5)

## We can also convert to float:
print(float(num) - 5)