# simple program that makes use of if statements to check whether a number is meeting a certain requirement

number = input()

if number != "5":
    print(False)
else:
    print(True)


# else if statements

newNumber = input()

if newNumber == "10":
    print("Too far")
elif newNumber == "15":
    print("Close")
elif newNumber == "20":
    print("You got it")