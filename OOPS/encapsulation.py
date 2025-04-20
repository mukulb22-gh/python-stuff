"""
Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to:

Bundling: Combining data (attributes) and the methods (functions) that operate on that data 
within a single unit (a class).

Data Hiding / Information Hiding: Restricting direct access to some of an object's components 
(typically its internal data/attributes). Access to this data is usually controlled through 
public methods (like getters and setters or other methods that use the data).
"""
class Student:

   def __init__(self, name="Vijay", marks=70):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Loki", 95)

s1.studentdata()
s2.studentdata()

# output
# Name: Vijay marks: 70
# Name: Loki marks: 95


# Name mangling
print ("Name: {} marks: {}".format(s1._Student__name, s1._Student__marks))
print ("Name: {} marks: {}".format(s2._Student__name, s2._Student__marks))

# output
# Name: Vijay marks: 70
# Name: Loki marks: 95


# NOT ACCESSEBLE
print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
print ("Name: {} marks: {}".format(s2.__name, __s2.marks))

# output
# AttributeError: 'Student' object has no attribute '__name'
# AttributeError: 'Student' object has no attribute '__marks'