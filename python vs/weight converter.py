#weight converter

weight=float(input("Enter a weight: "))
unit=input("Kilogram or Pounds? (K or L): ")

if unit=="K" or unit=="k":
    weight*=2.205
    unit="Lbs."
    print(f"Your Weight is: {round(weight,1)} {unit}.")
elif unit=="L" or unit=="l":
    weight/=2.205
    unit="Kgs"
    print(f"Your Weight is: {round(weight,1)} {unit}.")
else:
    print(f"{unit} is not valid")
