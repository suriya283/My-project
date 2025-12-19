
foods=[]
prices=[]
total=0

while True:
    food=(input("Enter an item to buy (q to quit): "))
    if food.lower()=="q":
        break
    if food == "":
        print("Food cannot be empty. Please try again")
        continue
    else:
        price=float(input(f"Enter an price of a {food}: "))
        prices.append(price)
        foods.append(food)
print("**********Your cart**********")
for food in foods:
    print(food, end=" ")
for price in prices:
    total+=price
print()
print(f"Your total amount is:{total} ")
