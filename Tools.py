import Spreadsheet

toolConditions = ["bad", "okay", "good", "great"]
toolTypes = {
    "fastening": 1,
    "cutting": 2,
    "power": 5
}

class Tools:
    def __init__(self):
          self.__price = ""
          self.__toolName = ""
          self.__toolID = ""
          self.__size = ""
          self.__condition = ""
          self.__availability = True

    def getPrice(self):
        return self.__price

    def getID(self):
        return self.__toolID

    def getSize(self):
        return self.__size

    def getCondition(self):
        return self.__condition

    def getAvailability(self):
        return self.__availability

    def rent(self):
        self.__availability = False

    def calcPrice(self):
        self.__price = toolTypes[self.__size] + (toolConditions.index(self.__condition))

    def createTool(self):
          self.__toolName = input("\nSet Tool Name: ").capitalize()
          self.__toolID = self.__toolName + "-" + str(Spreadsheet.getRows("tools"))
          self.__size = input("Set Tool Type: ").lower()
          self.__condition = input("Set Tool Condition (Bad, Okay, Good, Great):").lower()
          self.__availability = True

    # def viewTool(self, adbool):
    #     print(self.__toolName)
    #     print("Condition: ", self.__condition)
    #     print("$", self.__price)
