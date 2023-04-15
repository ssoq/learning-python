# this is the main script for the application,
# it will be a simple test that will import
# data that is stored from other python scripts

# importing
import PretendData as PD
import os

# public variables
writeableStrings = [["Names", "names"], ["Ages", "ages"], ["Crimes", "crimes"], ["All", "all"], ["Quit", "quit"]]

def ReadOptions():
    # print question asking user which data to view
    print("We have " + str(len(PD.pretendDataArray)) + " lists of wanted peoples data, which would you like to view?")
    print("Out of the three, we store: names, ages, and the crimes commited.")
    print("If you would like all of the data, say: `All` or `all`.")
    print("To quit, just say either `Quit` or `quit`.")
    DisplayOption()

def ChoosenOption():
    chosenOption = input("Choice: ")
    return chosenOption

def DisplayOption():
    optionChose = ChoosenOption()

    if optionChose in writeableStrings[0]:
        print(PD.pretendDataArray[0])
        ReadOptions()
    elif optionChose in writeableStrings[1]:
        print(PD.pretendDataArray[1])
        ReadOptions()
    elif optionChose in writeableStrings[2]:
        print(PD.pretendDataArray[2])
        ReadOptions()
    elif optionChose in writeableStrings[3]:
        print(PD.pretendDataArray) 
        ReadOptions()
    elif optionChose in writeableStrings[4]:
        CloseProgram() 
    else:
        ClearConsole()
        ReadOptions()

def CloseProgram():
    print("Closing now...")
    quit()

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

ReadOptions()