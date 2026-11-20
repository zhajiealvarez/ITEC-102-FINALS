# Tuples

# 1. make a tuple
point = (3, 4)
print(point)

# 2. get items
print(point[0])
print(point[1])

# 3. length
print(len(point))

# 4. tuples cannot be changed
# point[0] = 10   <- this gives an error

# 5. unpacking
x, y = point
print(x, y)

# 6. count and index
t = (1, 2, 2, 3, 2)
print(t.count(2))
print(t.index(3))

# 7. loop
for item in t:
    print(item)

# 8. function that returns 2 values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1])
print(low, high)
