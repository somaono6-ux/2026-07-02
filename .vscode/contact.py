import json
contacts = []
def add_contact():
    name = input("What is the name of the new contact?:")
    number = input("What is his/her phone number?:")
    contacts.append({"name": name, "phone": number})

def show_contact():
    print(contacts)

def save_contact():
    json_text = json.dumps(contacts)
    print(json_text)
    with open("contacts.json", "w") as f:
        f.write(json_text+"\n")

def load_contact():
    global contacts
    with open("contacts.json", "r") as f:
        raw_txt = f.read()
    contacts = json.loads(raw_txt)
while True:
    print("""Contact book
1. Add contact
2. Show contacts
3. Save data
4. Load data
5. Exit""")
    choice = int(input("select your choice:"))
    if choice == 1:
        add_contact()
    elif choice == 2:
        show_contact()
    elif choice == 3:
        save_contact()
    elif choice == 4:
        load_contact()
    elif choice == 5:
        print("Bye!")
        break
    else:
        print("Seems like you've typed something else")
    

