import random
from Bank import *

bank = Bank()
currID = 0

def register():
    newName = input("Please enter your name: ")
    newPass = input("Please enter a password: ")
    newBal = input("Please enter starting balance: ")
    bank.createCustomer(newName, newPass, newBal)
    bank.displayInfo()
    currID = bank.getCustID()

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
print("6. Logout")
print("7. Exit")
choice = input()

if (choice == "1"):
    print("How much money would you like to deposit?")
    bank.deposit(currID, input())
elif (choice == "2"):
    print("How much money would you like to withdraw?")
    withdrawAmt = input()
    
    while (withdrawAmt >= bank.getMoney()):
        print("You don't have that much money to withdraw! Please enter a valid amount, otherwise enter 0 to exit.")
        withdrawAmt = input()
    
    bank.withdraw(currID, withdrawAmt)
elif (choice == "3"):
    bank.displayInfo(currID)
elif (choice == "4"):
    bank.displayBalance(currID)
elif (choice == "5"):
    print("What would you like to change?")
    print("1. Name")
    print("2. Password")
    changeChoice = input()

    if (changeChoice == "1"):
        print("what would you like to change your name to?")
        bank.changeName(currID, input())
    elif (changeChoice == "2"):
        print("What would you like to change your password to?")
        bank.changePass(currID, input())
    else:
        print("Choice invalid.")
elif (choice == "6"):
    pass
elif (choice == "7"):
    print("Thank you for coming to CEK Bank, please come again!")
    # Save all the info here
    exit()
