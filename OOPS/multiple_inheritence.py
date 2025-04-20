#Parent Class 1
class Father:
    def __init__(self):
        self.fathername = "John"

    def father(self):
        print(self.fathername)

#Parent Class 2
class Mother:
    def __init__(self):
        self.mothername = "Merry"

    def mother(self):
        print(self.mothername)

#Child Class inherit multiple classes properties
class Child(Mother, Father):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
        print("Marlo parents names are %s , %s" % (self.fathername, self.mothername))

s1 = Child()
s1.parents()

# output
# Father : John 
# Mother : Merry
# Marlo parents names are John , Merry 