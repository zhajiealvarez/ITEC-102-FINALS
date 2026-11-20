# List basics

# 1. make a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# 2. get items
print(fruits[0])
print(fruits[-1])

# 3. change an item
fruits[1] = "blueberry"
print(fruits)

# 4. add items
fruits.append("date")
fruits.insert(0, "apricot")
print(fruits)

# 5. remove items
fruits.remove("cherry")
fruits.pop()
print(fruits)

# 6. slicing
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[::-1])

# 7. sort
nums = [5, 2, 9, 1]
nums.sort()
print(nums)
nums.reverse()
print(nums)

# 8. loop and sum
total = 0
for n in nums:
    total = total + n
print("Total:", total)
print("Length:", len(nums))
