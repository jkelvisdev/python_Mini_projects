import random
import time

answer = input('Do you want to roll the dice? Yes/no ')

if answer.lower() == 'yes':
    while 1 > 0:
        dice = range(1,7)
        print('We are shaking the dice.')
        time.sleep(1)
        print('We are shaking the dice..')
        time.sleep(1)
        print('We are shaking the dice...')
        time.sleep(1)
        print('dice was thrown')
        time.sleep(1)
        print('the dice is showing the number', random.choice(dice))
        again = input('Do you want to roll the dice again? Yes/No ')
        if again.lower() == 'no':
            print('The game is closed')
            break
elif answer.lower() == 'no':
    print('The game will be closed.')
else: 
    print('You should select a valid option')