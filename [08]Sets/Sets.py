# Sets

# 1. make a set (no duplicates)
s = {1, 2, 2, 3}
print(s)

# 2. add
s.add(4)
print(s)

# 3. remove
s.remove(1)
print(s)

# 4. check if inside
print(2 in s)
print(10 in s)

# 5. union and intersection
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)

# 6. difference
print(a - b)
print(b - a)

# 7. remove duplicates from a list
nums = [1, 1, 2, 3, 3]
print(list(set(nums)))

# 8. loop
for item in a:
    print(item)
