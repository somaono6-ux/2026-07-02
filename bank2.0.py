accounts={}
import json

def load_accounts():
    with open("bank.json", "r") as f:
        raw_txt = f.read()
        accounts = json.loads(raw_txt)
        return accounts

accounts = load_accounts()
def save_accounts():
    with open ("bank.json","w") as f:
        json.dump(accounts, f)

def add_accounts():
    name = input("What is your name?")
    balance = int(input("What is your balance?:"))
    accounts[name] = {"balance": balance}

def show_accounts():
   for name in accounts:
      print(name + ":", accounts[name]["balance"])

def deposit_money():
   search = input("What is your name?:")
   adding = int(input("How much money are you adding?:$"))
   found=False
   for name in accounts:
    if name == search:
        accounts[name]["balance"]+= adding
        print("Your current balance is", accounts[name]["balance"])
        found =True
   if found == False:
      print("The name not found")

def withdraw_money():
   search = input("What is your name?:")
   adding = int(input("How much money are you withdrawing?:$"))
   found=False
   for name in accounts:
    if name == search:
        if accounts[name]["balance"]>=adding:
           accounts[name]["balance"]-= adding
           print("Your current balance is", accounts[name]["balance"])
           found =True
        else:
           print("You do not have enough money!")
           found =True
   if found == False:
      print("The name not found")

def search_account():
   search = input("What is your name?:")
   found = False
   for name in accounts:
      if name == search:
         print("Hello", search, "your current balance is", accounts[name]["balance"])
         found = True
   if found == False:
      print("The name not found")

def delete_account():
   search = input("Who would you like to delete:")
   found = False
   target = None          

   for name in accounts:
      if name == search:
         print("Would you like to delete", search, "? your current balance is", accounts[name]["balance"])
         found = True
         target = name

   if found == True:
      del_ans = input("yes/no")
      if del_ans == "yes":
         del(accounts[target]) 
      elif del_ans == "no":
         print("deleting canceled")
      else:
         print("Seems like you typed something else")
   else:
      print("The name not found")

while True:
   print("""#####Bank 2.0#####
         1. Add acount
         2. show account
         3. deposit money
         4. withdraw money
         5. search account
         6. delete account
         7. exit""")
   choice = int(input("What is your choice?"))
   if choice == 1:
      add_accounts()
      save_accounts()
   elif choice == 2:
      show_accounts()
   elif choice == 3:
      deposit_money()
      save_accounts()
   elif choice == 4:
      withdraw_money()
      save_accounts()
   elif choice == 5:
      search_account()
   elif choice == 6:
      delete_account()
      save_accounts()
   elif choice == 7:
      print("Bye!")
      break
   else:
      print("Seems like you've typed something else")