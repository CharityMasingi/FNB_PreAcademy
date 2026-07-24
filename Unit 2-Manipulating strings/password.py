#A password hinting script
password = input("Please enter your password: ")

#removing spaces
password_stripped = password.strip()

#To take the first and last letters of the password
first_letter = password_stripped[0]
last_letter = password_stripped[-1]

#printing the hint
print (f"Your password starts with {first_letter.upper()} and ends with {last_letter.upper()}.")
