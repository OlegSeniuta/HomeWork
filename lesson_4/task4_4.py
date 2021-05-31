# The math quiz program
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.
import math as mt
value = [4.28, 8.01]
total = mt.fsum(value)
user = input('What is sum of 4.28 and 8.01?\n')
try:
    user1 = float(user)
    count = 3
    while count > 0 and user.isdigit() is True:
        count = count - 1
        if user1 != total:
            print('Sorry, wrong answer. You can try again')
            user = input('What is sum of 4.28 and 8.01?\n')
            user1 = float(user)
            if total == user1:
                print('Your answer is correct')
                break
            if count == 0:
                print('You out of attempt')
        if total == user1:
            print('Your answer is correct')
except:
    print('Invalid input')
