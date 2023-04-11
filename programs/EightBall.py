# basic eight ball program

import random

def UserQuestion():
    print("Ask me any question")
    question = input()
    return question

def BallChoices():
    print("You asked me: " + UserQuestion())
    roll = random.randint(1, 6)
    print("You rolled a " + str(roll))

    match roll:
        case 1:
            print("Very much likely")
        case 2:
            print("I'm pretty sure")
        case 3:
            print("I am not so sure")
        case 4:
            print("I don't think so")
        case 5:
            print("Maybe not")
        case 6:
            print("I have but a clue")

BallChoices()