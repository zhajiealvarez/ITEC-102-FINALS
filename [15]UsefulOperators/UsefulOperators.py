# Useful operators and functions

# 1. range
print(list(range(1, 10, 2)))

# 2. len
print(len("hello"))
print(len([1, 2, 3]))

# 3. in / not in
print("a" in "banana")
print(5 not in [1, 2, 3])

# 4. min, max, sum
nums = [4, 8, 15, 16, 23, 42]
print(min(nums))
print(max(nums))
print(sum(nums))

# 5. += -= *=
x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)

# 6. enumerate
for i, item in enumerate(["a", "b", "c"]):
    print(i, item)

# 7. zip
names = ["Ana", "Ben", "Cara"]
scores = [90, 85, 70]
for name, score in zip(names, scores):
    print(name, score)

# 8. sorted
print(sorted(nums, reverse=True))
words = ["banana", "kiwi", "apple"]
print(sorted(words))
print(sorted(words, key=len))
