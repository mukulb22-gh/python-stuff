from abc import ABC, abstractmethod
from typing import List

# 1. Component Interface
class AnimalComponent(ABC):
    """
    The base Component interface declares common operations for both
    simple (Leaf) and complex (Composite) objects of a composition.
    """
    def parent(self) -> 'AnimalComponent':
        return self._parent

    def parent(self, parent: 'AnimalComponent'):
        self._parent = parent

    def add(self, component: 'AnimalComponent') -> None:
        # Default behavior: leaves can't add children
        pass

    def remove(self, component: 'AnimalComponent') -> None:
        # Default behavior: leaves don't have children to remove
        pass

    def is_composite(self) -> bool:
        # Helper to distinguish composites from leaves
        return False

    @abstractmethod
    def make_sound(self) -> str:
        """A common operation for all animals/groups."""
        pass

    @abstractmethod
    def display_details(self, indent: str = "") -> None:
        """Another common operation to display structure."""
        pass


# 2. Leaf: Represents individual animals
class LeafAnimal(AnimalComponent):
    """
    The Leaf class represents the end objects of a composition.
    A leaf can't have any children.
    It does the actual work (like making a specific sound).
    """
    def __init__(self, species: str, sound: str):
        self.species = species
        self._sound = sound
        self._parent = None # Optional: reference back to parent

    def make_sound(self) -> str:
        return f"{self.species} says: {self._sound}"

    def display_details(self, indent: str = "") -> None:
        print(f"{indent}- {self.species}")


# 3. Composite: Represents a group of animals
class AnimalGroup(AnimalComponent):
    """
    The Composite class represents complex components that may have children.
    Composite objects usually delegate the actual work to their children and
    then "sum up" the result.
    """
    def __init__(self, name: str):
        self.name = name
        self._children: List[AnimalComponent] = []
        self._parent = None # Optional: reference back to parent

    def add(self, component: AnimalComponent) -> None:
        self._children.append(component)
        component.parent = self # Set the parent reference

    def remove(self, component: AnimalComponent) -> None:
        self._children.remove(component)
        component.parent = None # Remove parent reference

    def is_composite(self) -> bool:
        return True

    def make_sound(self) -> str:
        """Delegates sound making to children."""
        results = []
        for child in self._children:
            results.append(child.make_sound())
        # Combine sounds (could be more complex logic)
        return f"Group '{self.name}' sounds: [\n  " + "\n  ".join(results) + "\n]"


    def display_details(self, indent: str = "") -> None:
        """Display the group name and display children details  recursively ."""
        print(f"{indent}+ Group: {self.name}")
        for child in self._children:
            child.display_details(indent + "  ")


# 4. Client Code
def client_code(component: AnimalComponent):
    """
    The client code works with all components via the base interface.
    It doesn't need to know the concrete class of the objects it works with.
    """
    print("\n--- Client: Making Sound ---")
    print(component.make_sound())

    print("\n--- Client: Showing Details ---")
    component.display_details()
    print("-" * 30)

# --- Usage ---

# Create individual animals (Leaves)
lion1 = LeafAnimal("Lion", "Roar!")
lion2 = LeafAnimal("Lion", "Grrrr!")
elephant1 = LeafAnimal("Elephant", "Toot toot!")
monkey1 = LeafAnimal("Monkey", "Ooh ooh aah aah!")

# Create groups (Composites)
savanna_enclosure = AnimalGroup("Savanna Enclosure")
pride_rock = AnimalGroup("Pride Rock") # A subgroup

# Build the tree structure
pride_rock.add(lion1)
pride_rock.add(lion2)

savanna_enclosure.add(pride_rock) # Add a composite to another composite
savanna_enclosure.add(elephant1)

# Create another top-level group
jungle_enclosure = AnimalGroup("Jungle Enclosure")
jungle_enclosure.add(monkey1)

# Create the overall zoo structure
zoo = AnimalGroup("My Zoo")
zoo.add(savanna_enclosure)
zoo.add(jungle_enclosure)

# --- Client Interaction ---

# Client interacts with a single leaf
print("Interacting with a single Lion:")
client_code(lion1)

# Client interacts with a composite group
print("\nInteracting with the Pride Rock group:")
client_code(pride_rock)

# Client interacts with a larger composite group
print("\nInteracting with the Savanna Enclosure:")
client_code(savanna_enclosure)

# Client interacts with the entire zoo structure
print("\nInteracting with the whole Zoo:")
client_code(zoo)
