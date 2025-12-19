principle=0
rate=0
time=0
while True:
    principle=float(int(input("Enter the principle amount: ")))
    if principle<0:
        print("Principle amount can't be lesser than 0.")
    else:
        break
while True:
    rate=float(int(input("Enter the rate amount: ")))
    if rate<0:
        print("rate amount can't be lesser than 0.")
    else:
        break
while True:
    time=float(int(input("Enter the time in year: ")))
    if time<0:
        print("time amount can't be lesser than 0.")
    else:
        break


total=principle * pow(1+rate/100,time)
print(f"Balance after {time} years: {total:.2f}")

