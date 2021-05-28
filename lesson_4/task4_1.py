# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and
# lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
import random
for num in range(0, 1):
    comp = random.randint(1, 10)
user_input = input('Guess generated number \n')
if user_input.isdigit():
    if comp == int(user_input):
        print(f'You guess right {comp}')
    else:
        print('You guess is wrong')
else:
    print('Wrong input format')






