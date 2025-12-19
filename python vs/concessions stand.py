
menu={"pizza":100,
      "burger":80.50,
      "coke":60.75,
      "fries":80.25,
      "water":20,
      "samosa":20,}
cart=[]
total=0
print("---------menu---------")
for key,value in menu.items():
    print(f"{key:10}: Rs.{value:.2f}")
print("----------------------")

while True:
    food=input("Enter an item (q to quit): ").lower()
    if food == "q":
        break
    if food =="":
        print("Food cannot be empty. please try again")
    elif menu.get(food) is not None:
        cart.append(food)
print("---------YOUR ORDER---------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: Rs.{total:.2f}")
print("----------------------------")
