from Customer import Customer
#custID is for set up, custNum is the variable to determine which customer ID the operation is targeted to.
class Bank: 
    custList = []
    custID = 0;
    def __init__(self): #initialize class with all the values from the spreadsheet
        pass 

    def createCustomer(self, name, password, startingBalance):
        custList.append(Customer(custID, name, password, startingBalance)) # Customer array, super wack pls fix. Add starting parameters
        custID += 1; #this counters the customer ID 

    def deposit(self, custNum, amount): #Change user's balance by a positive amount 
        customerCurrentBalance = custList[custNum].getMoney()
        custList[custNum].setMoney(customerCurrentBalance + amount)

    def withdraw(self, custNum, amount): #Change user's balance by a negative amount 
        customerCurrentBalance = custList[custNum].getMoney()
        custList[custNum].setMoney(customerCurrentBalance - amount)

    def changeInfo(self, newName, newPass): #Change user's name and pass
        pass
    
    def displayBalance(self, custNum): #Display user's balance
        pass

    def displayName(self, custNum): #DIsplay user's name 
        pass

    def displayTransactionHistory(self, custNum): #Display user's transaction history
        pass
    

        
        
    

    
