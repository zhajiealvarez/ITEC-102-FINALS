# For loops

# 1. range
for i in range(5):
    print(i)

# 2. loop over a string
for letter in "Python":
    print(letter)

# 3. start, stop, step
for i in range(2, 11, 2):
    print(i)

# 4. loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 5. sum of 1 to 100
total = 0
for n in range(1, 101):
    total = total + n
print(total)

# 6. break and continue
for n in range(1, 10):
    if n == 3:
        continue
    if n == 7:
        break
    print(n)

# 7. multiplication table
for i in range(1, 6):
    print("5 x", i, "=", 5 * i)

# 8. nested loop (star pattern)
for row in range(1, 5):
    for col in range(row):
        print("*", end="")
    print()
