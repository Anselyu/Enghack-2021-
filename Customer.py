class Customer: 

    custID = 0
    money = 0
    location = ""
    name = ""

    def __init__(self, custID, name, password, startingMoney):
        self.custID = custID
        self.name = name 
        self.password = password
        self.money = startingMoney

    def setCustID(self, custID):
        self.custID = custID

    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setMoney(self, moneyChange):
        self.money += moneyChange

    def getCustID(self):
        return self.custID

    def getName(self): 
        return self.name

    def getPassword(self): 
        return self.password
        
    def getMoney(self):
        return self.money

