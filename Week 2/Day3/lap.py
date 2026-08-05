#LAB 1
result = 10 + 5 * 2 - 4 /2
print(result)

#LAB 2
total_items = 17
box_capacity = 5
full_box = total_items // box_capacity
remaining_items = total_items % box_capacity
print(f"You can full up to: {full_box}")
print(f"And you will have {remaining_items} remaining")

#LAB 3
base_calc = 2 + 3 * 2 **2
gcalc =  (2 + 3) * 2 **2
print(base_calc)
print(gcalc)

#LAB 4
user_age = 25
has_permission = True
is_eligible = (user_age >= 18 and has_permission)
print(is_eligible)
is_eligible = (user_age >= 18 or has_permission)
print(is_eligible)
is_eligible = (True if (user_age >= 18 or has_permission) else False)
print(is_eligible)
is_eligible = (user_age >= 18 and has_permission)
print(f"Eligiblty status :{is_eligible}")

#LAB 5
score = 15
score += 5
#score = score +  5
score *= 5
#score = score * 5
print(f"Your score is {score}")

#LAB 6
membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership in membership:
    print("welcome")

if current_membership or "Admin" in membership:
    print("welcome")

if current_membership and "Viewwer" in membership:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = ["Editor"]
if current_membership[1] in membership:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership == membership[1]:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership[0] == "E":
    print("welcome")

#LAB 7
stetence = "Python Web Development"
nem_stetence = stetence.find("Python")
print(type(nem_stetence))
print(nem_stetence)


sentence = ["Python" , "web" , "development"]
if "Python" in sentence:
    print("Math found")
else:
    print(" no match found")    


#LAB 8
message = "Python Programming"
first_char = message[0]
last_char = message[-1]
print(f"First character is {first_char} and last character is {last_char}")
#Slicing 
sliced_message = message[:6]
print(sliced_message)
reversed_message = message[::-1]
print(reversed_message)
print(f"""Your message was {message}
if we take the first 6 characters is will be {sliced_message}
if we reverese it, it will be {reversed_message}
""")

#LAB 9
my_email = "       dalal@gmail.com"
cleanded_email = my_email.strip().lower()
message = "python web development"
titled_message = message.title()
print(f"your emails is {cleanded_email}, and your course is {titled_message}")

#LAB 10
csv_text = "apple,orange,banana,cherry,dates"
splitted_text = csv_text.split(",")
print(sliced_message)
joined_text = " - ".join(splitted_text)
print(f"""Your list is {csv_text}
Splitted like this {splitted_text}
rejoned like this {joined_text}
""")

#LAB 11
name = "Khalid"
try:
    name[0] = "A"
except TypeError as e:
    print(e)


x = 5
y = 5
if (x == y):
    print("They are the same value")
else:
    print("They are not the same value")

x = 5
y = 5
if (x is y):
    print("They are the same object")
else:
    print("They are not the same object")

print(id(x))
print(id(y))

x = [5]
y = [5]
if (x is y):
    print("They are the same value")
else:
    print("They are not the same value")

print(id(x))
print(id(y))

#LAB 12
message = "Python Web Development"
new_message = message.replace("Development", "Programing")
print(new_message)

is_online = None
print (is_online == None)
is_online = None
print (is_online != None)

is_online = None
if(is_online): # نفس is_online == True
    print("True")
elif(is_online != True and is_online != False):
     print("False")
else:
    print("None")
#print(is_online)