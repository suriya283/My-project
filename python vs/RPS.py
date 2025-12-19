import random
options=("rock","paper","scissors")
player=None
computer=random.choice(options)
played=0
win=0
loss=0
tie=0
while True:
    player=input("Enter a choice (rock Paper Scissors): ")
    if player not in options:
        print("Enter an valid option")
        player=input("Enter a choice (rock Paper Scissors): ")
    played+=1
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("Its tie!")
        tie+=1
    elif player == "rock" and computer == "scissors":
        print("You won!")
        win+=1
    elif player == "paper" and computer == "rock":
        print("You won!")
        win+=1
    elif player == "scissors" and computer == "paper":
        print("You won!")
        win+=1
    else:
        print ("You lose!")
        loss+=1
    play=input("You want to play again (y/n): ").lower()
    if play != "yes":
        print(f"You played {played} times and Your win is {win} times and Your loss is {loss} times and Your tie is {tie} times")
        break
            