# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random
num = list()
n = 0
while n < 10:
    numbers = random.randint(0, 555)
    n = n+1
    num.append(numbers)
print(num)
print('Largest number is:',max(num))