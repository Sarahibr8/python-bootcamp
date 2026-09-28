#Lap 1

age = 20
if age >=18:
    print("Welcome")
print("Code Completed")

#----------

#Lap2

temprator = 31
if temprator >= 35:
    print("Its not outside")
else:
    print("cool")


#----------
#Lap3

score = 2000
if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("You need to improve ")

#----------


#Lap4

is_active = True
is_verified = True
role = "editor"
is_blcoked = False

if is_active and is_verified:
    print("Account is ready")

if role == "admin" or role == "editor":
    print("User can edit")

if not is_blcoked:
    print("User is not bloked")

else:
    print("User is blocked")

#----------
#Lap5 

account_active = True
has_permission = False

if account_active:
    if has_permission:
        print("Acces Granted")
    else:
        print("Acces denied")
else:
    print("Account is not active")

#----------
# Lap6

name = "Sarah"
cart = []
balance = 0

if name:
    print("Name has a value")

if not cart :
    print("Your cart is empty , plasse shop")
print(bool(balance))

#----------
#Lap7

name = input("Plasse enter your first name").strip()#ياخذ اول واخر المسافه 

if not name:
    print("Plasse enter a name")
elif not name.replace(" " , "").isalpha():
    print("Name must contain letters")

else:
    print(f"Valid name {name}")
print(name.replace(" " , ""))

#----------
# Lap8

age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5 } in 5 years")

else:
    print("Enter a number")

#----------
# Lap9

is_score_valid = False
score_text = input("Enter a number between 0 and 100: ")

if score_text.isdigit():
    score_x = int(score_text)

    if score_x >= 0 and score_x <= 100:
        print("Valid score")
        is_score_valid = True
    else:
        print("Score is invalid")
else:
    print("Plasse enter a number")


#----------
# Lap10

membership = ["Admin" , "Editor" , "Viewer"]

current_membership = input("Enter your membership: ").strip().lower()

if current_membership.title() in membership:
    print("You are allowed to view the content")
    print(current_membership)
else:
    print("Please contact admin team")
    print(current_membership)

#----------
# Lap11

command = input("Please enter a command (start , stop , status)").strip().lower()

match command:
    case "start":
        print("......Starting system")
    case "stop":
            print("Stooping system......")   
    case "status":
            print("System is up and running 👌") 
    case _:
            print("Please enter a proper command")
    
