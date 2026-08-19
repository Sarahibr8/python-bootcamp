# class Student:
#     pass

# print(Student)
# print(type(Student))

# # -----------------------------------
# class Student:
#     pass

# student_one = Student()
# student_two = Student()

# print(student_one)
# print(student_one is student_two)
# # -----------------------------------

# class Student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score

# student = Student("Sara" , 92)

# print(student.name)
# print(student.score)

# # -----------------------------------
# class Student:
#     def __init__(self , name):
#         self.name = name

#     def introduce(self):
#         print(f"I am {self.name}")

# student = Student("Omar")
# student.introduce()

# # -----------------------------------
# class Student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score

# sara = Student("Sara" , 92)
# omar = Student("Omar" , 81)

# sara.score = 95

# print(sara.score)
# print(omar.score)
# print(omar is sara)
# print(isinstance(omar , Student))
# -----------------------------------
# class Student:
#     academy = "Tuwaiq Academy"

#     def __init__(self , name):
#         self.name = name

# sara = Student("Sara")
# # Student.academy = "T" اذا ابي اعدل عليها

# print(Student.academy)
# print(sara.academy)

# -----------------------------------
# class Student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score

#     def display_result(self):
#         print(self.name , self.score)

# student = Student("Lina" , 88)
# student.display_result()

# -----------------------------------
# class Counter:
#     def __init__(self):
#         self.value = 0

#     def increment(self):
#         self.value += 1

# counter = Counter()
# counter.increment()
# counter.increment()

# print(counter.value)

# -----------------------------------
# class Rectangle:
#     def __init__(self , width , heigth):
#         self.width = width
#         self.heigth = heigth

#     def area(self):
#         return self.width * self.heigth

# rectangle = Rectangle(5 , 3)
# print(rectangle.area())

# -----------------------------------
class BankAccount:
    def __init__(self , balance=0):
        self.balance = balance

    def withdraw(self , amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

account = BankAccount(500)
print(account.withdraw(200))
print(account.balance)
# -----------------------------------
class Student:
    def __init__(self , name , score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

student = Student("Sara" , 95)
print(student)
# -----------------------------------
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()

first.increment()

print(first.value)
print(second.value)
# -----------------------------------
class Student:
    def __init__(self , name):
        self.name = name

    def greet(self):
        return f"Hello , {self.name}"

students = [
    Student("Sara"),
    Student("Omar"),
    Student("Lina")
]
for student in students:
    print(student.greet())
    # print(students[0].greet())

# -----------------------------------
class Student:
    pass

student = Student()
print(type(student))
print(type(student) is Student)
print(isinstance(student , Student))

# -----------------------------------
class Student:
    def __init__(self , name , score):
        self.name = name
        self._score = score

    # @property 
    # def score(self):
    #     return self.__score

student = Student("Sara" , 95)
student.__score = 45
print(student.name)
print(student._score)
# -----------------------------------
class Student:
    def __init__(self , name , scores):
        self.name = name
        self.scores = scores

    def averge(self):
        return sum(self.scores) /len (self.scores)

    def add_score(self , score):
        if 0 <= score <= 100:
            self.scores.append(score)

student = Student("Sara" , [80 , 90])
student.add_score(100)
print(student.name , student.averge())


# Practice

class Student:
    def __init__(self , name ):
        self.name = name
        self.scores = [] 

    def add_score(self , score):
        if 0 <= score <= 100:
            self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) /len (self.scores)


class Course:
    def __init__(self):
        self.students = []

    def add_student(self , student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print("Name:", student.name)
            print("Scores:", student.scores)
            print("Average:", student.average())

s1 = Student("Sarah")
s1.add_score(90)
s1.add_score(89)

s2 = Student("Omar")
s2.add_score(88)
s2.add_score(90)

s3 = Student("Jojo")
s3.add_score(100)
course = Course()
course.add_student(s1)
course.add_student(s2)

course.display_students()


