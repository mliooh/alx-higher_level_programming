#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)

last_digit = int(math.copysign(number % 10, number))

if last_digit > 5:
    print("Last digit of " + str(number) + " is " + str(last_digit) + " and is greater than 5")
elif last_digit == 0:
    print("Last digit of " + str(number) + " is " + str(last_digit) + " and is 0")
elif 0 < last_digit < 6:
    print("Last digit of " + str(number) + " is " + str(last_digit) + " and is less than 6 and not 0")
