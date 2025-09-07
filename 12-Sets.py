# Sets are fast!
# Frequency and order doesn't matter
# Used to check if an element exists or not

x = set()
s = {4,32,2,2}

print(s)

s.add(5)

print(s)

s.remove(5)

print(s)

# Check existence of element:

print(33 in s)
print(4 in s)

# Union and Intersection:
s2 = {5,6,1,0}

print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))