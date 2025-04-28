# structural proxy patter example on students
"""
The Proxy pattern provides a surrogate or placeholder for another object 
(the "real subject") to control access to it. Instead of interacting directly 
with the real object, the client interacts with the proxy. The proxy looks and 
acts like the real object (implementing the same interface) but can add extra 
logic before or after delegating the request to the real object.

USE CASE:

1) Access Control (Protection Proxy): Like in this example, the proxy can check if the client has the necessary permissions before allowing access to the real object's methods or data.
2) Lazy Initialization (Virtual Proxy): The proxy can delay the creation of an expensive real object until it's actually needed.
3) Logging (Logging Proxy): The proxy can log requests made to the real object.
4) Caching (Caching Proxy): The proxy can cache results from the real object to avoid repeated expensive operations.
5) Remote Proxy: Represents an object that exists in a different address space (like on a server).
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentProxy:
    def __init__(self, student):
        self.student = student

    def get_info(self):
        if self.student.grade >= 7:
            return self.student.get_info()
        else:
            return "Access denied: Student's grade is below 7"


if __name__ == "__main__":
    student1 = Student("Alice", 15, 8)
    student2 = Student("Bob", 14, 6)

    proxy1 = StudentProxy(student1)
    proxy2 = StudentProxy(student2)

    print(proxy1.get_info())
    print(proxy2.get_info())
    print(student1.get_info())
    print(student2.get_info())