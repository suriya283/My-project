
import random

def row():
    choices=['😍','❤️','🍒','🍉','⭐','🔔','😎']
    
    #result=[]
    #for i in range(3):
    #    result.append(random.choice(choices))
    #return result
    return [random.choice(choices) for _ in range(3)]
def print_row(rows):
    print("----------------------")
    print(" | ".join(rows))
    print("______________________")
def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "❤️":
            return bet*2
        elif row[0] == "🍒":
            return bet*4
        elif row[0] == "🍉":
            return bet*8
        elif row[0] == "⭐":
            return bet*16
        elif row[0] == "😍":
            return bet*20
        elif row[0] == "🔔":
            return bet*25
        elif row[0] == "😎":
            return bet*30
    else:
        return 0 
    

def main():
    balance=100
    print("***********************")
    print("Welcome to Pyhton Slots")
    print("Symbols: ❤️🍒🍉⭐😍🔔😎")
    print("***********************")
    while True:
        print(f"Your balance is Rs.{balance}")
        bet=input("Enter the bet: ")
        if not bet.isdigit():
            print("Please enter the valid bet!")
            continue
        bet=int(bet)
        if bet >balance:
            print("Insufficient bet")
            continue
        if bet <=0:
            print("Bet must be greater than 0")
            continue
        balance-=bet            
        rows=row()
        print("spinning.......")
        print_row(rows)
        result=payout(rows,bet)    
        if result > 0:
            print(f"You won Rs.{result}")
        else:
            print("Sorry you loss! This round")
        balance+=result
        play_again=input("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            print("You are exited")
            break
    print("************************")
    print(f"Game over! Your balance Rs.{balance}")
    print("************************")
if __name__ == "__main__":
    main()