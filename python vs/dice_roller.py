import random 

#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={
    1:( 
"┌─────────┐",
"│         │",
"│    ●    │",
"│         │",
"└─────────┘"),2:( 
"┌─────────┐",
"│  ●      │",
"│         │",
"│      ●  │",
"└─────────┘"),3:( 
"┌─────────┐",
"│  ●      │",
"│    ●    │",
"│      ●  │",
"└─────────┘"),4:( 
"┌─────────┐",
"│  ●   ●  │",
"│         │",
"│  ●   ●  │",
"└─────────┘"),5:( 
"┌─────────┐",
"│  ●   ●  │",
"│    ●    │",
"│  ●   ●  │",
"└─────────┘"),6:( 
"┌─────────┐",
"│  ●   ●  │",
"│  ●   ●  │",
"│  ●   ●  │",
"└─────────┘"),
}

dice=[]
total=0
numofdice=int(input("How many dice: "))

for i in range(numofdice):
    dice.append(random.randint(1,6))

#for i in range (numofdice):
#   for line in dice_art.get(dice[i]):
#      print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line] , end="")
    print()
for i in dice:
    total+=i
print(f"Total: {total}")