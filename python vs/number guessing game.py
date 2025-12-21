import random

lowest_num=1
largest_num=100
answer=random.randint(lowest_num,largest_num)
guesses=0
is_running=True

print("Number guessing game")
print(f"Enter a number between {lowest_num} and {largest_num}")

while is_running:
    guess=input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess < lowest_num or guess > largest_num:
            print("Out of range")
            (f"Please select a number between {lowest_num} and {largest_num}")
        elif guess > answer:
            print("guess is too high! try again")
        elif guess < answer:
            print("guess is too low! try again")
        else:
            print(f"Correct! The answer was {answer} ")
            print(f"Number of guesses: {guesses} ")
            is_running=False
    
    
    else:
        print(f"invalid guess")
        print(f"Please select a number between {lowest_num} and {largest_num}")
    
    
    
   
