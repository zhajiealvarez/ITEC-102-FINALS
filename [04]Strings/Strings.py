# Strings

# 1. make a string
word = "python"
print(word)

# 2. join strings
print("Py" + "thon")
print("ha" * 3)

# 3. length
print(len(word))

# 4. index
print(word[0])
print(word[-1])

# 5. slicing
print(word[0:3])
print(word[2:])
print(word[::-1])

# 6. upper, lower, strip, replace
text = "  Hello World  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))

# 7. split and join
words = "apple,banana,cherry".split(",")
print(words)
print(" ".join(words))

# 8. check if a word is a palindrome
word = "level"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
