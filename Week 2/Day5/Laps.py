# Lap1

for attempts in range(3):
    print(f"Attemps: {attempts + 1}")
print("Program Completed")

# ---------
# Lap2

for num in range(2 , 11 , 2):
    print(num)


# ---------
# Lap3

for secondsToLanch in range(10 , 0 , -1):
    print(f"T-: {secondsToLanch}")



# ---------
# Lap4

course = "Python"

for letter in course:
    print(letter)


# ---------
# Lap5

students = ["Sarah" , "Lama" , "khadija" , "Dalal"]

for student in students:
    print(f"Progreesing student is: {student}")

# ---------
# Lap6

for number in range(1 , 11):
    if number % 2 ==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    print("__________")

# ---------
# Lap7

numbers = [4 , 7 , 10 , 13 , 16 , 21 , 22]
even_counter = 0

for num in numbers:
    if num % 2 ==0:
        even_counter += 1 

print(f"Total even numbers is: {even_counter}")

# ---------
# Lap8

prices = [25 , 30 , 55 , 115]
total = 0

for price in prices:
    total += price

print(f"Your total is: {total} VAT: {total * 1.15:.2f}")
print(f"Your total is: {total} VAT: {total * 15/100}")

# ---------
# Lap9

count = 0 
while count <5:
    count += 1
    print(f"Count....{count}")
print("Loop completed")


# ---------
# Lap10

message = "Please enter your age:"
age_text = input(message).strip()

while not age_text.isdigit():
    age_text = input(message).strip()
age = int(age_text)

print(f"You are: {age}")

# ---------
# Lap11
password = "python123"
print("Please Enter yor password: ")


while password != "":
    password = input("Enter yor password: ")

