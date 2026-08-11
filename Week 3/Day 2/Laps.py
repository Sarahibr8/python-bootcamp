# # Lap 1

# course = "Web Development Bootcamp"
# duration = 12

# def type(course):
#     print("Opss!")

# print(course)
# print(duration)
# print(type(course))
# # print(globals())
# # print(locals())
# # print(globals() ["course"])

# # -----
# # Lap 2

# builiding = "Tuwaiq Acadmy"
# cohort_size = 20

# print(f"Welcome to {builiding} , class limit is {cohort_size}")
# print("Tuwaiq " in builiding)
# print("cohort_size" in globals())
# # print(globals() ["builiding"])
# # shift + alt + down

# # -----
# # Lap 3
# # loction = "Global"

# # def outter():
# #     loction = "Outter"
# #     print(f"From {loction}")
# #     def inner():
# #         loction = "Inner"
# #         print(f"From {loction}")

# #     inner()
# # outter()

# # -----
# # Lap 4

# # loction = 0

# def outter():
#     loction = 1
#     print(f"From {loction}")
#     def inner():
#         nonlocal loction
#         loction += 2
#         print(f"From {loction}")

#     inner()
# outter()

# # -----
# # Lap 5

# def printer():
#     print("Welcome!")


# def desk():
#     printer()

# def room():
#     desk()

# def house():
#     room()

# def city():
#     house()

# def country():
#     city()

# country()

# -----
# Lap 6

language = "Python"

def show_lang(language):
    print(language)

show_lang("Dart")
print(language)

# -----
# Lap 7

rate = 0.15
def getTotal(amount):
    total = amount * rate  + amount
    return total

print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99) , 2))

# -----
# Lap 8

def inspect_order(item , qty):
    subtotal = 25 * qty
    print(locals())
    print(locals() ["subtotal"])

inspect_order("Pen" , 10)