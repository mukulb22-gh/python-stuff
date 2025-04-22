# 1. Simple class creation and getter setter method
#### Filename : cls.py

`class` keyword use to create a class in python language. 

`def` keyword use to create a function/method in python language. 

`__init__` is special method called constructor method in python.

By default every function of a class contain first argument as `self`.

Below is the syntax of class and method creation in python.


    class ClassName:

        def __init__(self):
            pass

        def method_call(self):
            print("Calling from method_call method")

----
# 2. Inheritence in python language.
#### Filename : inheritence.py
One class inherit the properties and behaviours of another class. 

The class which inherit other class called `Child Class` 

And the class that get inherited called `Parent Class` or `Base Class`.

Syntax of `parent and child` class in python language.

    # Parent Class
    class ParentClassName:
        {Parent class body}

    # Child Class
    class ChildClassName(ParentClassName):
        {Child class body}


This is also called `Single Inheritence` in python language.

----
# 3. Multiple Inheritence in python language.
#### Filename : multiple_inheritence.py

One class inherit the properties and behaviours of multiple classes. 

Syntax of `mutliple inheritence parent and child` class in python language.

    # Parent Class
    class ParentClass1:
        {Parent class body}

    class ParentClass2:
        {Parent class body}

    # Child Class
    class ChildClassName(ParentClass1[, ParentClass2, ...] ):
        {Child class body}

---

# 3. Multilevel Inheritence in python language.
#### Filename : multilevel_inheritence.py

Suppose class `A` is the parent of class `B` and class `B` is the parent of class `C`.

So when class `C` inherit from `B` it also inherit from `A` class.

For example :- GrandParents -> Parents -> Child

    Challenge Time:-

    If commenting  these lines of code

    #cityObj.setCountry("Bharat")
    #cityObj.setState("Punjab")
    #cityObj.setCity("Chandigarh")
    #super().__init__()   Line no: 15, 27

    What will be the output and Why?


Output :- Throwing error  

    print("The country is: ", self.country)
    AttributeError: 'City' object has no attribute 'country' 

 Reason:-
 
    When cityObj = City() is executed, only City.__init__ runs completely. It doesn't trigger State.__init__, which in turn doesn't trigger Country.__init__. Therefore, the line self.country = "India" inside Country.__init__ is never executed for the cityObj

    The Error Call: When you later call cityObj.getCountry(), this method (inherited from Country) tries to access self.country. Since self.country was never assigned to the cityObj during initialization, Python raises the AttributeError.


# 4. Encapsulation in python language.
#### Filename : encapsulation.py

    Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to:

    Bundling:
    Combining data (attributes) and the methods (functions) that operate on that data 
    within a single unit (a class).

    Data Hiding / Information Hiding: 
    Restricting direct access to some of an object's components 
    (typically its internal data/attributes). Access to this data is usually controlled through 
    public methods (like getters and setters or other methods that use the data).


# 5. Polymorphism in python language.
#### Filename : polymorphism.py

    Polymorphism word come through combine two words `Poly` means `many` and `morphism` means `form`.
    It allows objects of different classes to respond to the same method call in their own specific way.
    If parent class method is overridden by child class method with different business logic, the base class method is a polymorphic method.

    Four ways of polymorphism:-
    1. Duck Typing 
    2. Operator Overloading
    3. Method Overloading
    4. Method Overriding

    Duck Typing:- The principle of duck typing is: "If it walks like a duck and quacks like a duck, then it must be a duck. In programming terms, if an object has the necessary methods and attributes, Python doesn't care about its actual class. It will happily call those methods.

    Operator Overloading:- Python allows you to redefine the behavior of built-in operators like +, -, *, etc., for your own classes. This is another form of polymorphism.

    Method overloading:- is a feature of object-oriented programming where a class can have multiple methods with the same name but different parameters. To overload method, we must change the number of parameters or the type of parameters.

    Method Overriding:- When a subclass redefine the method of superclass. This is called as Method Overriding.


---
# 6 Abstraction
#### Filename : abstraction.py

    Abstraction :- Abstraction in object-oriented programming is about hiding complex implementation details and showing only the essential information to the user.

    An abstract class is a class that:-
    . Cannot be instantiated directly. You cannot create objects of an abstract class.   
    . May contain abstract methods. An abstract method is a method declared but without an implementation in the abstract class. 
    . Subclasses must provide concrete implementations for all abstract methods.   


Python's abc (Abstract Base Classes) module provides the necessary tools to define abstract classes and abstract methods. You use the abc.ABC as a metaclass for your abstract class and the @abc.abstractmethod decorator to declare abstract methods

    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def make_sound(self):
            pass
        
        def how_many_legs(self,legs)
            return legs


    # working class as implement the abstract method 
    class Dog(Animal):
        def make_sound(self):
            print("Woof!")


    # Error in class as not implemented abstract method 
    class Cat(Animal):
        def how_many_legs(legs):
            return legs

---









     
