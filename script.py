#Rock Paper Scissors
#The Rules:
# two players
# three choices
# paper beats rock
# rock beats scissors
# scissors beats paper
# Tie = go again
# all other scenarios is a loss

import random

game_ends = False

while not game_ends:


    #wins tracker
    wins = 0
    ties = 0
    losses = 0

    #game choices
    choices = ["rock", "paper", "scissors"]

    #user choices
    user_choice = input("Make a selection: rock, paper, or scissors:")
    print(f'you chose {user_choice}')

    #computer choice
    comp_choice = random.choice(choices)
    print(f'the computer chose {comp_choice}')

    if user_choice == "quit":
        game_ends = True
        continue
        print(f'You won {wins}, You tied {ties}, You lost {losses}', "Sad to see you go")
    
    if user_choice == "paper" and comp_choice == "rock":
        print("You win!")
        wins+=1
    elif user_choice == "rock" and comp_choice == "scissors":
        print("You win!")
        wins+=1
    elif user_choice == "scissors" and comp_choice == "paper":
        print("You win!")
        wins+=1
    elif user_choice == comp_choice:
        print("Tie")
        ties+=1
    else:
        print("You lost...")
        losses+=1

