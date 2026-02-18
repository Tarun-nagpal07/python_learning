'''Create an abstract Shape class with an abstract method area(). Implement Circle,
Rectangle, and Triangle subclasses. Calculate and print areas for a mixed list of shapes.'''

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*self.r*self.r


class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b


class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        return 1/2*self.b *self.h


c = Circle(12)
r = Rectangle(10,20)
t = Triangle(12,2)


l = [c,r,t]
dir(c)
for i in l:
    print(f"{i.area()} is the area of {i.__class__.__name__}" )


