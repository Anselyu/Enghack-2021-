import random
from Bank import *
from time import sleep

bank = Bank()

with open("Enghack-2021-/CustomerInfo.txt", "r") as file_object:
        allLines = file_object.readlines()
        count = 0
        for i in allLines:
            information = allLines[count]
            custInfo = information.split()
            name = custInfo[0]
            password = custInfo[1]
            bal = custInfo[3]
            bank.createCustomer(name, password, int(bal))
            print(name + " " + password + " " + bal)
            count += 1

def register():
    newName = input("Please enter your name: ")
    newPass = input("Please enter a password: ")
    newBal = input("Please enter starting balance: ")
    bank.createCustomer(newName, newPass, newBal)
    bank.displayInfo(bank.getCustID())
    
    global currID 
    currID = bank.getCustID()
    print("Welcome " + bank.getName(int(currID)))

    with open("Enghack-2021-/CustomerInfo.txt", "a") as file_object:
        file_object.write(newName + " " + newPass + " " + str(currID) + " " + str(newBal) + "\n")

def login():
    tempUser = int(input("Please enter your customer ID:\n"))
    tempPassword = input("Please enter your password:\n")
    loginCheck = CheckIn()
    global currID
    currID = tempUser
    print("Welcome " + bank.getName(int(currID)))

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
    login()

while (choice != 7):
    print("\n")
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
        sleep(1)

    elif (choice == "2"):
        print("How much money would you like to withdraw?")
        withdrawAmt = input()
        
        while (int(withdrawAmt) >= int(bank.getMoney(currID))):
            print("You don't have that much money to withdraw! Please enter a valid amount, otherwise enter 0 to exit.")
            withdrawAmt = input()
        
        bank.withdraw(currID, withdrawAmt)
        sleep(1)
    elif (choice == "3"):
        bank.displayInfo(currID)
        sleep(1)
    elif (choice == "4"):
        bank.displayBalance(currID)
        sleep(1)
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
        print("Logging out, thank you for banking with us.")
        print("\n\n\n\n")
        sleep(1)

        print("Please select one of the following options:")
        print("1. Sign in")
        print("2. Register")
        choice = input()

        if (choice == "2"):
            register()
        else:
            login()
    elif (choice == "7"):
        print("Thank you for coming to CEK Bank, please come again!")
        
        open("Enghack-2021-/CustomerInfo.txt", "w").close()
        for x in range(0, bank.getCustID() + 1):
             with open("Enghack-2021-/CustomerInfo.txt", "a") as file_object:
                file_object.write(bank.custList[x].getName() + " " + bank.custList[x].getPass() + " " + str(bank.custList[x].getCustID()) + " " + str(bank.custList[x].getMoney()) + "\n")

        exit()
