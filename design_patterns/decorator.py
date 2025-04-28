# Structural: Decorator pattern implementaion in animals
"""
The Decorator pattern allows you to attach new behaviors or responsibilities 
to objects dynamically without altering their original code.
"""

# Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"I am a {self.name}."

# Decorator classes
class AnimalDecorator:
    def __init__(self, animal):
        self.animal = animal

    def describe(self):
        return self.animal.describe()

# Concrete decorator classes
class FlyingDecorator(AnimalDecorator):
    def describe(self):
        return f"{super().describe()} I can fly."

# Concrete decorator classes
class SwimmingDecorator(AnimalDecorator):
    def describe(self):
        return f"{super().describe()} I can swim."

# Concrete decorator classes
class RunningDecorator(AnimalDecorator):
    def describe(self):
        return f"{super().describe()} I can run."

# Example usage
dog = Animal("Dog")
print(dog.describe())

flying_dog = FlyingDecorator(dog)
print(flying_dog.describe())

swimming_dog = SwimmingDecorator(dog)
print(swimming_dog.describe())

running_dog = RunningDecorator(dog)
print(running_dog.describe())

flying_swimming_dog = FlyingDecorator(SwimmingDecorator(dog))
print(flying_swimming_dog.describe())
