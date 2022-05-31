#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = -1 * number
else:
    number1 = number
if number1 % 10 > 5:
    print(f"Last digit of {number} is {number1%10} and is greater than 5")
elif number1 % 10 == 0:
    print(f"Last digit of {number} is {number1%10} and is 0")
else:
    print(f"Last digit of {number} is {number1%10} and is \
less than 6 and not 0")
