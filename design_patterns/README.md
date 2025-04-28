# Creational pattern :-

### o Singleton Design Pattern  
    
    Singleton design pattern ensures that the object instance can be created only once.
    If object required to use then it return the existing instance.

    File = singleton.py
    
 
### o Factory Design Pattern  

    In factory design pattern we create object without exposing the creation logic and 
    refer to newly created object using an common interface

    File = factory.py


### o Abstract Factory Design Pattern  

    An interface is responsible for creating factory related objects without explicitly specifying the classes. Each generated factory can give the objects as per the factory patterns.

    File = abstract_factory.py


### o Prototype Design Pattern  

    It refers to creating duplicate object while keeping performance in mind. 
    Create a clone of current object.

    File = prototype.py

---
# Structural Design Patterns :-

### o Adapter Design Pattern  

    Adapter design pattern it work as a bridge between two incompatible interfaces.
    Eg: Same mobile charger can charge the Ctype, Dtype, thinpin , fatpin charger.

    File = adapter.py


### o Composite Design Pattern  

    It is used when we need to treat a group of objects in similar way as a single object.

    File = composite.py


### o Filter Design Pattern  

    In software is like having a set of rules to pick out specific objects from a larger collection based on the certain criteria.

    File = filter.py


### o Decorator Design Pattern 

    The Decorator pattern allows you to attach new behaviors or responsibilities to objects dynamically without altering their original code.

    File = decorator.py


### o Proxy Design Pattern 

    In this pattern, a class represent functionality of another class. We create object having original object to interface its functionality to outer world.

    USE CASE:

    1) Access Control (Protection Proxy): Like in this example, the proxy can check if the client has the necessary permissions before allowing access to the real object's methods or data.
    2) Lazy Initialization (Virtual Proxy): The proxy can delay the creation of an expensive real object until it's actually needed.
    3) Logging (Logging Proxy): The proxy can log requests made to the real object.
    4) Caching (Caching Proxy): The proxy can cache results from the real object to avoid repeated expensive operations.
    5) Remote Proxy: Represents an object that exists in a different address space (like on a server).

    File = proxy.py


### o Flyweight Design Pattern 

    The Flyweight pattern is a structural pattern focused on minimizing memory usage or computational expense by sharing as much common data as possible between multiple objects. Instead of each object storing all its data, objects share the common, immutable parts (called intrinsic state) and receive the unique, context-dependent parts (called extrinsic state) when needed.

    File = flyweight.py