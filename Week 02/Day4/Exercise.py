age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)

#------------

name = input("Enter your name : ")
if name == "":
    print("Name cannot be empty!")
else:
    score = int(input("Enter your score: "))
    if score < 0 or score > 100:
        print("Score moust be btween 0 and 100 ")
    else:
        corses = input("Enter your course: ").strip().lower()


    if score >=90:
        grade = "A"
    elif score >=80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F"

# if corses in ["Python" , "Dart" , "flutter"]:

        match corses:
            case "python":
                print("Course confirmed.")
            case "dart":
                print("Course confirmed.")
            case "flutter":
                print("Course confirmed.")
            case _:
                print("Invalid course.")