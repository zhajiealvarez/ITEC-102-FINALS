# While loops

# 1. count up
i = 1
while i <= 5:
    print(i)
    i = i + 1

# 2. count down
n = 3
while n > 0:
    print(n)
    n = n - 1
print("Go!")

# 3. sum of 1 to 10
total = 0
k = 1
while k <= 10:
    total = total + k
    k = k + 1
print(total)

# 4. break
count = 0
while True:
    count = count + 1
    if count == 4:
        break
print(count)

# 5. continue
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)

# 6. double a number until it is over 100
x = 1
while x <= 100:
    x = x * 2
print(x)

# 7. sum of digits
num = 1234
digit_sum = 0
while num > 0:
    digit_sum = digit_sum + num % 10
    num = num // 10
print(digit_sum)

# 8. guessing game (guesses are in a list so it runs without typing)
secret = 7
guesses = [3, 9, 7]
index = 0
guess = guesses[index]
while guess != secret:
    print(guess, "is wrong")
    index = index + 1
    guess = guesses[index]
print(guess, "is correct!")
