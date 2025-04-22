"""
Polymorphism:
Duck typing:-
"""
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Chirp!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
bird = Bird()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird) # Output: Chirp!

"""
Operator Overloading:-

"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # The __add__ method is called

print(p3)  # Output: (4, 6)

"""
Method Overloading:-
"""
class MethodOverloadingError:
    def add(self, a, b):
        x = a+b
        return x
    
    #python consider only below function definitions
    def add(self, a, b, c):
        x = a+b+c
        return x

moeObj = MethodOverloadingError()

print (moeObj.add(10,20,30))
#print (moeObj.add(10,20)) # Throw error as python considered only latest definition

class MethodOverloading:
    def add(self, a = None, b = None, c = None):
        x=0
        if a !=None and b != None and c != None:
            x = a+b+c
        elif a !=None and b != None and c == None:
            x = a+b
        return x

moObj = MethodOverloading()
print (moObj.add(10,20,30))


"""
Method Overriding:-
"""

class AnyShape:
    def area(self):
        return "Shape is not defined"


class Rectangle(AnyShape):
    def __init__(self, len, breadth):
        self.length = len
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(AnyShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rectObj = Rectangle(10, 20)
circleObj = Circle(5)

print(rectObj.area())  # Output: 200
print(circleObj.area())  # Output: 78.5
