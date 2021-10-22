import random
import math

play = True

guess = random.randint(0, 100)  #generate a random integer value between 0-100
guesses = 0
while play == True:
    try:
        userguess = int(input('Guess a number between 0-100 : '))
    except ValueError:
        print('Please enter a valid integer.')
    else:
        if(userguess > guess):
            print('Too high! Try again...')
            guesses += 1
        elif(userguess < guess):
            print('Too low! Try again...')
            guesses += 1
        elif(userguess == guess):
            print('Correct! The number was ', guess, ' and it took you ', guesses ,'times to get it right!')
            play = False
        

 
    