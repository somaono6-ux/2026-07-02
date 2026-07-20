import json
def load_pass():
    try:
        with open("passwords.json", "r") as f:
            passwords = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords

def save_pass(passwords):
    try:
        with open("passwords.json", "w") as f:
            json.dump(passwords , f)
    except (PermissionError):
        print("Permission Error! Cant save file!")

def add_account(passwords):
    website = input("What is the website called? :")
    if website =="":
        print("Please type the website name")
        return
    else:
        username = input("What is the username? :")
        password = input("What is the password? :")
        passwords[website] = {"username": username, "password" : password}
        save_pass(passwords)

def show_accounts(passwords):
    if passwords =={}:
        print("Please add your account first")
    else:
        for website in passwords:
            print ("Website :", website,"Username :",  passwords[website]["username"], "Password :", passwords[website]["password"])

def search_website(passwords):
    search = input("What website's password are you looking for? :")
    try:
        username = passwords[search]["username"]
        password = passwords[search]["password"]
        print("Username :", username, "Password :",password)
    except KeyError:
        print("Website not found")

def delete_website(passwords):
    delete = input("What website's password do you want to delete? :")
    try:
        username = passwords[delete]["username"]
        password = passwords[delete]["password"]
        ans = input("Are you sure you want to delete "+ f"{delete}"+ "Username :"+ f"{username}"+"Password :"+f"{password}"+ "? (yes/no)")
        if ans == "yes":
            del passwords[delete]
            print("deleted successfully")
            save_pass(passwords)
        elif ans == "no":
            print("deleting canceled")
        else:
            print("seems like you've typed something else")
    except KeyError:
        print("Website not found")


passwords = load_pass()

while True:
    print("""#####password manager#####
          1. Add password
          2. Show passwords
          3. Search passwords
          4. Delete passwords
          5. Exit""")
    try:
        choice = int(input("Please select your choice :"))
        if choice == 1:
            add_account(passwords)
        elif choice == 2:
            show_accounts(passwords)
        elif choice == 3:
            search_website(passwords)
        elif choice == 4:
            delete_website(passwords)
        elif choice == 5:
            print("Bye!")
            break
        else:
            print("Seems like you've typed something else.")
    except ValueError:
        print("Seems like you've typed something else.")