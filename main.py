import random
option = ["rock","paper","scissors"]
print("Let's play")
computerchoice = random.choice(option)
playerchoice = input("choose rock / paper / scissors:")
#tie
if playerchoice == computerchoice:
    print("it's a tie!!")
#player won
elif (playerchoice == "rock" and computerchoice == "scissors"):
    print("you win!")
elif (playerchoice == "paper" and computerchoice == "rock"):
    print("you win!")   
elif (playerchoice == "scissors" and computerchoice == "paper"):
    print("you win!")   
#computer won
else:
    print("computer won!")