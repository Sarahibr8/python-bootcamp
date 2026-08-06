#اعكس القيم 
x = 0 
y = 1
x , y = y , x
#1  0   1   0 # اول شي نقرا اليمين ونحطه باليسار
print(x)
print(y)

#-------- 
# another example:

a = 10
b = 20

a , b = b , a 

print(a)
print(b)

# Exercise Day2-w2\
# print the student card 
# Greet the student
# show thier program name 
# show thier age
#  thank you massage
# using f string  

student_name = "Sarah"
program_name = "Database Programming"
age = 24
registration_status = "registered"

print("\n--- Student Card ----")
print(f"Hello , {student_name}!")
print(f"Program is :{program_name}")
print(f"Age : {age}")
print(f"Registration status: : {registration_status}")
print(f"Thank you {student_name} \n- Have a greet day! ")

#With input :
student_name = input("Enter your name : ")
program_name = input("Enter your program name : ")
age = int(input("Enter your age : "))
registration_status = input("Enter your registration status :")

print("\n--- Student Card ---")
print(f"Hello , {student_name}!")
print(f"Program is :{program_name}")
print(f"Age : {age}")
print(f"Registration status: : {registration_status}")
print(f"Thank you {student_name} \n- Have a greet day! ")
