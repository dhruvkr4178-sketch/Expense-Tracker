# Expense Tracker Project 

expenses = [] #List of expenses in form of dicitionary
print("Welcome to Expense Tracker")

while True:
    print("======Menu======")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total Cost")
    print("4. Exit")

    choice = int(input("Please Enter your choice"))

# Add Expense
    if(choice==1):
        date=input("Enter the date of the expense (DD-MM-YYYY): ")
        category = input("Enter the expense category (Food, Travel, Shopping, Bills, Entertainment, etc.): ")
        description = input("Enter a description for the expense:" )
        amount = float(input("Enter the amount of product"))

        expense = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\nExpenses is added succesfully")

# 2. VIEW ALL EXPENSES
    elif(choice==2):
        if( len (expenses)==0 ):
            print("No Expenses Added.")
        else:
            print("=======Your Expenses")
            count = 1
            for items in expenses:
                print(f"Item Number{count} -> {items["date"]},{items["category"]},{items["description"]},{items["amount"]}")
                count = count + 1

#3. VIEW TOTAL SPENDING
                
    elif(choice==3):
        total = 0
        for items in expenses:
            total = total + items["amount"]

        print("\n Total expenses = ",total)    


#4. EXIT
    elif(choice == 4):
        print("Thank You For Choosing Our Expenses Tracker Platform")
        break

    else:
        print("Invalid Choice ... Please Try Again")


   
   


































