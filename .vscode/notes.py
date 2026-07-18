def write_note():
    note_input = input("Write a note here:")
    with open ("notes.txt", "a") as f:
        f.write(note_input+"\n")
def read_note():
    with open ("notes.txt", "r") as f:
        content = f.read()
        print(content)

while True:
    print("""###### Note ######
          1. Write a note
          2. Read notes
          3. Exit""")
    ans = int(input("Enter your choice:"))
    if ans == 1:
        write_note()
    elif ans == 2:
        read_note()
    elif ans == 3:
        print("bye!")
        break
    else:
        print("Seems like you've typed something else.")