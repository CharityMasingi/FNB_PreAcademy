#Tracking individual letters
name = "Python"

print(name[0])#We start counting from 0 from left to the right
print(name[-1])#We start counting from negative 1 from the right going to the left
print(name[2])

#Using string methods

town = "  Johannesburg  "

print(town.upper()) #changes words into upper cases
print(town.strip())#removes the spaces in from or behind a word

#combining string methods
#email generator
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

#creating a username for the user
username = f"{first_name[0]}{last_name}"
print(f"Your email is: {username.lower()}@university.co.za")#.lower to ensure it is in small caps
