import User as usr, Tools, Spreadsheet, Lending


def newAccount(adminBool):
    if adminBool:
        tempAcc = usr.Admin()
        tempAcc.createUser()
    else:
        tempAcc = usr.Customer()
        tempAcc.createUser()
    Spreadsheet.addAccount(tempAcc)

def newTool():
    tempTool = Tools.Tools()
    tempTool.createTool()
    tempTool.calcPrice()
    Spreadsheet.addTool(tempTool)

def newLend(user, password):
    tempLend = Lending.Lending()
    rentedTool = input("\nEnter ID of desired tool (Type \"Back\" to return to previous menu): ")
    if rentedTool.lower() == "back":
        return None
    for Row in range(2, Spreadsheet.getRows("tools") + 1):
        if Spreadsheet.getValue(Row, 1, "tools") == rentedTool:
            weeks = int(input("Enter how many weeks you would like to rent for: "))
            tempLend.createLend(user, rentedTool, weeks)
            while 1:
                confirm = input("Total Cost: " + str(tempLend.getPrice()) + "\nType your password to confirm order (type \"Cancel\" to cancel): ")
                if confirm == password:
                    Spreadsheet.addLend(tempLend, Row)
                    break
                elif confirm.lower() == "cancel":
                    break
                else:
                    print("\nIncorrect password, try again.")
                    continue

