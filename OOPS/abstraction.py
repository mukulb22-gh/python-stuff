"""
Abstraction :-  in object-oriented programming is about hiding complex implementation 
                details and showing only the essential information to the user.
"""

from abc import ABC, abstractmethod

class MyFamily(ABC):
    @abstractmethod
    def profession(self, profession):
        print("profession is: ", profession)
        return

    def salary(self):
        print("salary method")
        return


class MyFather(MyFamily):
    def profession(self, profession):
        print("profession is: ", profession)
        return

    def salary(self):
        print("salary is $100000")
        return


obj = MyFather()
obj.profession("Engineer")
obj.salary()

# output:
# profession is:  Engineer
# salary is $100000

#obj2 = MyFamily()  # It will throw error as we cannot instantiate abstractclass


class Mother(MyFamily):
    # Missing profession method implementations

    def salary():
        print("salary is $0");


# obj3 = Mother(); # TypeError: Can't instantiate abstract class Mother without an implementation for abstract method 'profession'