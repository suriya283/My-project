def check_balance(balance):
    print(f"Your current balance is {balance:2f}")

def amt_deposit(balance):
    print(f"Your current balance is {balance:2f}")
    amt=int(input("Enter an amount to deposit: "))
    if amt<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amt
    
def amt_withdraw(balance):
    print(f"Your current balance is {balance:2f}")
    amt=int(input("Enter an amount to withdraw: "))
    if amt>balance:
        print("Insufficient balance!")
        return 0
    if amt<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amt


def main():
    balance=0
    is_running = True
    while is_running:
        print("*********************")
        print("*********ATM*********")
        print("*******Options*******")
        print("\t1.Balance")
        print("\t2.Deposit")
        print("\t3.Withdraw")
        print("\t4.Exit")
        print("*********************")
        option=input("Enter the option(1 to 4): ")
        if option == "1":
            check_balance(balance)
        elif option == "2":
            balance+=amt_deposit(balance)
        elif option == "3":
            balance-=amt_withdraw(balance)
        elif option == "4":
            print("********************")
            print("You are exited")
            print("Thank you! Have a nice day")
            print("********************")
            is_running=False
        else:
            print(f"{option} invalid! Try valid option")


if __name__ == "__main__":
    main()
