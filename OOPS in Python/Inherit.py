class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def get_info(self):
        return f"name: {self.name}, age: {self.age}"
class Student(Person):    
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def get_student_info(self):
        print(f"student id: {self.student_id}")

p1 = Person('Raman', 30)
stu1 = Student('Ron', 20, 'S12345')
print(p1.get_info())
print(stu1.get_info())
stu1.get_student_info()