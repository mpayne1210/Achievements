# Name: task7.py
# Author: Michael Payne
# Date Created: October 25, 2022
# Date Last Modified: October 29, 2022
# Purpose: The purpose of this program is to allow a student to register for up to 4 courses from a given list.  It will take the users information, including
#          first name, last name, and student number.  Then it will display the available courses and ask for the student to make their selection. It will then
#          display the students name, student number, and the courses code and course names of all programs selected.
          
# This is the dictionary of available programs.
available_courses = {"PROG1344" : "Programming" , "HIST1885" : "History" , "CHEM1121" : "Chemistry" , "COMP3385" : "Networking"}

# This creates a dictionary for the student.  Currently there are no values for the keys.
student = {"First Name    " : "" , "Last Name     " : "" , "Student Number" : ""}

print("Are you ready to enroll in courses? "" \n")

# Below gathers the information from the student.  It will capitilize the first letter of the name, and remove any blank spaces.
firstName = input("Please enter your first name: ").capitalize().strip()
student["First Name    "] = firstName # As the information is collected, it is added to the dictionary holding the students information.

while not firstName.isalpha(): # This makes sure the name entered is letters.

    firstName = input("Please enter a valid first name: ").capitlize().strip()

lastName = input("Please enter your last name: ").capitalize().strip()
student["Last Name     "] = lastName

while not lastName.isalpha():

    lastName = input("Please enter a valid last name: ").capitalize().strip()

studentNumber = input("Please enter your 7-digit student number: ").strip()
student["Student Number"] = studentNumber

while not studentNumber.isnumeric(): # This makes sure that the student number is entered correctly as numbers.

    studentNumber = input("Please enter a valid student number: ").strip()

while len(studentNumber) != 7: # This makes sure that the student number entered is valid containing the required 7 characters.

    studentNumber = input("Student Number must be 7 digits:").strip()

# Below displays the courses that are available.
print()
print("Here is what is currently open for registration:" "\n")
print("Course Code \t Course Name")
print("----------- \t -----------")

for course , code in available_courses.items(): # This is a loop that will display each of the items in the available courses dictionary.

    print (course , "\t", code)

print()

# This takes the courses that the student wants to register for.
selection = input("Please enter the course codes for the programs you would like to register for separated by commas: ").upper().strip()     

courses = selection.split(",") # This tells the program where to separate the string of input and creates a list of the requested courses

# This is where the confirmation starts to be printed back to the student.
print()
print("****Confirmation****")
print()

# This loop prints out the students information, including first name, last name, and student number.
for a, b in student.items():

    print(a, "\t", b)

print()

# This loop compares each item in the list of selected courses with the dictionary containing the available courses. If the requested course is a match
# to an available course the program will display that they are enrolled in that program.  The course code and course name are displayed. 
for x in courses:
    
    while x in available_courses:

        output = available_courses[x]

        print("Enrolled --  {} {}".format(x, output))
        print()

        break

    while x not in available_courses: # If one of the course codes entered is not in the available course list, it will display what was entered with a message
                                      # that it does not exist in the system.

        print("*** \"",x,"\"", "does not match an available course code ***")

        break


   



