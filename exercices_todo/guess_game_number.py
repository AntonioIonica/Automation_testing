"""
Toata asta de copiat intr-un fisier extern .py si de rulat apoi in terminal
"""
from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input('Guess a number between 1~10! '))
        if 0 < guess < 11:
            if guess == answer:
                print('The number is correct!')
                break
        else:
            print('Enter a number between 1 to 10 only!')
    except ValueError:
        print('Please enter a number!')
        continue