name = "John"
date_of_birth = "2005-10-15"
age = 25
location = "London"
country = "UK"
weight = 70.5
year_of_study = 2025
student_id = "12345"
classes = ["Math", "Science", "English"]
marks = {"Math": 10, "Science": 20, "English": 30, }
majors = ("Math", "Science", "English")
minors = (("History", "Geography"), ("Biology", "Chemistry"))

def getName(name):
    return name

def getProfile(name, age, location, country, date_of_birth):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My location is {location}")
    print(f"My country is {country}")
    print(f"My date of birth is {date_of_birth}")

def getClasses(classes):
   for i in classes:
       print(f"I am doing {i}")

def getMarks(marks):
   for key, value in marks.items():
       print(f"I got {value} in {key}")
   for mark in marks.values():
       print(f"I got {mark}")
   for key in marks.keys():
       print(f"I got {key}")

def getGrade(marks):
    for key, value in marks.items():
        if value >= 90:
            print(f"I got {value} in {key} which is an A")
        elif value >= 80:
            print(f"I got {value} in {key} which is a B")
        elif value >= 70 and value < 75:
            print(f"I got {value} in {key} which is a C")
        elif value >= 60 and value < 70:
            print(f"I got {value} in {key} which is a D")
        else:
            print(f"I got {value} in {key} which is an F")


my_name = getName("Marie")
print(f"My name is {my_name}")
getGrade(marks)

# 1. Prints out my majors
# 2. Prints out my Minors
# 3. Use a while loop to ask the user to enter the information they want and close when the user types close

# here is the code for the assignment
# Function to print majors
def getMajors(majors):
    print("My Majors are:")
    for major in majors:
        print(major)

# Function to print minors
def getMinors(minors):
    print("My Minors are:")
    for group in minors:
        for minor in group:
            print(minor)

# Calling the functions
getMajors(majors)
getMinors(minors)

# While loop for user interaction
while True:
    user_input = input(
        "\nEnter what you want to see "
        "(profile/classes/marks/grades/majors/minors) "
        "or type 'close' to exit: "
    )

    if user_input.lower() == "close":
        print("Program closed.")
        break

    elif user_input.lower() == "profile":
        getProfile(name, age, location, country, date_of_birth)

    elif user_input.lower() == "classes":
        getClasses(classes)

    elif user_input.lower() == "marks":
        getMarks(marks)

    elif user_input.lower() == "grades":
        getGrade(marks)

    elif user_input.lower() == "majors":
        getMajors(majors)

    elif user_input.lower() == "minors":
        getMinors(minors)

    else:
        print("Invalid option. Try again.")