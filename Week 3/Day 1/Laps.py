# Lap 1
def greet():
    print(f"Welcome to Python")
greet()

# ----
# Lap 2

def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Espreso")

show_menu()
print("Outside the call")
show_menu()

# ----
# Lap 3
def unknowScope():
    print("Line One")
    def gotoFunc():
        print("From within the GoTo")

    print("where is line 2?")
    gotoFunc()
    print("I'm up here")

# ----
# Lap 4

def greet_sudent(name):
    print(f"Welcome {name}")

greet_sudent("Sarah")
greet_sudent("Jojo")


# ----
# Lap 5
def show_booking(destination = "Riyadh", nights = 1):
    # if nights.isdigit():
    #         nn = int(nights)
    # print(f"You're traveling to {destination} , and will stay for {nights} nights")
    print(f"You're traveling to {destination} , and will stay for {nights} nights")

# show_booking()
show_booking("Jeedah" , 3 )
show_booking("Doha", 5 )

# ----
# Lap 6

def geetVAT(total , rate = 0.15):
    """ This function will get the total with VAT added to it, and return the sum  """
    subtotal = total + (total * rate)
    return subtotal

print(geetVAT(154))
print(geetVAT(154 , 0.05))
print(geetVAT.__doc__)
help(geetVAT)



# ----
# Lap 7

