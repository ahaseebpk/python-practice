x = [1,2,3,4,5,6,7,89,10,22,22,3,4,5,6,8,2,2,1,3]

mp = map(lambda i: i+2, x)

print(list(mp))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

# You can also use functions

def func(i):
    return i % 2 == 0

mp = filter(func, x)
print(list(mp))