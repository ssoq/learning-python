# hangman
# this program will generate a random string which the player then has to guess
# the player has a limited amount of tries to guess the string before their
# try count reaches 0, when it does, they lose

import random

words = ["silly", "stand", "octopus", "man", "daddy", "mummy", "development", 
         "subtract", "addition", "python", "c#", "programming", "unity"]
chosenWord = str(random.choice(words))

print("You must attempt to guess the word I am thinking of")
 
def UserGuess():
    guess = input("Word: ")
    return guess

def CheckGuess():
    while UserGuess() != chosenWord:
        UserGuess()
    else:
        UserWon()

def UserWon():
    print("You won, good job")

def UserLost():
    print("You lost, bad job")

UserGuess()
CheckGuess()
