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

getClasses(classes)

# 1. Prints out my majors

#This function prints out the majors I'm doing in one line using the join method.
def print_majors(majors):
    if len(majors) == 1:
        print(f"I am doing {majors[0]} as a major.")
    else:
        all_but_last = ", ".join(majors[:-1])
        print(f"I am doing {all_but_last} and {majors[-1]} as majors.")

# 2. Prints out my Minors

#This function uses a recursive approach to flatten out the nested mminors tuple.
def flatten(items):
    flattened = []
    for item in items:
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

#This function prints out the minors I'm doing in one line using the join method.
def print_minors(minors):
    flattened_minors = flatten(minors)
    if len(flattened_minors) == 1:
        print(f"I am doing {flattened_minors[0]} as a minor.")
    else:
        all_but_last = ", ".join(flattened_minors[:-1])
        print(f"I am doing {all_but_last} and {flattened_minors[-1]} as minors.")

# 3. Use a while loop to ask the user to enter the information they want and close when the user types close

#While loop to ask the user to enter the information they want and close when the user types close
def user_input():
    print("\nType one of the following to get information:")
    print(" 'name' - Get name")
    print(" 'profile' - Get profile")
    print(" 'classes' - Get classes")
    print(" 'marks' - Get marks")
    print(" 'grade' - Get grade")
    print(" 'majors' - Get majors")
    print(" 'minors' - Get minors") 
    print(" 'close' - Exit")

    while True:
        user_choice = input("\nEnter what you want to see: ").lower()
        
        if user_choice == "close":
            print("Exiting the program. Goodbye!")
            break

        elif user_choice == "name":
            print(f"My name is {my_name}")
        elif user_choice == "profile":
            getProfile(my_name, age, location, country, date_of_birth)
        elif user_choice == "classes":
            getClasses(classes)
        elif user_choice == "marks":
            getMarks(marks)
        elif user_choice == "grade":
            getGrade(marks)
        elif user_choice == "majors":
            print_majors(majors)
        elif user_choice == "minors":
            print_minors(minors)
        
        else:
            print("Invalid choice. Please try again.")

print_majors(majors)
print_minors(minors)
user_input()
