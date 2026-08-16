# Lap 1

new_name = ["Mada" , "Sara" , "Yamam" , "Jojo"]

upp = (
    name.upper()
    for name in new_name
)
print(next(upp))
print(next(upp))
print(list(upp))
print("-" *5)
for x in upp:
    print(x)
