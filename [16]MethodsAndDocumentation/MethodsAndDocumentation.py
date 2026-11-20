# Functions (methods) and documentation

# 1. simple function
def greet():
    print("Hello!")

greet()

# 2. parameters
def greet_person(name):
    print("Hello,", name)

greet_person("Ana")

# 3. return
def add(a, b):
    return a + b

print(add(2, 3))

# 4. default value
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 10))

# 5. docstring (documentation)
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

print(area(4, 5))
print(area.__doc__)

# 6. keyword arguments
def intro(name, age):
    return name + " is " + str(age)

print(intro(age=20, name="Ana"))

# 7. function with a loop and if
def count_even(numbers):
    """Count how many even numbers are in a list."""
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))

# 8. function that calls another function
def square(x):
    return x * x

def sum_of_squares(a, b):
    """Return a squared plus b squared."""
    return square(a) + square(b)

print(sum_of_squares(3, 4))
