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

def printMajors(majors):
    print("Majors:")
    for major in majors:
        print(f"- {major}")


def printMinors(minors):
    print("Minors:")
    for group in minors:
        print("- " + ", ".join(group))


my_name = getName("Marie")
print(f"My name is {my_name}")
getGrade(marks)

print("\n1. Prints out my majors")
print("2. Prints out my minors")
print("3. Use a while loop to ask the user what information they want and close when the user types 'close'.")

def show_menu():
    print("\nChoose what information you want:")
    print("  profile - see basic profile")
    print("  classes - see class list")
    print("  marks - see marks details")
    print("  grades - see grade letters")
    print("  majors - see majors")
    print("  minors - see minors")
    print("  close - exit the program")

if __name__ == "__main__":
    show_menu()

    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice == "close":
            print("Closing program. Goodbye!")
            break
        elif choice == "profile":
            getProfile(name, age, location, country, date_of_birth)
        elif choice == "classes":
            getClasses(classes)
        elif choice == "marks":
            getMarks(marks)
        elif choice == "grades":
            getGrade(marks)
        elif choice == "majors":
            printMajors(majors)
        elif choice == "minors":
            printMinors(minors)
        else:
            print("Unknown option. Please type one of the menu choices or 'close'.")