# Class-Practice : Week 3-Day5.
from copy import deepcopy

students = [
    {"name" : "Sara" , "scores" : [90 , 90 , 88]},
    {"name" : "Dalal" , "scores" : [70 , 98 , 50]},
    {"name" : "Lama" , "scores" : [55 , 44 , 50]},
]

report = [
    {
    "name": student["name"],
    "scores": student["scores"],
    "average": round(sum(student["scores"]) /len (student["scores"]),2)
    }
    for student in students
]

print(report)
passed_student = [
    student
    for student in report
    if student ["average"] >= 60
]

print(passed_student)
students_by_name = {
    student["name"]: student
    for student in passed_student
}

print(students_by_name)
backup = deepcopy(passed_student)

backup[1]["scores"][0] = 99


print("Orginal:" , passed_student)
print("Backup:" , backup)
print("Orginal ID:" , id(passed_student))
print("Backup ID:" , id(backup))