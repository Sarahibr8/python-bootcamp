first = [1 ,2]
second = [1 ,2]
alias = first


first == second  # True : the same value
first is second  # False: different object
first is alias   # True : same object

# ------
csv_line = "Ali,Sarah😍,Omar"
names = csv_line.split(",")

message = " | ".join(names)

print(names) 


# ------
sentence = input("Enter sentence ")
num1 = int(input("Enter numbers "))
num2 = int(input("Enter numbers "))

print(num1 + num2, num1 - num2, num1 / num2, num1 % num2)


nambers = [2,3]
secound_num = [2 ,3]
alias = nambers

nambers == secound_num
nambers is secound_num 
nambers is alias

print(nambers == secound_num)
print(nambers is secound_num )
print(nambers is alias)


corses = "Python Bootcamp"
print(corses.lower())
print(corses.upper())
print(corses.strip())

f_line = "Sarah,Lama,Bdoor"
names = f_line.split(",")

message = " | ".join(names)
print(names) 
