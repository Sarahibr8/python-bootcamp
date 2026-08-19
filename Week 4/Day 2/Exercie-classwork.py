from pathlib import Path

data_file = Path("data") / "students.txt"

print(data_file)
print(data_file.name)
print(data_file.suffix)

# ------------------------------
# Inspect paths before using them
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
data_file = data_dir / "students.txt"
print(data_dir.is_dir()) # Data Directory
print(data_dir.exists())
print("-" * 30)

# ------------------------------
# File ----
# "r" read an existing file
# "w" write and replace content
# "a" append after existing contant
# "x" create only when absent

with open("notes.txt" , "a" , encoding="utf-8") as file:
    file.write("New note\n")

# "cn-us" يدعم بس الانجليزي
# "SA-Ar" يدعم غير الانجليزي

print("-" * 30)

# ------------------------------
path = Path("notes.txt")
with path.open("r" , encoding="utf-8") as file:
    content = file.read()
print(content)
print(file.closed) #True
print("-" * 30)

# ------------------------------
path = Path("notes.txt")
with path.open("r" , encoding="utf-8") as file:
    text = file.read()
same_text = path.read_text(encoding="utf-8")
print(text == same_text)
print("-" * 30)

# ------------------------------
path = Path("students.txt")

with path.open("w", encoding="utf-8") as file:
    file.write("Sara\n")
    file.write("Ali\n")
    file.write("Ahmed\n")
# ------------------------------
path = Path("students.txt")
with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line. strip()
        if name: # Truthy يعني ما يهمني قيمتها
            print (name)
#    write ينفع يس csv الى write لو غيرت
print("-" * 30)

# ------------------------------
path = Path("students. txt")
with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")

print(count)
print("-" * 30)
# ------------------------------

path = Path("activty.log")
with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")

print("Activity saved")
print("-" * 30)
# ------------------------------
names = ["Sara" , "نوره" , "Ali"]
text = "\n".join(names) + "\n"
Path("students. txt").write_text(
    text,
    encoding="utf-8"
)
print(Path)
print("-" * 30)
# ------------------------------



# ------------------------------



# ------------------------------


# ------------------------------
