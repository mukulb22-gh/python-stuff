class ParentCls:

    def __init__(self):
        self.cls = "Parent Class"

    def method_call(self):
        print(self.cls)


#Child class inherit ParentCls method
class ChildClass(ParentCls):

    def __init__(self):
        self.cls = "Child Class"

    def child_method_call(self):
        print(self.cls)


#initate Child class object
chObj = ChildClass()
chObj.child_method_call()   #Child Class Method
#Parent method call
chObj.method_call()         #Child Class Calling Parent Class Method

#initate Parent class object
pObj = ParentCls()
pObj.method_call()          #Parent Class Method

ParentCls.method_call(chObj)    #Parent Class Method uses Child object to called

#output
# Child Class
# Child Class
# Parent Class
# Child Class