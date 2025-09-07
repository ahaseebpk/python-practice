# Allows to take slice of a collection: String, Array, List, Tupple, etc
# sliced = x[start:stop:step]
# sliced = x[:4] start at beginning and stop at 4
# sliced = x[2:] start at 2
# sliced = x[4:2,-1]: Start at 4, end at 2, step -1
# sliced = x[::-1]: reverse a list

x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye']
s = "hello"

print(s[::-1])
print(y[::-1])