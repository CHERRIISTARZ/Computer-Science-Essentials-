#Single Player Guessing Game
#this app allows a user to play against AI to guess a number 

#IMPORTS
import random

#VARIABLES
player_guess = -1
random_number = -1
player_lives = 10

print('Welcome to the sinle player guessing game')
print('Guess a number between 1-1000')

random_number = random.randint(1,1000) 
#print(random_number)
while player_lives > 0:
    try:
        player_guess = int(input('->'))
        player_lives -= 1
        print('Lives Remaining', player_lives)
        if player_guess == random_number:
            print('YOU WIN!')
            break
        elif player_guess > random_number:
            print('Guess Lower')
        elif player_guess < random_number:
            print('Guess Higher')
        else:
            print('Your the reason for the devorce.')
    except: print('Your still the reason for the devorce.')
print('Thanks for playing!')
print('The secret number was ', random_number)