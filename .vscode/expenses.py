expenses = []
while True:
    print("""######Expense tracker#####
          1. Add expense
          2. Show all expenses
          3. Show total spending
          4. Show avarage spending
          5. Remove an expense
          6. Exit""")
    ans=input("Enter your choice:")
    if ans == "1":
        category=input("What type of products did you spend your money on?:")
        amount=float(input("How much money did you spend?:"))
        expense={"category":category, "amount":amount}
        expenses.append(expense)
    elif ans == "2":
        for expense in expenses:
            print(expense["category"], "- $",expense["amount"])
    elif ans == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print ("Total spending: $", total)
    elif ans == "4":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        avrg=total/len(expenses)
        print("Avarage spending: $", avrg)
    elif ans == "5":
        for i, expense in enumerate(expenses):
            print(i+1, expense["category"], "- $",expense["amount"])
        del_number = int(input("Which expense do you want to delete?:")) - 1
        del expenses[del_number]

    elif ans == "6":
        print("Bye!")
        break
    else:
        print("Seems like you typed something else")