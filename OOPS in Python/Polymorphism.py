import math
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        super().__init__('Circle')
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self,w,h):
        super().__init__("Rectangle")
        self.width = w
        self.height = h 
    def area(self):
        return self.width* self.height
def calculate_Area(s):
    return f"The area of {s.name} is {s.area()}"
c = Circle(15)
r = Rectangle(5,12)
print(calculate_Area(c))
print(calculate_Area(r))