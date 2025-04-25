from abc import ABC, abstractmethod
import random

# 1. Target Interface: What the client system expects
class Animal(ABC):
    """Target Interface: Defines how the system interacts with animals."""
    @abstractmethod
    def speak(self):
        pass

# 2. Adaptee: The existing class with an incompatible interface
class Bird:
    """Adaptee: Represents a bird with its own specific methods."""
    def __init__(self, species="Sparrow"):
        self.species = species

    def tweet(self):
        return f"{self.species} says: Tweet tweet!"

    def chirp_volume(self):
        # Birds might have varying chirp volumes
        return random.randint(1, 10)

# 3. Adapter: Implements the Target interface and wraps the Adaptee
class BirdAdapter(Animal):
    """Adapter: Makes the Bird compatible with the Animal interface."""
    def __init__(self, bird: Bird):
        self._bird = bird # Composition: Adapter holds an instance of Adaptee

    def speak(self):
        # Translation: Call the adaptee's relevant method(s)
        print(f"Adapter: Translating 'speak' call for a {self._bird.species}.")
        # We can even combine information from multiple adaptee methods if needed
        volume = self._bird.chirp_volume()
        base_sound = self._bird.tweet()
        return f"{base_sound} (Volume: {volume})"

# 4. Client Code: Interacts with the Target interface
def make_animal_speak(animal: Animal):
    """Client code that expects any object conforming to the Animal interface."""
    print("-" * 25)
    print("Client: Requesting the animal to speak...")
    sound = animal.speak()
    print(f"Client: Heard: '{sound}'")
    print("-" * 25)

# --- Usage ---

# Create an instance of the Adaptee (the object with the incompatible interface)
my_bird = Bird("Robin")

# Create the Adapter, wrapping the Adaptee
bird_adapter = BirdAdapter(my_bird)

# The client code uses the Adapter as if it's a standard Animal
make_animal_speak(bird_adapter)

# For comparison, let's create a class that directly implements the Animal interface
class Lion(Animal):
    def speak(self):
        return "Roar!"

my_lion = Lion()
make_animal_speak(my_lion) # Client code works the same way
