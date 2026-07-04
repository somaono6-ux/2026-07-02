
students= {}
while True:
    print("""1. Add Student
2. Show All Students
3. Search Student
4. Update Grade
5. Remove Student
6. Show Average Grade
7. Exit""")
    user_input = int(input("Please select a number."))
    if user_input == 7:
        print("bye!")
        break
    elif user_input ==1:
        name=input("what is the student name?:")
        grade=int(input("what is his/her grade?"))
        students[name]=grade
    elif user_input ==2:
        for key, value in students.items():
            print(key + ":", value)
    elif user_input ==3:
        y=input("what is the student name?:")
        if y in students:
            print(students[y])
        else:
            print("student not found")
    elif user_input ==4:
        z=input("who do you want to change?")
        if z in students:
          a=int(input("what number is the new grade?"))
          students[z]=a
        else:
               print("student not found")
    elif user_input ==5:
         x=input("who do you want to delete?")
         if x in students:
            del students[x]
         else:
            print("add students first!")
    elif user_input == 6:
        if len(students)==0:
            print("add students and grades!")
        else:
            print(round(sum(students.values()) / len(students)))
    else:
        print("seems like you type something else")
