class Country:
    def __init__(self):
        self.country = "India"

    def getCountry(self):
        print("The country is: ", self.country)

    def setCountry(self, country):
        self.country = country


class State(Country):
    def __init__(self):
        self.state = "Haryana"
        super().__init__()

    def getState(self):
        print( "The state is : ", self.state)

    def setState(self, state):
        self.state = state


class City(State):
    def __init__(self):
        self.city = "Faridabad"
        super().__init__()

    def getCity(self):
        print( "The ciity is : ", self.city)

    def setCity(self, city):
        self.city = city


### CityObject initiate
cityObj = City()

### Call and set setters method

# cityObj.setCountry("Bharat")
# cityObj.setState("Punjab")
# cityObj.setCity("Chandigarh")

cityObj.getCountry()
cityObj.getState()
cityObj.getCity()


# output:
# The country is:  Bharat
# The state is:  Punjab
# The city is:  Chandigarh

# Without set country, state, city
# The country is:  India
# The state is:  Haryana
# The city is:  Faridabad


"""
Challenge Time:-

If commenting  these lines of code

#cityObj.setCountry("Bharat")
#cityObj.setState("Punjab")
#cityObj.setCity("Chandigarh")
#super().__init__()   Line no: 15, 27

What will be the output and Why?

Ans: .readme
"""