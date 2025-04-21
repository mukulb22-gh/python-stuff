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