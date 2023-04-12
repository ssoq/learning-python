# password generator
# the passwords that will come out of this program will contain 12-24 chars,
# symbols and lower case letters to ensure strong passwords are outputted

import random

characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
              "r","s","t","u","v","w","x","0","1","2","3","4","5","6","7","8","9"]
symbols = ["$", "£", "#", "?"]

def AmountOfCharacters():
    amountOfCharacters = random.randrange(12, 24)
    print("The amount of characters chosen within your password will be: " + str(amountOfCharacters))
    return int(amountOfCharacters)
    # this function returns the random number of which will be used as the password length 

def GeneratePassword():
    chosenPassword = ""
    for i in range(int(AmountOfCharacters())):
        ChooseCharacter()
        chosenPassword += ChooseCharacter()
    else:
        print(chosenPassword)
    # this function iterates through the range of an int that is stored within the amount of chosen characters
        

def ChooseCharacter():
    whichArray = random.randint(0, 1) # 0 is characters, 1 is symbols
    
    match whichArray:
        case 0:
            chosenCharacter = str(random.choice(characters))
        case 1:
            chosenCharacter = str(random.choice(symbols))

    return chosenCharacter
    # this function chooses a random int which will then choose whether to use characters or symbols
    
GeneratePassword()
ChooseCharacter()
