# List comprehension

# 1. normal loop first
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)

# 2. same thing in one line
squares = [n * n for n in range(1, 6)]
print(squares)

# 3. letters
print([ch.upper() for ch in "abc"])

# 4. only even numbers
print([n for n in range(10) if n % 2 == 0])

# 5. double each number
nums = [1, 2, 3, 4]
print([n * 2 for n in nums])

# 6. length of each word
words = ["python", "is", "fun"]
print([len(w) for w in words])

# 7. if / else inside
print(["even" if n % 2 == 0 else "odd" for n in range(5)])

# 8. numbers divisible by 3
print([n for n in range(1, 31) if n % 3 == 0])
