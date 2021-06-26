class CheckIn:
    def __init__(self, username, password, userID, balance):
        self.username = username
        self.password = password
        self.userID = userID
        self.balance = balance
    
    #adds the new customer information to the CustomerInfo.txt file
    def register(self):
        with open("Enghack-2021-/CustomerInfo.txt", "a") as file_object:
            file_object.write(self.username + " " + self.password + " " + self.userID + " " + self.balance + "\n")
