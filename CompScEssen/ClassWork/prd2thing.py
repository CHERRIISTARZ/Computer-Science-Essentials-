#Homeroom roster program
#This program is designed to allow a teacher to:
#1) See students in homeroom 
#2) Add/remove students to homeroom
#3) See basic info about students
#4) 

#Create an object called Student
class Student:
    def __init__(self, name, grade, ID, address, age, lockerNumber):
        self.name = name 
        self.grade = grade
        self.ID = ID
        self.address = address
        self.age = age
        self.lockerNumber = lockerNumber

listOfHomeroomStudents = []

#Functions
def addToHomeroom():
    # Create a new student object with the following properties:
    # name, grade, ID, address, age, lockerNumber
    print("Create a new student:")
    print("What is their name?")
    name = input("->")

    print("What is their grade?")
    grade = input("->")
    
    print("What is their ID?")
    ID = input("->")

    print("What is their address?")
    address = input("->")

    print("What is their age?")
    age = input("->")

    print("What is their locker number?")
    lockerNumber = input("->")
    newStudent = Student(name, grade, ID, address, age, lockerNumber)
    listOfHomeroomStudents.append(newStudent)
    print("Created a student with the details below:")
    print("Name:", newStudent.name)
    print("Grade:", newStudent.grade)
    print("ID Number:", newStudent.ID)
    print("Address:", newStudent.address)
    print("Age:", newStudent.age)
    print("Locker Number:", newStudent.lockerNumber)

def getNumberOfStudents():
    number = len(listOfHomeroomStudents)
    return number
def searchListForStudents(searchName):
    for counter in listOfHomeroomStudents:
        if searchName == counter.name:
            print("This student is on the list.")
            return
    print("This student is not on the list.")

def getStudentAddress(searchName):
    for counter in listOfHomeroomStudents:
        if searchName == counter.name:
            print("This student's address is", counter.address)
    
def getStudentBasicInfo(searchName):
    for counter in listOfHomeroomStudents:
        if searchName == counter.name:
            print("This student's grade is", counter.grade)
            print("This student's ID is", counter.ID)
            print(getStudentAddress(searchName))
            print("This student's age is", counter.age)
            print("This student's locker number is", counter.lockerNumber)
def listHomeroomStudents():
    print("Now Showing The List of Homeroom Students")
    #print(listOfHomeroomStudents)
    for counter in listOfHomeroomStudents:
        print(counter.name)

#MAIN CODE
while True:
    print("What would you like to do:")
    print("1: View Homeroom Roster")
    print("2: Add student to homeroom")
    print("3: Remove student from homeroom")
    print("4: Get a sudent's ID Number")
    print("5: See number if sudents in homeroom")
    print("6: See basic student information")
    print("7: See if a student is on the homeroom list")
    print("8: Exit program")
    choice = int(input("->"))
    if choice == 1:
        # See list of studenta
        print("You selected to see the lsit of homeroom students")
        listHomeroomStudents()
    elif choice == 2:
        # Add students to homerooom
        addToHomeroom()
    elif choice == 3:
        # Remove student from homeroom
        pass
    elif choice == 4:
        #Get sudents ID number
        pass
    elif choice == 5:
        # Get number of students
        print("Getting number of Homeroom Students")
        print(getNumberOfStudents())
    elif choice == 6:
        # See basic info about student
        print("getting information about this student...")
    elif choice == 7:
        # Search on roster to see if student is on it
        print("What student would you like to search for?")
        searchName = input("->")
        searchListForStudents(searchName)
    elif choice == 8:
        # Quit program
        break
    else: 
        print("An error has occured")


print("Thanks for using the homeroom software")