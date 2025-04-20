class MyCls:

    #Constructor with name parameter required
    def __init__(self, name):
        self.name = name

    #Getter
    def get_name(self):
        return self.name

    #Setter
    def set_name(self, name):
        self.name = name

#Create class object
clsObj = MyCls("Ram")
print(clsObj.get_name()) # get name // Ram
clsObj.set_name("Shyam") # set name 
print(clsObj.get_name()) # get name // Shyam

