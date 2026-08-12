# Comprehension > دائما القيمه ناخذها من ال for  - يعني المتغير ثم نعرفه في الفور
numbers = [1 , 2 , 3 , 4 , 5] #Expression الي يعطيني قيمه

squares = [
    number ** 2
    for number in numbers
    if number % 2 == 1   #close
]

print(squares)
# # ----

prices = [10 , 25 , 40 ]

prices_with_vat = [
    round(price * 1.15 , 2)
    for price in prices

]

print(prices_with_vat)

# --------

scores = [42 , 67 , 91 , 58 , 75]

passing_scores = [
    # score for score in scores if score >= 60
    score 
    for score in scores 
    if score >= 60


]

print(passing_scores)

# -------

raw_names = [" sara " , "" , "OMAR" , "lina"]

clean_names = [
    name.strip().title() # الستريب للمسافات و التايتل اول حرف كابيتل
    for name in raw_names
    if name.strip()
    # if name.title()
    # for name in raw_names
]

print(clean_names)
# -------

numbers = [1 , 2 , 3 , "S"]
letters = ["A" , "B" , "C"]

pairs = [
    (number , letter)
    for number in numbers
    for letter in letters

]
print(pairs)

# ------

scores = [42 , 67 , 91]

labels = [
    "pass" if score >= 60 else "retry"
    for score in scores
]
print(labels)

# ------

emils = [
    "SARA@EXAMLE.COM",
    "omar@example.com",
    "lina@school.sa"
]
domains = {
    email.split("@")[1].lower()
    for email in emils
}
print(domains)

# --------

numbers = range(1 , 6) 

squares = {
    number: number ** 2
    for number in numbers
}
print(squares)