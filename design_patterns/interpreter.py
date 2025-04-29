#Behaviour interpreter pattern with country and languages
from abc import ABC, abstractmethod

# Expression abstract class
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# Country expression class
class Country(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        context.set_country(self.name)

# Language expression class
class Language(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        context.set_language(self.name)

# Context class
class Context:
    def __init__(self):
        self.country = None
        self.language = None

    def set_country(self, country):
        self.country = country

    def set_language(self, language):
        self.language = language

    def get_country(self):
        return self.country

    def get_language(self):
        return self.language

    def __str__(self):
        return f"Country: {self.country}, Language: {self.language}"
        

obj = Context()
sentences = [Country("Spain"), Language("Spanish")]

for expression in sentences:
    expression.interpret(obj)

print(obj)

# obj.set_country("USA")
# obj.set_language("English")
# print(obj.__str__())

# obj.set_country("Spain")
# obj.set_language("Spanish")
# print(obj.__str__())
