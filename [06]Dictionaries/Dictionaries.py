# Dictionaries

# 1. make a dictionary
person = {"name": "Ana", "age": 20}
print(person)

# 2. get a value
print(person["name"])

# 3. add and change
person["city"] = "Lipa"
person["age"] = 21
print(person)

# 4. get() so there is no error
print(person.get("email"))
print(person.get("email", "no email"))

# 5. remove
person.pop("city")
print(person)

# 6. loop
scores = {"math": 90, "art": 85}
for subject in scores:
    print(subject, scores[subject])

# 7. keys, values, items
print(scores.keys())
print(scores.values())
for k, v in scores.items():
    print(k, "->", v)

# 8. count letters
word = "banana"
count = {}
for letter in word:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print(count)
