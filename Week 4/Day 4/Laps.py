# continut day3 laps -
# Lap 5
# Name-Mangling
# property
# HW
class Student :

    # __enrolled = True
    def __init__(self , name , enrolled):
        self.name = name
        self.score = []
        self.__enrolled = True

    def add_score(self , score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100 ")
        self.score.append(score)
        
        # Getter
    @property
    def enrolled(self):
        return self.__enrolled

        # Setter
    @enrolled.setter
    def enrolled(self , status):
        self.__enrolled = status

    @property
    def average(self):
        if not self.score:
            return 0
        else:
            return sum(self.score) / len (self.score)
        
student = Student("Sarah" , None)
student.add_score(80)
student.add_score(90)
student.add_score(100)

print(student.average)
# print(student._Student__enrolled) # اذا ابي غصب يطلع
# print(student.__enrolled) #ماراح يطلع 

student.enrolled = False
student.enrolled = True
print(student.enrolled)
print(student.score)
# --------------------------------------------------
# Lap 6

class Food:
    def __init__(self , name):
        self.name = name

    def showName(self):
        return self.name

class Fruites(Food):
    newName = "    Fa      "
    def __init__(self, name ,cal):
        super().__init__(name)
        self.cal = cal

    @staticmethod
    def strpName(newName):
        return newName.strip()

myFruite = Fruites("Apple" , 200)
print(myFruite.showName())
print(myFruite.strpName("    Fa      "))