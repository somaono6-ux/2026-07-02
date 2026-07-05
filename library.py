library = {}
while True:
    print (
        """########Library########
        1.Add Books
        2.Show Books
        3.Search Books
        4.Remove Books
        5. Borrow books
        6. Return books
        7.Exit
        """
        )
    answer = input("Enter your choice:")
    if answer == "1":
        title = input("What is the book title?:")
        if title in library:
            print("The book is already in the library")
        else:
            author = input("Who is the author?:")
            library[title] = {"author": author, "available": True}
    elif answer == "2":
        if  library:
            for title in library:
                print("Title:", title, "| Author:", library[title]["author"], "| Available:", library[title]["available"])
        else:
            print("No books in library yet")
    elif answer == "3":
        searching = input("What book are you looking for?")
        if searching in library:
            print("Title:", searching, "| Author:", library[searching]["author"], "| Available:", library[searching]["available"])
        else:
            print("the book not found")
    elif answer == "4":
        remove = input("What book do you want to remove?:")
        if remove in library:
            del library[remove]
            print("Removed successfully!")
        else:
            print("Item not found")
    elif answer == "5":
        searching = input("What book do you want to borrow?")
        if searching in library:
            print("Title:", searching, "| Author:", library[searching]["author"], "| Available:", library[searching]["available"])
            borrow_ans = input("Would you like to borrow this book?(yes/no)")
            if borrow_ans == "yes":
                if library[searching]["available"]:
                    library[searching]["available"]=False
                    print ("borrowed!")
                else:
                    print("The book is already borrowed by someone")
            elif borrow_ans == "no":
                print("Borrowing canceled")
        else:
            print("the book not found")
    elif answer == "6":
        searching = input("What book do you want to return?")
        if searching in library:
            print("Title:", searching, "| Author:", library[searching]["author"], "| Available:", library[searching]["available"])
            return_ans = input("Would you like to return this book?(yes/no)")
            if return_ans == "yes":
                if not library[searching]["available"]:
                    library[searching]["available"]=True
                    print ("returned!")
                else:
                    print("The book is already returned")
            elif return_ans == "no":
                print("returning canceled")
        else:
            print("the book not found")
    elif answer == "7":
        print ("Bye!")
        break
    else:
        print("Seems like you typed something else. Try again")
