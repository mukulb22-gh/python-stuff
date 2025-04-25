from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class Elephant(Animal):
    def voice(self):
        return "Toot toot!"

class Lion(Animal):
    def voice(self):
        return "Roar!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class ElephantFactory(AnimalFactory):
    def create_animal(self):
        return Elephant()

class LionFactory(AnimalFactory):
    def create_animal(self):
        return Lion()

# Example usage
elephant_factory = ElephantFactory()
elephant = elephant_factory.create_animal()
print(elephant.voice())

lion_factory = LionFactory()
lion = lion_factory.create_animal()
print(lion.voice())

