class CheckIn:
    def __init__(self, username, password, userID, balance):
        self.username = username
        self.password = password
        self.userID = userID
        self.balance = balance

    #reads the CustomerInfo.txt file to and returns the information of the user
    def checkInfo(self):
        with open("Enghack-2021-/CustomerInfo.txt", "r") as file_object:
            allLines = file_object.readlines()
            count = -1
            for i in allLines:
                count += 1
                if self.username in allLines[count]:
                    break
            information = allLines[count]
            custInfo = information.split()
            return custInfo

    
    #adds the new customer information to the CustomerInfo.txt file
    def register(self):
        with open("Enghack-2021-/CustomerInfo.txt", "a") as file_object:
            file_object.write(self.username + " " + self.password + " " + self.userID + " " + self.balance + "\n")

username = input()
password = input()
userID = input()
balance = input()

test = CheckIn(username, password, userID, balance)
test.checkInfo()

