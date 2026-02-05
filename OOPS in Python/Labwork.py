# --- THE BLUEPRINTS (Classes) ---

class Person:
    def __init__(self, name, age):
        # 'self' refers to the specific person being created
        self._name = name   # Storing name internally
        self._age = age     # Storing age internally
        
    def get_info(self):
        # A shared way for any Person to describe themselves
        return f"{self._name}, age {self._age} yrs"

class Student(Person): # (Inheritance) Student gets everything Person has
    def __init__(self, name, age, student_id):
        # super() calls the Person's __init__ to handle name and age
        super().__init__(name, age) 
        self.student_id = student_id # Student adds their own unique ID
        
    def get_info(self):
        # Overriding: Calls the parent's info AND adds the ID to the end
        return f" student : {super().get_info()} ,ID : {self.student_id}"

class Teacher(Person): # (Inheritance) Teacher also gets Person's traits
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject # Teacher adds their specific teaching subject
        
    def get_info(self):
        return f"Teacher : {super().get_info()} ,Course : {self.subject}"

class Course:
    course_count = 0  # CLASS VARIABLE: Shared by all courses (the counter)
    
    def __init__(self, coursename):
        self.coursename = coursename
        self._students = []  # A private "container" (list) for this specific course
        self._teachers = []  # A private "container" (list) for teachers
        Course.course_count += 1 # Every time a course is made, add 1 to the counter
        
    def add_student(self, student):
        # Takes a Student OBJECT and puts it into the list
        self._students.append(student)
        
    def add_Teacher(self, teacher):
        # Takes a Teacher OBJECT and puts it into the list
        self._teachers.append(teacher)
        
    def get_all(self):
        # List Comprehension: Loops through lists and runs get_info() on everyone
        return {
            "students": [s.get_info() for s in self._students],
            "teachers": [t.get_info() for t in self._teachers]
        }    

    @classmethod
    def total_courses(cls):
        # Looks at the 'Course' blueprint itself to see the shared counter
        return cls.course_count

    @staticmethod
    def course_rules():
        # A simple "notice board" that doesn't need data from a specific course
        return " attendance should be greater than 90%"

# --- THE REAL WORLD (Objects) ---

# 1. We create two Course objects
courseda = Course("Data Analyst")
courseProgramming = Course("Programming")

# 2. We create People (The data is now packaged into objects)
s1 = Student('student1', 15, 'st101')
s2 = Student('student2', 18, 'st102')
t1 = Teacher("Teacher1", 34, 'IT')

# 3. We connect them (The Course list now points to these People)
courseProgramming.add_student(s1)
courseProgramming.add_student(s2)
courseProgramming.add_Teacher(t1)

# 4. We ask the objects to report their status
print(courseProgramming.get_all())
print("Total no of courses ",Course.total_courses())
print("Rule ::::",Course.course_rules()) 