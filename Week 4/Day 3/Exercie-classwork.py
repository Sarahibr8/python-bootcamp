# continut day2 -

# import csv

# with open("students.csv" , "w" ,
#           encoding="utf-8" , newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name" , "course"])
#     writer.writerow(["Sarah" , "Python"])
#     writer.writerow(["Ali" , "Django"])

# ------------------

# import json

# students = [
#     {"name": "Sara" , "score" : 92},
#     {"name": "Ali" , "score" : 85}
# ]

# with open("students.json" , "w" , encoding="utf-8") as file:
#     json.dump(students , file , indent=2)

# with open("students.json" , "r" , encoding="utf-8") as file:
#     loaded = json.load(file)

# print(loaded[0]["name"])

# ------------------
# try:
#     score = int(input("Score: "))
# except ValueError:
#     print("Enter a whole number")
#     print(ValueError)
# print("Program continues")

# ------------------

# from pathlib import Path

# try:
#     text = Path("students.txt").read_text(
#         encoding="utf-8"
#     )
# except FileNotFoundError:
#     print("Student file not found")
# except PermissionError:
#     print("Student file cannot be read")

# # -----------------------

# path = Path("students.txt")

# try:
#     text = path.read_text(encoding="utf-8")
# except OSError as error:
#     print("Load failed:" , error)
# else:
#     print(text)
# finally:
#     print("Load attempt finished")

# # -----------------------
# def validate_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError("Score must be 0 to 100")
#     return score

# try:
#     score = validate_score(120)
# except ValueError as error:
#     print(error)

# # -----------------------
# class StudentNOtFoundError(Exception):
#     pass

# def find_student(name , students):
#     for student in students:
#         if student["name"] == name:
#             return student
#     raise StudentNOtFoundError(name)

# students = [{"name" : "Sarah"}]

# try:
#     print(find_student("Ali" , students))
# except StudentNOtFoundError as error:
#     print("Missing student:" , error)
# -----------------------
# Practice
from pathlib import Path
import json

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  

data_file = data_dir / "studends.json"

print(data_dir.is_dir())  
print(data_file.exists())  

students = [
    {"name" : "Sarah" , "score" : 99} , 
    {"name" : "Jojo" , "score": 100} ,
    {"name" : "Bobo" , "score" : 98}
]


with data_file.open( "w" , encoding="utf-8") as file:
    json.dump(students, file , indent = 4)

try:
   with data_file.open( "r" , encoding="utf-8") as file:
    loaded_students = json.load(file)
   print(loaded_students)
except FileNotFoundError:
   print("Students file not found")
except json.JSONDecodeError:
   print("Invalid JSON format")


class InvalidStudentError(Exception):
    pass

def find_student(name , students ):
    for student in students:
        if student["name"] == name:
         return student
    raise InvalidStudentError(name)