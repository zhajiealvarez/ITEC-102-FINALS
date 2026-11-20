# Booleans

# 1. True and False
print(True)
print(False)

# 2. comparisons give a boolean
print(5 > 3)
print(5 == 3)

# 3. type
print(type(True))

# 4. and
print(True and True)
print(True and False)

# 5. or
print(True or False)
print(False or False)

# 6. not
print(not True)
print(not False)

# 7. bool() of values
print(bool(1))
print(bool(0))
print(bool("hello"))
print(bool(""))

# 8. use in a program
age = 20
has_id = True
can_enter = age >= 18 and has_id
print("Can enter:", can_enter)
