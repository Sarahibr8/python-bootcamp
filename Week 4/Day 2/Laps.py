class Dog():
    _legs = 4

    def __init__(self , name):
        self.name = name

    def getLegs(self):
        return self._legs

    def setLegs(self , number):
        self._legs = number



myDog = Dog("Slugi")
myDog.setLegs(93)
print(myDog.getLegs())
