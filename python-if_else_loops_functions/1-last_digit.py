#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    newnum = -(abs(number) % 10)
else:
    newnum = abs(number) % 10
output = f"Last digit of {number} is {newnum}"
if newnum > 0:
    output += " and is greater than 5"
elif newnum == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)