 "John"
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
# 3. Use a while loop to ask the user to enter the information they want and close when the user types 
class Student:
    def __init__(self, name, age, location, country, date_of_birth, student_id, weight, year_of_study, majors, minors, classes, marks):
        self.name = name
        self.age = age
        self.location = location
        self.country = country
        self.date_of_birth = date_of_birth
        self.student_id = student_id
        self.weight = weight
        self.year_of_study = year_of_study
        self.majors = majors
        self.minors = minors
        self.classes = classes
        self.marks = marks

    def getProfile(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My location is {self.location}")
        print(f"My country is {self.country}")
        print(f"My date of birth is {self.date_of_birth}")

    def getClasses(self):
        for subject in self.classes:
            print(f"I am doing {subject}")

    def getMarks(self):
        for subject, mark in self.marks.items():
            print(f"I got {mark} in {subject}")

    def getGrade(self):
        for subject, mark in self.marks.items():
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            elif 70 <= mark < 75:
                grade = "C"
            elif 60 <= mark < 70:
                grade = "D"
            else:
                grade = "F"
            print(f"I got {mark} in {subject} which is a {grade}")

    def getMajors(self):
        for major in self.majors:
            print(f"My major is {major}")

    def getMinors(self):
        for minor_group in self.minors:
            for minor in minor_group:
                print(f"My minor is {minor}")


# Create a student object
student = Student(
    name="Marie",
    age=25,
    location="London",
    country="UK",
    date_of_birth="2005-10-15",
    student_id="12345",
    weight=70.5,
    year_of_study=2025,
    majors=("Math", "Science", "English"),
    minors=(("History", "Geography"), ("Biology", "Chemistry")),
    classes=["Math", "Science", "English"],
    marks={"Math": 10, "Science": 20, "English": 30}
)

# Interactive loop
while True:
    user_input = input("Enter the information you want (profile, majors, minors, classes, marks, grade) or type 'close' to exit: ").lower()
    
    if user_input == "close":
        print("Closing program...")
        break
    elif user_input == "profile":
        student.getProfile()
    elif user_input == "majors":
        student.getMajors()
    elif user_input == "minors":
        student.getMinors()
    elif user_input == "classes":
        student.getClasses()
    elif user_input == "marks":
        student.getMarks()
    elif user_input == "grade":
        student.getGrade()
    else:
        print("Invalid option, please try again.")
        
