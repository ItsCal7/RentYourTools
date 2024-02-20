# The lent tool class will manage the actual rental side of things.
# It will move items from the available list to the rented list,
# and vice versa alongside managing the pending list to await admin approval of returns.
# It will also create a rental object that stores information like which tool is being rented,
# who rented it, and th
# e date it needs to be returned using the calendar library.
import datetime
import Spreadsheet


class Lending:
    def __init__(self):
        self.__renter = None
        self.__returnDate = None
        self.__rentedTool = None
        self.__price = None
        self.__pending = False

    def getRenter(self):
        return self.__renter

    def getReturnDate(self):
        return self.__returnDate

    def getRentedTool(self):
        return self.__rentedTool

    def getPrice(self):
        return self.__price

    def checkPending(self):
        return self.__pending

    def calcPrice(self, weekNum):
        for toolID in range(2, Spreadsheet.getRows("tools")+1):
            if Spreadsheet.getValue(toolID, 1, "tools") == self.__rentedTool:
                price = Spreadsheet.getValue(toolID, 2, "tools")
                price *= weekNum
        return price

    def calcDate(self, weekNum):
        today = datetime.date.today()
        weeks = datetime.timedelta(days=weekNum * 7)
        return today + weeks

    def createLend(self, user, tool, rentWeeks: int = 1):
        self.__renter = user
        self.__returnDate = self.calcDate(rentWeeks)
        self.__rentedTool = tool
        self.__price = self.calcPrice(rentWeeks)

    # def deleteLend(self):
    #     stuff.lentNum += 1
    #     tempLend = "lend" + str(stuff.lentNum)
    #     self.__renter = user
    #     self.__returnDate = self.calcDate(rentWeeks)
    #     self.__rentedTool = tool
    #     self.__price = self.calcPrice(rentWeeks)
    #     stuff.lentList.append(tempLend)
