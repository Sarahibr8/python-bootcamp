# def greet():
#     print("Welcome")
# greet()

# # -----

# def greet(name):
#     print(f"hello , {name}")
          
# greet("sarah")
# greet("jojo")

# # -----
# def welcome(name):
#     print(f"Welcome , {name}")
          
# welcome("sarah")

# # -----

# def introduce(name , age):
#     print(f"{name} is {age} year old.")

# introduce (age= 25 , name= "Sarah")

# # -----
# def greet(name , greeting= "Hello"):
#     print(f"{greeting} , {name} !")

# greet("Sarah")
# greet("Sarah" , "Welcome")

# # -----
# def add(a , b):
#     return a + b 

# total = add( 5 , 3)
# print(total)
# # print(add( 5 , 3))

# # -----

# def rectangle_area(length , width):
#     return length * width

# area = rectangle_area(5 , 4)
# print(f"Area: {area}")

# # -----
# # def show_m




# # -----
# def calculate_tax(amount , rate):
#     """Return the tax amount for a give rate"""
#     return amount * rate

# tax = calculate_tax(200 , 0.15)
# print(calculate_tax.__doc__) #display the coomant inside the function.

# # -----

# def count_even(limit):
#     count = 0

#     for number in range(1 , limit+ 1):
#         if number % 2 == 0:
#             count += 1
#         return count
# print(count_even(10))

# -----
# class work 
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
score = float(input("Enter your score: "))

print(calculate_grade(score))
# print(calculate_grade(77))
# print(calculate_grade(40))
