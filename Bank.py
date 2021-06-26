from Customer import Customer
#custID is for set up, custNum is the variable to determine which customer ID the operation is targeted to.
class Bank: 
    def __init__(self): #initialize class with all the values from the spreadsheet
        self.custList = []
        self.custID = 0

    def createCustomer(self, name, password, startingBalance):
        self.custList.append(Customer(self.custID, name, password, startingBalance)) # Customer array, super wack pls fix. Add starting parameters
        self.custID += 1; #this counters the customer ID 
        print(self.custList)

    def deposit(self, custNum, amount): #Change user's balance by a positive amount 
        customerCurrentBalance = self.custList[custNum].getMoney()
        self.custList[custNum].setMoney(int(amount))

    def withdraw(self, custNum, amount): #Change user's balance by a negative amount 
        customerCurrentBalance = self.custList[custNum].getMoney()
        self.custList[custNum].setMoney(0 - int(amount))

    def changeName(self, custNum, newName): #Change user's name
        self.custList[custNum].setName(newName)

    def changePass(self, custNum, newPass): #Change user's password
        self.custList[custNum].setPass(newPass)
    
    def displayBalance(self, custNum): #Display user's balance
        print("Hi, your current balance is " + str(self.custList[custNum].getMoney()) + "$")

    def displayInfo(self, custNum): #DIsplay user's name 
        print("Name: " + self.custList[custNum].getName() + ", ID: " + str(self.custList[custNum].getCustID()))
    
    def getCustID(self):
        return (self.custID - 1)

    def getMoney(self, custNum):
        return self.custList[custNum].getMoney()

    def getName(self, custNum):
        return self.custList[custNum].getName()
        
        
    

    
