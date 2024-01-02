
#name = input("What's your name? ")

"""
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

"""

"""
# Write to file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

"""

"""
#Read a file
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print("hello,", line)

"""

# Read a file elegantly
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip() )