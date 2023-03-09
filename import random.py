import random

player1 = input("Enter a choice for player1 (rock,paper,scissors):")
possible_choice = ["rock","paper","scissors"]

player2 = input("Enter a choice for player 2 (rock,paper,scissors):") 
print("player1 chose {player1}, and player2 chose{player2}\n")

if player1 == player2:
    print("Both players selected {player1}. It's a tie!")

elif player1 == "rock":
    if player2 == "paper":
        print("Paper covers rock. You lose!") 
    else:
        print("Rock smashed scissors. You win!")

elif player1 == "paper":
    if player2 == "scissors":
        print("Scissors cuts paper. You lose!") 
    else:
        print("Paper covers rock. You win!")

elif player1 == "scissors": 
    if player2 == "rock":
        print("Scissors are smashed by rock. You lose!") 
    else:
        print("Scissors cut paper. You win!")
           