print("Welcome to Rent Your Tools")
while True:
    option = input("\n\"Login\" to login\n\"Register\" to create a new account\n\"Quit\" to quit the program\nEnter your choice: ")
    option = option.lower()

    if option == "login":
        logged = False
        userName = input("\nEnter Username: ")
        userPass = input("Enter Password: ")
        for row in range(2, Spreadsheet.getRows("users")+1):
            if Spreadsheet.getValue(row, 1, "users") == userName and Spreadsheet.getValue(row, 2, "users") == userPass:
                logged = True
                if Spreadsheet.getValue(row, 3, "users") == "Admin":
                    print("\nWelcome, Admin.")
                    while True:
                        choice = input("\n\"Create admin\" to create a new admin account\n\"Create customer\" to create a new customer account\n\"Add Tool\" to add a new tool\n\"Returns\" to review return requests\n\"Logout\" to exit to main menu\nEnter your choice: ")
                        choice = choice.lower()

                        if choice == "create admin":
                            newAccount(True)

                        elif choice == "create customer":
                            newAccount(False)
                            continue

                        elif choice == "add tool":
                            newTool()
                            continue

                        elif choice == "returns":
                            while True:
                                returns = 0
                                choice = input("\n\"Search\" to search by Tool-ID\n\"All\" to see all return requests\n\"Back\" to go to previous menu\nEnter your choice: ")
                                if choice.lower() == "all":
                                    for Row in range(2, Spreadsheet.getRows("lends") + 1):
                                        if Spreadsheet.getValue(Row, 5, "lends"):
                                            print("\nTool ID:", Spreadsheet.getValue(Row, 3, "lends"))
                                            print("Date Due:", Spreadsheet.getValue(Row, 2, "lends"))
                                            returns += 1
                                    if returns == 0:
                                        print("No return requests available for approval.")
                                        break
                                    else:
                                        choice = "search"
                                if choice.lower() == "search":
                                    returnTool = input("\nEnter the tool you would like to confirm (\"Cancel\" to return to previous menu): ")
                                    returnTool.capitalize()
                                    if returnTool == "Cancel":
                                        break
                                    else:
                                        returned = False
                                        for Row in range(2, Spreadsheet.getRows("lends") + 1):
                                            if Spreadsheet.getValue(Row, 5, "lends") and returnTool == Spreadsheet.getValue(Row, 3, "lends"):
                                                for toolRow in range(2, Spreadsheet.getRows("tools") + 1):
                                                    if returnTool == Spreadsheet.getValue(toolRow, 1, "tools"):
                                                        Spreadsheet.deleteLend(Row)
                                                        Spreadsheet.confirmReturn(toolRow)
                                                        print("\nReturn Confirmed")
                                                        returned = True
                                                    elif Row == Spreadsheet.getRows("tools") and not returned:
                                                        print("\nInvalid tool, return failed.")
                                elif choice.lower() == "back":
                                    break
                                else:
                                    print("Invalid input, try again.")
                                    continue
                            continue

                        elif choice == "logout":
                            break

                        else:
                            print("\nInvalid input, try again.")

                elif Spreadsheet.getValue(row, 3, "users") == "Customer":
                    print("\nWelcome, Customer.")
                    while True:
                        choice = input("\n\"Rent\" to rent a tool\n\"Return\" to return a tool\n\"Delete\" to delete your account\n\"Logout\" to exit to main menu\nEnter your choice: ")
                        choice = choice.lower()

                        if choice == "rent":
                            while True:
                                toolCategory = input("\nEnter the category of tool you would like (Cutting, Fastening, Power, or type \"Back\" to return to previous menu): ")
                                toolCategory = toolCategory.lower()
                                if toolCategory == "fastening" or toolCategory == "cutting" or toolCategory == "power":
                                    available = 0
                                    for Row in range(2, Spreadsheet.getRows("tools") + 1):
                                        if Spreadsheet.getValue(Row, 5, "tools") and Spreadsheet.getValue(Row, 3, "tools") == toolCategory:
                                            print("\nTool ID:", Spreadsheet.getValue(Row, 1, "tools"))
                                            print("Tool Condition:", Spreadsheet.getValue(Row, 4, "tools"))
                                            print("Tool Price/Week: $" + str(Spreadsheet.getValue(Row, 2, "tools")))
                                            available += 1
                                    if available == 0:
                                        print("\nNo tools available in this category.")
                                        continue
                                    else:
                                        newLend(userName, userPass)
                                elif toolCategory == "back":
                                    break
                                else:
                                    print("Invalid input, try again.")

                        elif choice == "return":
                            accessed = False
                            for Row in range(2, Spreadsheet.getRows("lends") + 1):
                                if Spreadsheet.getValue(Row, 1, "lends") == userName and not Spreadsheet.getValue(Row, 5, "lends"):
                                    accessed = True
                                    print("\nTool ID:", Spreadsheet.getValue(Row, 3, "lends"))
                                    print("Date Due:", Spreadsheet.getValue(Row, 2, "lends"))
                                    returnTool = input("\nEnter the tool you would like to return (\"Cancel\" to return to previous menu): ")
                                    returnTool.lower()
                                    if returnTool == "cancel":
                                        break
                                    elif Spreadsheet.getValue(Row, 1, "lends") == userName and Spreadsheet.getValue(Row, 3, "lends") == returnTool and not Spreadsheet.getValue(Row, 5, "lends"):
                                        Spreadsheet.returnTool(Row)
                                elif Row == Spreadsheet.getRows("lends") and not accessed:
                                    print("\nNo current lends.")
                            continue

                        elif choice == "delete":
                            test = True
                            for Row in range(2, Spreadsheet.getRows("lends") + 1):
                                if Spreadsheet.getValue(Row, 1, "lends") == userName:
                                    test = False
                            if test:
                                confirm = input("\nAre you sure you want to delete your account? Enter your password to confirm: ")
                                if userPass == confirm:
                                    Spreadsheet.deleteAccount(row)
                                    break
                                else:
                                    print("\nConfirmation failed.")
                                    continue
                            else:
                                print("\nOutstanding/Unapproved lends. Cannot delete account.")
                                continue

                        elif choice == "logout":
                            break

                        else:
                            print("\nInvalid input, try again.")

                else:
                    print("\nError. Account not of type Admin or Customer.")
                    break

            elif row == Spreadsheet.getRows("users") and not logged:
                print("\nIncorrect username or password.")
                break

    elif option == "register":
        newAccount(False)
        continue

    elif option == "quit":
        break

    else:
        print("\nInvalid choice. Try again.")
