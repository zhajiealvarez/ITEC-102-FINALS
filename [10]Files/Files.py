# Files
# (files are made in the same folder as this script)

# 1. write a file
f = open("test.txt", "w")
f.write("Hello file\n")
f.close()

# 2. read the file
f = open("test.txt", "r")
print(f.read())
f.close()

# 3. use with (closes automatically)
with open("test.txt", "r") as f:
    print(f.read())

# 4. add more text
with open("test.txt", "a") as f:
    f.write("Second line\n")
    f.write("Third line\n")

# 5. read line by line
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# 6. readlines gives a list
with open("test.txt", "r") as f:
    lines = f.readlines()
print(lines)

# 7. count the lines
print("Number of lines:", len(lines))

# 8. file that does not exist
try:
    f = open("nothing.txt", "r")
except FileNotFoundError:
    print("File not found")

# delete the test file
import os
os.remove("test.txt")
