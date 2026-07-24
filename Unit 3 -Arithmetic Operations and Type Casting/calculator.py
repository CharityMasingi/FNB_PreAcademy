#Asking user to enter a number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 == 0:
  print ("Error")

addition = num1+num2
subtraction = num1-num2
multiplication = num1*num2
division = num1/num2
#Diplaying addition, subtraction, multiplication and division
print (f"Addition:{addition}, subtraction:{subtraction}, multiplication:{multiplication}, division:{division}.")

#Diplaying floor division and modulus
floor_div = num1//num2
mod = num1%num2

#Rounded results
rounded_add = round(addition,2)
rounded_sub = round(subtraction,2)
rounded_mult = round(multiplication,2)
rounded_div = round(division,2)
rounded_floor = round(floor_div,2)
rounded_mod = round(mod,2)

print (f"Before rounding: {addition} | {subtraction} | {multiplication} | {division} | {floor_div} | {mod} ")
print (f"After rounding: {rounded_add} | {rounded_sub} | {rounded_mult} | {rounded_div} | {rounded_floor} | {rounded_mod} ")
