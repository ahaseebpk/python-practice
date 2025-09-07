# Dictionaries

x = {'key': 4}
print(x['key'])

x['key2'] = 5
print('key2')

x[2] = [1,2,3]
print(x)

print('key' in x)

print(x.values())
print(list(x.values()))

del x['key']
print(x)

for key, value in x.items():
    print(key, value)