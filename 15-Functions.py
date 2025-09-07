def func():
    print('Run')

# Functions are actually objects

func()

def func(x, y, z = 10):
    print('Run', x, y,z)
    return x * y, x / y, z

r1, r2, r3 = func(5, 6)
print(r1, r2)

# =========

# Advanced Functions

def func(x):
    def func2():
        print(x)
    
    return func2 # Functions are objects, they can be returned

print(func(3))

x = func(3)
x()

def func(*args, **kwargs):
    pass

x = [1,23,23444,2333]

print(*x) # Unpack the list and pass elements as arguments like print(1,23,23444,2333)
print(x)

def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(*pair)

# for dict:

for pair in pairs:
    func(**{'x': 2, 'y': 5})
    # If you name the arguments same as keys, they don't have to be in order
    # func(**{'y': 5, 'x': 2}) will also be the same

def func(*args, **kwargs):
    print(*args)

func(1,2,3,4,5, one=0, two=1)