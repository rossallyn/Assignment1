import csv

student_data = ['id', 'firstname', 'dob', 'firstlineaddress', 'gender']


def display_menu():
    print("**********Student Information System****************")
    print()

    input("""
          A: Add Student Name
          B: View Student List
          C: Search by ID number
          D: delete Student
          E: Quit/Exit

          Press Any key! """)


def enterstudentdetails():
    global student_data

    stud_data = []
    print("Enter student id")
    id = input()
    stud_data.append(id)
    print("Enter student name")
    firstname = input()
    stud_data.append(firstname)
    print("Enter your Year Level")
    dob = input()
    stud_data.append(dob)
    print("Enter your course")
    firstlineaddress = input()
    stud_data.append(firstlineaddress)
    print("Enter Gender")
    gender = input()
    stud_data.append(gender)

    with open('studentfile.txt', 'a') as studentfile:
        studentfileWriter = csv.writer(studentfile)
        studentfileWriter.writerows([stud_data])
        print("Record has been  added to file")


def viewstudentdetails():
    f = open("studentfile.txt", "r", encoding="utf8")
    displaylist = f.read()
    print(displaylist)
    f.close()


def searchbyid():
    with open("studentfile.txt", "r") as studentfile:
        idnumber = input("Enter the ID number you require:")
        studentfileReader = csv.reader(studentfile)
        for row in studentfileReader:
            for field in row:
                if field == idnumber:
                    print(row)


def deletestudent():
    global student_data

    print("--- Delete Student ---")
    idnumber = input("Enter the ID number to delete:")
    student_found = False
    updated_data = []
    with open("studentfile.txt", "r") as studentfile:
        reader = csv.reader(studentfile)
        counter = 0
        for read in reader:
            if len(read) > 0:
                if idnumber != read[0]:
                    updated_data.append(read)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open("studentfile.txt", "w") as studentfile:
            studentfileWriter = csv.writer(studentfile)
            studentfileWriter.writerows(updated_data)
        print("ID no. ", idnumber, "deleted successfully")
    else:
        print("ID No. not found in our database")

    input("Press any key to continue")


while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == "A" or choice == "a":
        enterstudentdetails()
    elif choice == "B" or choice == "b":
        viewstudentdetails()
    elif choice == "C" or choice == "c":
        searchbyid()
    elif choice == "D" or choice == "d":
        deletestudent()
    else:
        break
