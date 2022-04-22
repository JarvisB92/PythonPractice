"""
Your module description
"""
#Guess The Number
##user will input a random number with unlimited attempts to "Guess The Number" correctly
##This program will respond by giving a "too low","too high",or "You Guessed It!" response

import random
print("Try To Guess The Number!")

#generating a random integer with a variable
any_number = random.randint(0,100)
answer = random.randint(0,100)
#User Enters Their Guess 
guess = int(input('Enter Your Guess: '))
counter = 0

while (guess != answer):
   counter += 1 
   if guess < answer:
       print('Too Low! Try Again!')
       guess = int(input('Enter your guess: '))
   elif guess > answer:
       print('Too High! Try Again!')
       guess = int(input('Enter your guess: '))
       print('You Guessed It!')
#Game Complete
