# # Lap 1
# class Ticket:
#     def __init__(self , name , status = "Open"):
#         self.name = name
#         self.status = status

#     def newstatus(self , status):
#         self.status = status

# # myTicket = Ticket("Unable to open email" , "Closed")
# myTicket1 = Ticket("1000" , "In-Progress")
# myTicket2 = Ticket("1001" , "Pending")

# print(myTicket1.status)
# print(f"Ticket ID : {myTicket1.name} is {myTicket2.status}")
# # --------------------------------------------------
# # Lap 2

# class Greeter:
#     def __init__(self , message):
#         self.message = message

#     def greet(self , user):
#         self.user = user

#         return(f"Hello {user} , {self.message}")


# mygreet = Greeter("Welcome to Tuwaiq")
# mymsg = mygreet.greet("Sarah")

# print(mymsg)

# # --------------------------------------------------
# # Lap 3
# class Welcome:
#     def __init__(self,name):
#         self.name = name

#     def welcome(self):
#         print(f"welcome {self.name}")

# students = [
#     Welcome("Sarah"),
#     Welcome("Khdijah"),
#     Welcome("Dala"),
#     Welcome("Omar")
# ]
# # students[1].welcome()
# for s in students:
#     s.welcome()

# --------------------------------------------------
# Lap 4
from pathlib import Path

path = Path("home") / "students" / "students.txt"
# path.mkdir(parents=True , exist_ok=True)
path.parent.mkdir(parents=True, exist_ok=True)
print(path.is_dir())# يطلع لي هل هو مجلد او لا
print(path.suffix) # يطلع لي امتداده وش
print(path.is_file())
path.write_text("Welcome to class", encoding="utf-8")

# with open(path, "w" , encoding="uft-8") as file:





# --------------------------------------------------






# --------------------------------------------------


    
