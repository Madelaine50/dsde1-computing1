print('Guess a number between 1 and 10')
number = input()
import random
dice_roll = random.randint(1,10)
if (number == dice_roll):
    print('congrats')
else:
    print('unfortunate')
    
