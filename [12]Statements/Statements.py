# Statements (if / elif / else)

# 1. if
number = 5
if number > 0:
    print("positive")

# 2. if else
if number % 2 == 0:
    print("even")
else:
    print("odd")

# 3. elif
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

# 4. and / or
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter")

# 5. not
raining = False
if not raining:
    print("Go outside")

# 6. one line if
status = "adult" if age >= 18 else "minor"
print(status)

# 7. nested if
if age >= 18:
    if has_ticket:
        print("Welcome")
    else:
        print("Buy a ticket")

# 8. biggest of three numbers
a, b, c = 4, 9, 7
if a >= b and a >= c:
    print("biggest is", a)
elif b >= a and b >= c:
    print("biggest is", b)
else:
    print("biggest is", c)
