import random
import sys

number = random.randrange(1,10)
guesses = 0
win = False
while not win:
    input("Guess a number from 1 to 10")
    guesses += 1
    current_guess = sys.argv[1]
    if current_guess == number:
        print(f'You got it, the number was {number}, with {guesses} tries!')
        win = True
