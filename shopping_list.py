
shopping_list = []
def add_item(my_list):
    item = input("what do you need to buy?")
    my_list.append(item)
def show_items(my_list):
    if len(my_list) ==0:
        print("nothing here!")
    else:
        for i in range(len(my_list)):
            print(i + 1, my_list[i])

def remove_item(my_list):
    x = input("what item you want to remove?")
    if x in my_list:
        my_list.remove(x)
    else:
        print("item not found")


while True:
    print("""==========================
Shopping List Manager
==========================
1. Add item
2. Show items
3. Remove item
4. Exit""")
    choice = input("Choose an option: ")
    if choice == "1":
        add_item(shopping_list)
    elif choice == "2":
        show_items(shopping_list)
    elif choice =="3":
        remove_item(shopping_list)
    elif choice =="4":
        print("good bye!")
        break
    else:
        print("seems like you type something different")