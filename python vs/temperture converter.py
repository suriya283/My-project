unit=input("Is a temperture is Celsius or Fahrenhiet (C/F): ")
temperture=float(input("Enter the Temperture: "))

if unit=="C" or unit=="c":
    temperture= (temperture*9/5)+32
    print(f"The temperture in fahrenheit is {round(temperture,1)}F.")
elif unit=="F" or unit=="f":
    temperture= (temperture*5/9)-32
    print(f"The temperture in celsius is {round(temperture,1)} C.")
else:
    print(f"{unit} is invalid unit of temperture")
