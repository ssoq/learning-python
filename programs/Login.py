# this is a login system and is my first program
# the aim of this program is to allow the user to login if the password entered is correct. If it is not correct, restart

password = "password123"

def Login():
    print("Enter your password to login:")
    returnedPassword = input()
    return returnedPassword

def EnterSystem():
    print("Welcome to your system.")

while Login() != password:
    Login()
else:
    EnterSystem()