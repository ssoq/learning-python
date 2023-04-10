# switch statements

number = 20

def NumberSwitcher():
    match number:
        case 10:
            print("Youve got " + str(number))
        case 20:
            print("Now you have " + str(number))
        case 30:
            print("You have now " + str(number))
        case 40:
            print("You have " + str(number))

NumberSwitcher()