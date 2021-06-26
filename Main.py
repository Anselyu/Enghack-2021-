import random
from Bank import *

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
else:
    tempUser = input("Please enter your customer ID")
    tempPassword = input("Please enter your password")
    

#
# replace blank with customer name
#
print("Welcome " + "blank")
print("Please select the function you would like to access:")
print("1. Deposit")
print("2. Withdraw")
print("3. Display Name and ID")
print("4. Display Balance")
print("5. Change Account Details")
print("6. Display Transaction History")
choice = input()

if (choice == "1"):
    print("How much money would you like to deposit?")
    Bank.deposit( )