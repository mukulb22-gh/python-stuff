# Structural design pattern:
# Filter or Criteria pattern example
"""
The Filter pattern allows you to decouple the filtering logic 
from the objects being filtered. It enables you to select a 
subset of objects from a collection based on different criteria, 
and importantly, allows you to combine these criteria in various 
ways (like using AND, OR logic) without modifying the core object 
classes or the filtering classes themselves.
"""
from abc import ABC, abstractmethod

#Animal abstract class
class Animal(ABC):
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    @abstractmethod
    def sound(self):
        pass

#Dog concrete class inherit Animal class
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def sound(self):
        return "Woof!"

#Cat concrete class inherit Animal class
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cat", age)

    def sound(self):
        return "Meow!"

#Filter abstract class
class Filter(ABC):
    @abstractmethod
    def filter(self, animals):
        pass

#Concrete filter classes
class SpeciesFilter(Filter):
    def __init__(self, species):
        self.species = species

    
    def filter(self, animals):
        """
        Filter method :create and return a new list containing only 
            animals whose species attribute matches the one stored in 
            the filter instance.
        """
        return [animal for animal in animals if animal.species == self.species]

class AgeFilter(Filter):
    def __init__(self, age):
        self.age = age

    #Age Filter like species
    def filter(self, animals):
        return [animal for animal in animals if animal.age > self.age]


#This is a key part of the pattern, allowing criteria combination. 
#It also implements the Filter interface
class AndFilter(Filter):
    def __init__(self, filter1, filter2):
        self.filter1 = filter1
        self.filter2 = filter2

    def filter(self, animals):
        return self.filter2.filter(self.filter1.filter(animals))

#Filter patter use and demonstration
if __name__ == "__main__":
    animals = [
        Dog("Buddy", 3),
        Cat("Whiskers", 5),
        Dog("Max", 7),
        Cat("Mittens", 2),
        Dog("Charlie", 10)
    ]

    dog_filter = SpeciesFilter("Dog")
    old_filter = AgeFilter(4)
    old_dogs_filter = AndFilter(dog_filter, old_filter)

    dogs = dog_filter.filter(animals)
    print("Dogs:")
    for dog in dogs:
        print(f"- {dog.name} ({dog.age} years old)")

    old_animals = old_filter.filter(animals)
    print("\nOld animals:")
    for animal in old_animals:
        print(f"- {animal.name} ({animal.age} years old)")

    old_dogs = old_dogs_filter.filter(animals)
    print("\nOld dogs:")
    for dog in old_dogs:
        print(f"- {dog.name} ({dog.age} years old)")
        
