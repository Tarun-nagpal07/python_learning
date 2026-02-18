'''Create a base Animal class with name and a speak() method. Subclass into Dog, Cat, and
Bird, each overriding speak(). Store all three in a list and call speak() in a loop.'''


class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("HAHA")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(self.name,"says Warfff")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(self.name,"says meowww")

class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        print(self.name,"says chiichii")


d = Dog('coco')
c = Cat('chili')
b = Bird('roman')

# l = [d,c,b]
l = [d.speak,c.speak,b.speak]

for i in l:
    # print(i)
    # print(type(i))
    i()
