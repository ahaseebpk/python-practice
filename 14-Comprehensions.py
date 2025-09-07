# Comprehensions

x = [x for x in range(5)]
print(x)

x = [x % 5 for x in range(10)]
print(x)

x = [[0 for x in range(100)]]
print(x)

x = [i for i in range(100) if i % 5 == 0]
print(x)

x = tuple(i for i in range(100) if i % 5 == 0)
print(x)