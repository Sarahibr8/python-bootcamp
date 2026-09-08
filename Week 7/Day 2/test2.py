items = ["Coffee" , "Sandwich" ,"Juice"]

prices = [12 , 14 , 20]

total = 0

for price in prices:
    total += price

vat = total * 0.15
finall_total = total+vat



print("Items:")

for item in items:

    print("-" , total)

print("Total:" , total)
print("VAT")

print("Final:" , total)