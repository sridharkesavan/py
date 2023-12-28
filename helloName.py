# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

"""
This is a multiline comment
So you can go about doing it
"""

"""
# Capitalize the user input
name = name.capitalize()

# Capitalizes the first letter of every word input
name = name.title()
"""

# can be chained like below
name = name.strip().title()

# Split the name using the space character and assign it to a variable
first, last = name.split(" ")

# Say hello to user
print("hello,", first)




