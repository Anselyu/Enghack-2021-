class Customer: 

    custID = 0
    money = 0
    location = ""
    name = ""

    def __init__(self, custID, startingMoney, location, name):
        self.custID = custID
        self.money = startingMoney
        self.location = location
        self.name = name 

    def setMoney(self, moneyChange):
        self.money += moneyChange

    def setLocation(self, location):
        self.location = location

    def setName(self, name):
        self.name = name

    def getCustID (self):
        return self.custID

    def getMoney:
        return money

    def getLocation: 
        return location

    def getName: 
        return name

    