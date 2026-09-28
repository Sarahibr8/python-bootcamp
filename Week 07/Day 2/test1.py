student_name = input("Student name:")
score = int(input("Score:"))

if score >=90:
    grade = "A"
    
elif score >=80:
    grade = "B"

elif score >=70:
    grade = "C"

else:
    grade = "Needs improvment"


print("Student:" , student_name)

print("Score:" , score)

print("Grade:" , grade)


