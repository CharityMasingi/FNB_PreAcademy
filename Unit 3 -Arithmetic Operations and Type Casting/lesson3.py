#Adding two numbers
num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: "))

print(num1+num2) #this just combines the strings it is not a calculation. it is string contatenation if the data type is not shown

#or
num1 = (input("Enter the first number: ")) 
num2 = (input("Enter the second number: "))

print(int(num1+num2))
#Core data types
#str: String/text
#int:Interger
#float:decimal
#bool: True or false

#Type casting - changing the data type


#CALCULATING THE TIP
bill = float(input("Enter the bill: R"))
tip = 0.15

val_tip = bill*tip
total_cost = bill + val_tip

print(f"Here is the tip: R{val_tip}")
print(f"Here is the tip: R{round(val_tip,2)} rounded")

print(f"Here is the total cost: R{total_cost}")
print(f"Here is the tip: R{round(total_cost,2)} rounded")
