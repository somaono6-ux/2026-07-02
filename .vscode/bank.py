bank = []

def create_account():
    name = input("What is your name?:")
    balance = int(input("What is your balance?:$"))
    bank.append({"name" : name, "balance" : balance})

def show_account():
   for account in bank:
      print(account["name"] + ":", account["balance"])
    
def deposit_money():
   search = input("What is your name?:")
   adding = int(input("How much money are you adding?:$"))
   found=False
   for account in bank:
    if account["name"] == search:
        account["balance"]+= adding
        print("Your current balance is", account["balance"])
        found =True
   if found == False:
      print("The name not found")

def withdraw_money():
   search = input("What is your name?:")
   adding = int(input("How much money are you withdrawing?:$"))
   found=False
   for account in bank:
    if account["name"] == search:
        if account["balance"]>=adding:
           account["balance"]-= adding
           print("Your current balance is", account["balance"])
           found =True
        else:
           print("You do not have enough money!")
           found =True
   if found == False:
      print("The name not found")

def search_account():
   search = input("What is your name?:")
   found = False
   for account in bank:
      if account["name"] == search:
         print("Hello", search, "your current balance is", account["balance"])
         found = True
   if found == False:
      print("The name not found")

def delete_account():
   search = input("Who would you like to delete:")
   found = False
   target = None          

   for account in bank:
      if account["name"] == search:
         print("Would you like to delete", search, "? your current balance is", account["balance"])
         found = True
         target = account

   if found == True:
      del_ans = input("yes/no")
      if del_ans == "yes":
         bank.remove(target) 
      elif del_ans == "no":
         print("deleting canceled")
      else:
         print("Seems like you typed something else")
   else:
      print("The name not found")
while True:
   print("""#######Bank Kanb#######
      1. create account
      2. show accounts
      3. deposit money
      4. withdraw money
      5. search account
      6. delete account
      7. exit""")
   choice = int(input("Select your choice:"))
   if choice == 1:
      create_account()
   elif choice == 2:
      show_account
   elif choice == 3:
      deposit_money
   elif choice == 4:
      withdraw_money
   elif choice == 5:
      search_account
   elif choice == 6:
      delete_account
   elif choice == 7:
      print("bye!")
      break
   else:
      print("Seems like you tiped something else.")