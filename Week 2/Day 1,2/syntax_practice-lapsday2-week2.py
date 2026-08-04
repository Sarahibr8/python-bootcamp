# Lap 1 in week 2(الاثنين)
student_name = "Abdallah"
student_name = "Sara"


print(student_name)


score = 95

if score >=90:
    print("Excellent")
else:
    print("Thank you")




# Lap 2 in week 2(الاثنين)**
#Create , rename 

student_name = "Mada"
student_age = 20
course = "Web development bootcamp"
registered = True


MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15

print(f"""
Welcome {student_name} to {course}
You are {student_age} 
Registration status: {registered}

""")

student_name , student_age ,student_is_registered = "Sarah" , 24 , True

print(type(student_age))
print(type(student_name))
print(type(student_is_registered))

print(isinstance(student_name , str))
print(isinstance(student_age , int))


age = input("Enter your age") 

if (isinstance(age,int)):
    print("You are" , age+5 , "after 5 years")
else:
    print("You are " , int(age) + 5 , "After 5 years")



# Lap 3 in week 2(الاثنين)

teacer_name = "faisal"
print(teacer_name)

index = int(input("Select an index"))

if (index <= len(teacer_name)):
    print(teacer_name[index])

else:
    print("out of range")


#ابحث كيف اعكس القيم 
x = 0 
y = 1

x = 0 
y = 1
x , y=y , x

#print the st

