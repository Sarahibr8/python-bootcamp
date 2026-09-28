# Lap 1
numbers = [1 , 2 , 3 , 4 , 5]
sqaured_numbers = []

for number in numbers:
    sqaured_numbers.append(number ** 2)

print(sqaured_numbers)

comp_numbers = [ number ** 2 for number in numbers ]

print(sqaured_numbers)

# -------------------------------------------
# Lap 2

prices = [10 , 25 , 40]
prices_with_vat = [
    round(price * 1.15 , 2)
    for price in prices
]

print(prices_with_vat)

# -------------------------------------------
# Lap 3

names = ["SaRa" , "ArEej" , "Mashael" , "nasser"]

lower = [ name.lower() for name in names ]

upper = [ name.upper() for name in names ]

titled = [ name.title() for name in names ]

print(lower , upper , titled)


# -------------------------------------------
# Lap 4

c_temp = [20 , 33 , 15 , 1]

f_temp = [
    (temp * 1.8 + 32)
    for temp in c_temp
    if temp > 0
]

print(f_temp)
# -------------------------------------------
# Lap 5

nested_list = [[1 , 2] , [3 ,4] , [5 , 6]]
flattened_list = []

for row in nested_list:
    for column in row:
        flattened_list.append(column)

print(flattened_list)

comp_flatted_list = [ column 
    for row in nested_list
    for column in row
]

print(comp_flatted_list)


# -------------------------------------------
# Lap 6

scores = [45 , 55 , 65 , 75 , 86 , 95]
passing_score = [
    "Pass" if score >= 60 else "Filed"
    for score in scores
]

print(passing_score)

# -------------------------------------------
# Lap 7

skills = [ "PYTHON" , "Git" , "Python" , "Javascript" , "SQL" , "git"]
skills_set = {
    skill.title().lower()
    for skill in skills
}

print(skills_set)

# -------------------------------------------
# Lap 8

list_name = ["Sara" , "Dalal" , "Nouf" , "Taif"]

counted_chars = [
    {"name":name , "count":len(name)} for name in list_name
]

print(counted_chars)
