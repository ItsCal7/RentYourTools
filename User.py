import Spreadsheet


def checkUser(userName):
    boolTest = True
    for row in range(2, Spreadsheet.userSheet.max_row+1):
        if Spreadsheet.getValue(row, 1, "users") == userName:
            boolTest = False
    return boolTest


class User:
    def __init__(self, accountType=None, username=None, password=None):
        self.__acctype = accountType
        self.__uName = username
        self.__pw = password

    def getAccountType(self):
        return self.__acctype

    def getUsername(self):
        return self.__uName

    def getPassword(self):
        return self.__pw

    def createUser(self, boolAd):
        if boolAd:
            self.__acctype = "Admin"
        else:
            self.__acctype = "Customer"
        while True:
            self.__uName = input("\nSet New Username: ")
            if not checkUser(self.__uName):
                print("Username Already in Use")
                continue
            self.__pw = input("Set New Password: ")
            break

    def printUser(self):
        print("Username:", self.__uName)
        print("Password:", self.__pw)
        print("Account type:", self.__acctype)


class Admin(User):
    def __init__(self, accountType=None, username=None, password=None):
        User.__init__(self, accountType, username, password)

    def createUser(self, adminBool=True):
        User.createUser(self, adminBool)


class Customer(User):
    def __init__(self, accountType=None, username=None, password=None):
        User.__init__(self, accountType, username, password)

    def createUser(self, adminBool=False):
        User.createUser(self, adminBool)
