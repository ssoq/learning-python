# simple program that iterates through numbers, one at a time

import random

number = 0

for number in range(5):
    print(number)
    number = number

# same can be done but with a variable created within the for loop too, lookie lookie

for i in range(5):
    print("Hello, how do you do?")

# tadaaaaa, just like that

for i in range(1, 10):
    if i == 9:
        print(i)
    continue # only prints 9 as continue excepts all other numbers

for i in range(10):
    print(i)
    if i == 5:
        break # stops the loop after lewis == 5