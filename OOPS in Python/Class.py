class Person:
    def __init__(self,name):
        self.name =name
        print("constructor called")

    def hi(self):
        print("hi method of class person")
    def hello(self):
        print(f"hello {self.name}")

p1 = Person('Raman')
p2 =Person('Ron')
p1.hi()
p1.hello()
p2.hello()

 