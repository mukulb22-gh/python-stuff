#singleton pattern example
class SingletonCls:
    __myinstance = None

    def __init__(self):
        if SingletonCls.__myinstance is not None:
            raise Exception("SingletonCls cannot be instantiated more than once!")
        else :
            SingletonCls.__myinstance = self

    @staticmethod
    def get_the_instance():
        if SingletonCls.__myinstance is None:
            SingletonCls() # instantiate SingeltonCls then
        return SingletonCls.__myinstance

       
#initialize objects
obj1 = SingletonCls()
print("obj1 :", obj1)

#get the objects directly
obj2 = SingletonCls.get_the_instance()
print("obj2 :", obj2)

#Compare objects
if (obj1 == obj2) :
    print("same instance were used :", obj)

