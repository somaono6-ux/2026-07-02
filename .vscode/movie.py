movies = []
def add_movie():
    title = input("What is the movie name?")
    genre = input("What is the movie genre?")
    year = int(input("which year was movie published?"))
    watched = False
    movies.append({"title": title, "genre": genre, "year": year, "watched": watched})
def show_movie():
    for movie in movies:
        print("Title: ",movie["title"],"Genre :", movie["genre"],"Year: ", movie["year"],"Watched : ", movie["watched"])
def search_movie():
    found = False
    search = input("What movie are you looking for?")
    for movie in movies:
        if movie["title"].lower() == search.lower():
            print("Title: ",movie["title"],"Genre :", movie["genre"],"Year: ", movie["year"],"Watched : ", movie["watched"])
            found = True
    if found == False:
        print("Movie you are looking for not found")
def edit_movie():
    found = False
    search = input("What movie would you like to change?")
    for movie in movies:
        if movie["title"].lower() == search.lower():
            print("Title: ",movie["title"],"Genre :", movie["genre"],"Year: ", movie["year"],"Watched : ", movie["watched"])
            found = True
            watch_ans = input("DO you want to change it as watched? yes/no")
            if watch_ans == ("yes"):
                movie["watched"] = True
                print("changed!")
            else:
                print("Nothing changed")
    if found == False:
        print("Movie you are looking for not found")
def remove_movie():
        found = False
        search = input("What movie do you want to remove?")
        for movie in movies:
            if movie["title"].lower() == search.lower():
                print("Title: ",movie["title"],"Genre :", movie["genre"],"Year: ", movie["year"],"Watched : ", movie["watched"])
                remove_ans = input("Is this the movie you want to remove? yes/no")
                if remove_ans == ("yes"):
                    movies.remove(movie)
                    print("movie removed!")
                    found = True
                else:
                    print("removing canceled")
        if found == False:
            print("Movie you are looking for not found")
def stats_movie():
    watched_count = 0
    for movie in movies:
        if movie["watched"] == True:
            watched_count += 1
    unwatched_count = 0
    for movie in movies:
        if movie["watched"] == False:
            unwatched_count += 1
    print("Total movies in the list:",len(movies), "Movies watched:", watched_count, "Movies not watched:", unwatched_count)
while True:
    print("""#######Movie tracker#######
      1. Add a movie
      2. Show movies
      3. Search a movie
      4. Mark as watched
      5. remove a movie
      6. Current movie status
      7. Exit""")
    ans = input("Enter your choice:")
    if ans == ("1"):
        add_movie()
    elif ans == ("2"):
        show_movie()
    elif ans == ("3"):
        search_movie()
    elif ans == ("4"):
        edit_movie()
    elif ans == ("5"):
        remove_movie()
    elif ans == ("6"):
        stats_movie()
    elif ans == ("7"):
        print("Bye!")
        break
    else:
        print("Seems like you typed something else")