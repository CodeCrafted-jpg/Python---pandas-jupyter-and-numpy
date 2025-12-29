
weight = float(input("Enter weight: "))
unit = input("Enter choice: K (for kilogram) L (for pounds): ")
if unit=="K" :
 weight=weight*2.205
 unit="lbs"
elif unit=="L" :
 unit="kg"
 weight=weight/2.205 
else :
 print(f"{unit} is not valid")

print(f"your weight is {round(weight,2)} {unit}")