def func():
    print('Run')

# Functions are actually objects

func()

def func(x, y, z = 10):
    print('Run', x, y,z)
    return x * y, x / y, z

r1, r2, r3 = func(5, 6)
print(r1, r2)