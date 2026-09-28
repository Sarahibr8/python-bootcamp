#  login/password:
password = "New1029".lower()
for attempts in range(3):
   p_password = input("Please Enter Your Password :").strip()
   if p_password == password:
      print("Login successful✅")
      break
   else:
      print(f"Wrong password. Attempt {attempts + 1} of 3")
else:
   print("Program Closed")

# Welcome countdown
for second in range(3 , 0 ,-1):
   print(f"Starting in {second}")

print("Welcome the store!")

#products and prices 
products = ["Coffee", "Tea", "Esspreso"]
prices = [8, 10, 20]

for i in range(len(products)):
    print(f"{i + 1}. {products[i]} - {prices[i]} SAR")

# Count even and odd prices

even_counter = 0
odd_counter = 0

for price in prices:
   if price % 2 == 0 :
      even_counter += 1
else:
   odd_counter += 1

print(f"Even price count : {even_counter}")
print(f"Odd price count : {odd_counter}")

# Check age before purchase
total = 0

for price in prices:
   total += 1

print(f"Your total is:: {total} SAR")
print(f"VAT: {total * 15 / 100:.2f} SAR")
print(f"Total with VAT: {total * 1.15:.2f} SAR")

# Check age before purchase

age_text = input("Please enter your age: ").strip()
 
while not age_text.isdigit():
    print("Please enter a valid number")
    age_text = input("Please enter your age: ").strip()
 
age = int(age_text)
 
if age >= 18:
    print("You are allowed to buy all products ✅")
else:
    print("Some products are restricted for your age ❌")

# End the program.

count = 0
while count < 3:
    count += 1
    print(f"Closing program... {count}")
 
print("Program Completed")