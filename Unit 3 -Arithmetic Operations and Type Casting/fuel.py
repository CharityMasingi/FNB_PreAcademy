#A calculator to calculate traveling cost

kilometers = float(input("Enter the distance of your trip in km:"))
price_per_liter = float(input("Enter the price of fuel per liter: R" ))

#Calculating the liters of fuel needed
liters_needed =  kilometers / 10

total_cost = round(liters_needed * price_per_liter, 2)
print (f" Your trip will cost you: R{total_cost}")
