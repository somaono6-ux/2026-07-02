def add_note():
    user_note = input("Add yoyur note here:")
    with open ("notes.txt", "a") as f:
        f.write(user_note+"\n")

def read_note():
    with open ("notes.txt", "r") as f:
        number = 1
        for line in f:
            print(number, line)
            number+=1

def search_note():
    user_search = input("What are you looking for?:")
    with open ("notes.txt", "r") as f:
        for line in f:
            if user_search in line:
                print(line)
    
def count_note():
    with open ("notes.txt", "r") as f:
        number = 0
        for line in f:
            number+=1
        print(number)
    
def clear_note():
    doublecheck = input("Are you sure you want to clear the note?(yes/no)")
    if doublecheck == "yes":
        with open ("notes.txt", "w") as f:
            print("the note is clear now")
    elif doublecheck == "no":
        print("clearing note canceled")
    else:
        print("Seems like you typed something else")

while True:
    print("""########Note2.0########
          1. Add note
          2. show note
          3. search
          4. count note
          5. clear note
          6. exit""")
    user_input = int(input("Select your choice"))
    if user_input == 1:
        add_note()
    elif user_input == 2:
        read_note()
    elif user_input == 3:
        search_note()
    elif user_input == 4:
        count_note()
    elif user_input == 5:
        clear_note()
    elif user_input == 6:
        print("Bye!")
        break
    else:
        print("seems like you typed something else")
        
