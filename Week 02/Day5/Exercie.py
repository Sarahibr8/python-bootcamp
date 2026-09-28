for number in range(5):
    print(number)


# ----

for n in range(1,6):
    print(n)

for n in range(5, 0 , -1):
    print(n)


# ----

word = "Python"

for character in word:
    print(character)

# ----
Students = ["Ahmed" , "Sara" , "Faisal"]

for student in Students:
    print(f"Welcome, {student}")

# ----

max_num = int(input("Enter the maximum number :"))

even_count = 0
even_total = 0

for num in range(1 ,max_num):
    if num % 2 == 0:
        print(f"{num} is Even")
        even_count +=1
        even_total += num
    else:
        print(f"{num} is Odd")

print(f"Even numbers count: {even_count}")
print(f"Total numbers numbers: {even_total}")