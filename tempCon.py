
unit = input("Enter choice: Celcius or Farennhite (C/F): ").upper()
temp = float(input("Enter temp: "))

if unit == "C" :
    temp=round((9*temp)/5+32 ,2)
    unit= "F"
    print(f"Converted temperature is {temp} {unit}")
elif unit == "F" :
    temp=round((temp -32) * 5/9 ,2)
    unit="C"
    print(f"Converted temperature is {temp} {unit}")
else :
    print(f"{unit} is invalid")