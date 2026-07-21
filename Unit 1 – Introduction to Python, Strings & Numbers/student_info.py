#Using input to ask for user input
first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
age = int (input("Please enter your age: "))
fav_number = float (input("Please enter your favourite number: "))

#Displaying name with a greeting and making the name in uppercase and the surname in Title 
print (f"Welcome ,{first_name.upper()} {surname.title()}, !")

new_age = age * 12
print(f"Your age in months is: {new_age}")

new_fav = round(fav_number, 2)

print(type(first_name))
print(type(surname))
print(type(age))
print(type(fav_number))
