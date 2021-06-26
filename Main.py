import random
from Bank import Bank

bank = Bank()

def register():
    newID = random.randint(1000000000000000, 9999999999999999)
    print("Your new card number is now: " + str(newID))
    newPW = input("Please enter a password: ")

# introduction text
print("░█████╗░███████╗██╗░░██╗  ██████╗░░█████╗░███╗░░██╗██╗░░██╗")
print("██╔══██╗██╔════╝██║░██╔╝  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝")
print("██║░░╚═╝█████╗░░█████═╝░  ██████╦╝███████║██╔██╗██║█████═╝░")
print("██║░░██╗██╔══╝░░██╔═██╗░  ██╔══██╗██╔══██║██║╚████║██╔═██╗░")
print("╚█████╔╝███████╗██║░╚██╗  ██████╦╝██║░░██║██║░╚███║██║░╚██╗")
print("░╚════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝")

print("Welcome to CEK Bank!")

# add customer check in here?
print("Please select one of the following options:")
print("1. Sign in")
print("2. Register")
choice = input()

if (choice == "2"):
    register()

