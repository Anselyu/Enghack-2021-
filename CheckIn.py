class CheckIn:
    def __init__(self, username, password):
        self.userLogin = username + password

    #reads the CustomerInfo.txt file to check if the information matches an existing user
    def signIn(self):
        if self.userLogin in open('Enghack-2021-/CustomerInfo.txt').read():
            return True
        else:
            return False
    
    #adds the new customer information to the CustomerInfo.txt file
    def register(self):
        with open("Enghack-2021-/CustomerInfo.txt", "a") as file_object:
            file_object.write(self.userLogin + "\n")

