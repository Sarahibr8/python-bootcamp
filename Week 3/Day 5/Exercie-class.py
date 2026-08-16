# numbers = range(1_000_000)

# total =sum(
#     number ** 2
#     for number in numbers
# )

# print(total)

# ----------------------------

# items = ["Python" , "Git"]
# items.append("Django")

# name = "sara"
# name = name.title()

# print(items)
# print(name)

# print(id(name))
# print(id(items))

# ----------------------------

# original = ["Python" , "Git"]
# alias = original

# alias.append("Django")

# print(original)
# print(alias)
# print(original is alias) #True
# print(id(original))
# print(id(alias))


# ----------------------------

# original = ["Python" , "Git"]
# clone = original.copy()

# clone.append("Django")

# print(original)
# print(clone)
# print(original is clone) #Fales
# print(id(original))
# print(id(clone))

# ----------------------------
# shallow copy > هنا يغير الاثنين الاساس وبعد الكوبي
# original = [["Sara" , 90] , ["Omar" , 85]]
# clone = original.copy()

# clone[0][1] = 95
# print(original)
# print(clone)
# print(original [0] is clone [0]) #True

# ----------------------------
# deep copy > هنا مايتغير الاساس بس الي بعد النسخ و يعتبر مكلف جدا 
# from copy import deepcopy

# original = [["Sara" , 90] , ["Omar" , 85]]
# clone = deepcopy(original)

# clone[0][1] = 95
# print(original)
# print(clone)
# print(original [0] is clone [0]) #False

# ----------------------------
# names = ["Sara" , "Omar" , "Lina"]
# # Searches items one by one: O(n)
# print("Lina" in names)

# name_set = set(names)
# # Average membership lookup: O(1)
# print("Lina" in name_set)

# ----------------------------

# students = [
#     {"id" : 101 , "name" : "Sara"},
#     {"id" : 102 , "name" : "Omar"},
# ]

# students_by_id = {
#     student["id"]: student
#     for student in students
# }

# print(students_by_id[102]["name"])
# ----------------------------
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