message =  "Global"

def show_message():
    message = "Local"
    print(message)


show_message() #Local
print(message) #Global

# ------
# Python searches in this order:
# L - Local
# E - Enclosing
# G - Global
# B - Builit-in
print(len("Python"))

# ------
def calculate_total(price , quanity):
    total = price * quanity
    return total

result = calculate_total(20 , 3)
print(result)

# ------
def outer():
    course = "Python"

    def inner():
        print(course)

    inner()
outer()
# ------

tax_rate = 0.15

def calculate_tax(amout):
    return amout * tax_rate

print(calculate_tax(200))
# ------
scores = [80 , 90 , 100]

print(len(scores))
print(sum(scores))
print(type(scores))
# ------

list = [ 1 , 2 , 3]

# list("abc") now fails because
# list refers to the varible above.

sutent_list = [1 , 2 , 3]
# ------

#math is a standard-library module
import math

radius = 4
area = math.pi * radius ** 2
print(area)
# ------

from math import sqrt, pi

print(sqrt(49))
print(pi)

# Avoid : from math import *
# ------

import datetime as dt
from math import factorial as fact

today = dt.date.today()
print(today)
print(fact(5))
# ------

import random
import statistics 

scores = [82 , 91 , 75 , 88]

print(random.choice(scores))
print(statistics.mean(scores))
# ------

# calculater.py
def add(a ,b):
    return a + b

# main.py
import calculater

result = calculater

# ------

def greet(name):
    return f"Hello , {name}"

if __name__ == "__main__":
    print(greet("Sarah"))

# ------

# class work.
n = input("Enter your name:")
for letter in n:
    print(letter)
