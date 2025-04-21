"""
Polymorphism:
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