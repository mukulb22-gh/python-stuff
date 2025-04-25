#prototype design pattern with example
import copy

class PrototypeCls:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

# Example usage
original = PrototypeCls([1, 2, 3])
clone = original.clone()
clone.value.append(4)

print(f"Original: {original.value}")
print(f"Clone: {clone.value}")

