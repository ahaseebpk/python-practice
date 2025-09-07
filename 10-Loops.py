# range() is a function that returns range of values
# range(stop): until a specific number
# range(start, stop): start from a particular number and stop before the second number
# range(start, stop): same but provide how much to step (unlike 1)

for i in range(10):
    print(i)

print('=======')

for i in range(3, 5):
    print(i)

print('=======')

for i in range(4, 20, 2):
    print(i)

print('=======')

## Outputs:

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# =======
# 3
# 4
# =======
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# =======

# A range simpy returns a list, so, you can directly use a list

for i in [7,1,7,0]:
    print(i)

# Printing an array:

x = [3, 4, 43, 3, 4, 2]

for i in range(len(x)):
    print(x[i])


# Enumerate, provides you with both range and elements:

for i, element in enumerate(x):
    print(i, ". ", element)


# While Loops

x = [3, 4, 42, 3, 2, 4]
i = 0
while i < 10:
    print('run')
    i += 1
    # Add a break statement to break loop
    # break