#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
rem = 0
if number < 0:
    number = abs(number)
    rem = (number % 10) * -1
    number *= -1
else:
    rem = number % 10
if rem > 5:
    print(f"Last digit of {number} is {rem} and is greater than 5")
elif rem == 0:
    print(f"Last digit of {number} is {rem} and is 0")
else:
    print(f"Last digit of {number} is {rem} and is less than 6 and not 0")
