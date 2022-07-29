# Python Basics
import math
import module_example as mEx

print("Hello World")

if 10 < 20:
    print("10 is less than 20.")
else:
    print("else")

name = "Jacob"
age = 30

# print(name + " is your name.")
print(f"{name} is your name in f strings and {age} is your age.")

print(math.ceil(3.2))
print(math.floor(3.2))
mEx.welcome(name)